'''Bot runner.

In this file: configure dependencies, load middleware, run the bot.
'''

import os

from redis import Redis
from dotenv import load_dotenv

from pbot.bot import PBot
from pbot.constants import BOT_NAME
from pbot.logger import get_logger
from pbot.middleware.tacos import TacoRecipes


# Configure Environment
#######################

# Load environment variables.
load_dotenv()
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

# Get bespoke logger for service.
logger = get_logger()

# Redis client.
redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True)

# Create bot.
bot = PBot(redis, logger)


# Load Bot Middleware (order matters)
#####################################

# Tests your bot works out of the box.
bot.add_middleware(TacoRecipes(redis))


# Run the bot.
if __name__ == '__main__':
    logger.debug(f'Starting {BOT_NAME}.')
    bot.run()
