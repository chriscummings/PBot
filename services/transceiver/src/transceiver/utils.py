from datetime import datetime
from urllib.parse import urlparse
from typing import Any

import redis
import discord

from transceiver.process_msg import process_msg
from transceiver.logger import logger
from transceiver.constants import (
	REDIS_KEY_RESPONSES,
    REDIS_KEY_RESPONSE_PREFIX,
    DISCORD_CHARACTER_LIMIT,
    RESPONSE_DELVE_TIME
)

def intents() -> discord.Intents:
	'''Returns a configured Intents object for a Discord a client.

    By default, a bot does not have access to messages or their contents.
    Instead, permission has to be explicitly given to the bot for access to
    that information.
    See docs:
    https://discordpy.readthedocs.io/en/stable/intents.html

    Returns:
        discord.Intents: A Discord intents object for client.
	'''
	intents = discord.Intents.default()
	intents.messages = True
	intents.message_content = True
	return intents

async def send_message(message: discord.Message, content: str) -> None:
    '''Asynchronously sends response to a specific Discord message.

    Args:
        message (discord.Message): Message to respond
        content (str): Body
    '''
    try:
        await message.reply(content)
    except Exception as error: # FIXME: too permissive--don't try forever
        logger.error(error)

async def handle_response(discord_client: discord.Client, redis_conn: redis.Redis, response: dict[str, any]) -> None:
    '''Asynchronously handles sending single/multi-part messages to Discord.

    Args:
        response (dict[str, id]): Dictionary represensation
    '''
    # Dig up Discord message to respond to via API calls.
    channel: Any = discord_client.get_channel(int(response['channel']))
    message: Any = channel.get_partial_message(int(response['message']))

    # Handle multi-part responses due to length.
    if len(response['content']) > DISCORD_CHARACTER_LIMIT:
        chunks = chunk_str(response['content'], DISCORD_CHARACTER_LIMIT)

        for chunk in chunks:
            # Await each message so the response messages are in order.
            await send_message(message, chunk)

    else:
       await send_message(message, response["content"])

    # Mark response as sent.
    redis_conn.hset(
        f'{REDIS_KEY_RESPONSE_PREFIX}:{response["id"]}',
        'sent', str(datetime.now().timestamp())
    )

def handle_message(redis_conn: redis.Redis, message: discord.Message) -> None:
    '''Handle an incoming Discord message.

    Args:
        redis (redis.Redis): Redis connection
        message (discord.Message): Discord Message
    '''
    logger.debug(format_message_for_log(message))
    process_msg(redis_conn, message)

def get_unsent_responses(redis_conn: redis.Redis) -> list[dict]:
    '''Unsent responses.

    Args:
		redis_conn (redis.Redis): Redis connection

	Returns:
		list[dict]: A list of unsent response dicts
    '''
    cutoff = (datetime.now() - RESPONSE_DELVE_TIME).timestamp()

    # Get recent responses.
    responses: Any = redis_conn.zrangebyscore(
        REDIS_KEY_RESPONSES, cutoff,
        '+inf',
        withscores=False)

    unsent = []

    for mixed_key in responses: # response:<server_id>.<channel_id>.<user_id>-<response_id>

        # Remove prefix
        mixed_key = mixed_key.replace(f"{REDIS_KEY_RESPONSE_PREFIX}:", "") # <server_id>.<channel_id>.<user_id>-<response_id>

        # Unpack ids from mixed key.
        server_channel_user, resp_id = mixed_key.split("-") # "<server_id>.<channel_id>.<user_id>", "<response_id>"
        server_id, channel_id, user_id = server_channel_user.split(".") # ""<server_id>", "<channel_id>", "<user_id>"

        # Pull related objects.
        # TODO: Handle missing...
        response = redis_conn.hgetall(f"{REDIS_KEY_RESPONSE_PREFIX}:{resp_id}")
        server = redis_conn.hgetall(f"server:{server_id}")
        channel = redis_conn.hgetall(f"channel:{channel_id}")
        user = redis_conn.hgetall(f"user:{user_id}")

        # Handle an unsent response.
        if response and (response["sent"] == None or response["sent"] == ""):

            print("-")

            # Ensure Server, Channel, and User are allowed responses.
            if all([
                int(server["respond"]) == 1,
                int(channel["respond"]) == 1,
                int(user["respond"]) == 1
            ]): # FIXME: handle ignored responses clogging queue.
                unsent.append(response)

    return unsent

def format_message_for_log(message: discord.Message) -> str:
    '''String representation of Discord Message.

    Args:
        message (discord.Message): Discord Message

    Returns:
        str: Formatted Message
    '''
    # Log statement template.
    tremplate = '{created}|{msg_id}|{server}.{channel}|{author}({nick}):{content}'

    # Populate template.
    tremplate = tremplate.replace('{created}', str(message.created_at))
    tremplate = tremplate.replace('{msg_id}', str(message.id))
    tremplate = tremplate.replace('{server}', message.guild.name)
    tremplate = tremplate.replace('{channel}', message.channel.name)
    tremplate = tremplate.replace('{author}', message.author.name)
    tremplate = tremplate.replace('{nick}', str(message.author.nick))
    tremplate = tremplate.replace('{content}', message.content)

    return tremplate

def chunk_str(string: str, size: int) -> list[str]:
    '''Breaks string up on whitespace by chunk size.

    Args:
		string (str): String to chunk.
        size (int): Character length to chunk by

    Returns:
		list[str]: A list of strings
    '''
    if len(string) > size:
        all_chunks = []
        current_line = ''
        words = string.split(' ')

        for word in words:
            # If str wouldn't exceed chunk size:
            if (len(current_line) + len(word) + 1) < size:
                # If its the initial, empty line.
                if current_line == '':
                    current_line = str(word)
                # Otherwise append + space.
                else:
                    current_line += ' '+str(word)
            # Otherwise, start a new chunk
            else:
                all_chunks.append(current_line)
                current_line = str(word)

        # Append last chunk segment.
        all_chunks.append(current_line)

        return all_chunks

    return [string]
