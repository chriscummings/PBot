from datetime import datetime, timedelta
from typing import Any

import tiktoken
from redis import Redis

from pbot.constants import DEFAULT_TOKEN_ENCODING
from pbot.constants import REDIS_RESPONSES_KEY
from pbot.constants import REDIS_RESPONSE_KEY_PREFIX
from pbot.constants import REDIS_CHANNEL_KEY_PREFIX
from pbot.constants import REDIS_MESSAGES_KEY
from pbot.constants import REDIS_MESSAGE_KEY_PREFIX

# TODO: rename to message_ids ?
def channel_message_ids(redis: Redis, channel_id: str, hours: int=1, mins: int=0) -> Any:
    '''Returns a list of message ids from a channel within timeframe.

    Args:
        redis (Redis): Redis connection
        channel_id (str): Channel to pull messages
        hours (int): include messages
        mins (int): include messages

    Returns:
        list: List of message ids (strings)
    '''
    msg_key = f'{REDIS_CHANNEL_KEY_PREFIX}:{channel_id}:{REDIS_MESSAGES_KEY}'

    cutoff = (datetime.now() - timedelta(hours=hours, minutes=mins)).timestamp()

    return redis.zrangebyscore(msg_key, cutoff, '+inf')

def mark_as_read(redis: Redis, messages: list[dict]) -> None:
    '''Mark messages are read.

    Args:
        redis (Redis): Redis connection
        messages (list): List of messages to be marked

    Returns:
        None
    '''
    for message in messages:
        redis.json().set(
            f'{REDIS_MESSAGE_KEY_PREFIX}:{message["id"]}',
            '.read',
            datetime.now().timestamp())

def active_channels(redis: Redis, hours: int=1, mins: int=0) -> list[str]:
    '''Channel ids with recent message activity.

    Args:
        redis (Redis): Redis connection
        hours (int): Hours ago to include message history
        mins (int): Minutes ago to include message history

    Returns:
        list[str]: List of channel ids
    '''
    cutoff = (datetime.now() - timedelta(hours=hours, minutes=mins)).timestamp()

    messages: Any = redis.zrangebyscore(REDIS_MESSAGES_KEY, cutoff, '+inf')

    channels = set()
    for message in messages:
        _, channel_id = (message.split('-')[0]).split('.')
        channels.add(channel_id)
    return list(channels)

def count_tokens(input: str, encoding: str=DEFAULT_TOKEN_ENCODING) -> int:
    '''(DEPRECATED: Will be moved to OpenAi-middleware.)
    Tokens in a string.

    Args:
        input (str): Sting to count
        encoding (str): Token encoding

    Returns:
        int: Count
    '''
    encoding = tiktoken.get_encoding(encoding)
    num_tokens = len(encoding.encode(input))
    return num_tokens

def get_messages(redis: Redis, ids: list[str]) -> list[dict]:
    '''Messages from a list of ids. Ignores unknown ids.

    Args:
        redis (Redis): Redis connection
        ids: (list): List of message ids

    Returns:
        list[dict]: List of message dicts
    '''
    messages = []
    for message_id in ids:
        message = redis.json().get(f'{REDIS_MESSAGE_KEY_PREFIX}:{message_id}')
        if message:
            messages.append(message)

    return messages

def create_response(redis: Redis, resp_id: str, content: str, msg_id: str) -> None:
    '''Creates a response entry in Redis.

    Args:
        redis (Redis): Redis connection
        resp_id (str): Id for response
        content (str): Response content
        msg_id (str): Message id responding to

    Returns:
        None
    '''
    # Get message responding to.
    key_message = get_messages(redis, [msg_id])[0]

    server_id = key_message['origin']['server']['id']
    channel_id = key_message['origin']['server']['channel']['id']
    user_id = key_message['user']['id']

    # Create response entry.
    mapping:dict = Response().mapping()
    mapping['id'] = resp_id
    mapping['user'] = user_id
    mapping['content'] = content
    mapping['message'] = msg_id
    mapping['channel'] = channel_id
    mapping['server'] = server_id
    mapping['time'] = datetime.now().timestamp()

    redis.hset(f'{REDIS_RESPONSE_KEY_PREFIX}:{resp_id}', mapping=mapping)

    # Create links to response entry.
    k = f'{server_id}.{channel_id}.{user_id}-{resp_id}'
    redis.zadd(REDIS_RESPONSES_KEY, {k: datetime.now().timestamp()})
    redis.json().set(f'{REDIS_MESSAGE_KEY_PREFIX}:{msg_id}', '.response', resp_id)

def is_refusal(content: str) -> bool:
    '''(DEPRECATED: Will be moved to OpenAi-middleware.)
    Was a AI refusal.

    Args:
        content (str): String

    Returns:
        bool: Boolean
    '''
    # FIXME: this is jank at best...
    refusal_substrings = [
        'Sorry, but I can\'t',
        'I\'m sorry, but',
        'I cannot comply',
        'As an AI',
        'As a large language model',
        'as a llm',
        'As an AI language model',
        'I apologize, but']

    for substring in refusal_substrings:
        if substring.lower() in content.lower():
            return True

    return False
