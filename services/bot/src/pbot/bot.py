from logging import Logger
from typing import NoReturn

from redis import Redis

from pbot.middleware.base import Middleware
from pbot.utils import active_channels
from pbot.utils import get_messages
from pbot.utils import channel_message_ids
from pbot.utils import mark_as_read
from pbot import constants


class PBot:
    '''PBot is a lightweight handler that is merely meant to pass message
    history to a stack of middleware layers, where the real work is done.
    '''

    middlewares: list[Middleware] = []
    '''Middleware to pass message history'''

    def __init__(self, redis: Redis, logger: Logger) -> None:
        '''PBot constructor.

        Args:
            redis (Redis): Redis connection
            logger (Logger): Logger

        Returns:
            None
        '''

        self.redis = redis
        self.logger = logger

    def add_middleware(self, middleware: Middleware) -> None:
        '''Adds middleware to bot.

        Args:
            middleware (Middleware): Middleware to load

        Returns:
            None
        '''

        self.middlewares.append(middleware)

    def handle_messages(self, messages: list[dict]) -> None:
        '''Pushes a stack of message history through middleware.

        Args:
            messages (list): List of message dicts

        Returns:
            None
        '''

        message_buffer = messages
        for middleware in self.middlewares:
            message_buffer = middleware.handle_messages(message_buffer)

    def run(self) -> NoReturn:
        '''Endlessly loops bot over recently active channels.

        Returns:
            None
        '''

        while True:
            for channel_id in active_channels(
                    self.redis,
                    hours=constants.ACTIVE_CHANNEL_CUTOFF_HOURS):

                # Skip ignored channels.
                channel = self.redis.hgetall(
                    f'{constants.REDIS_CHANNEL_KEY_PREFIX}:{channel_id}'
                )

                if int(channel['parse']) != 1:
                    continue

                # Fetch message history.
                message_ids = channel_message_ids(
                    self.redis,
                    channel_id,
                    hours=constants.MESSAGE_HISTORY_CUTTOFF_HOURS
                )

                messages = get_messages(self.redis, message_ids)

                # Skip channel if all the messages are already read.
                if len(list(filter(lambda m: m['read'] == None, messages))) < 1:
                    continue

                # Push messages through middleware.
                self.handle_messages(messages)

                # Clean up.
                mark_as_read(self.redis, messages)
