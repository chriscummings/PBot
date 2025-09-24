import os
from datetime import (
	datetime,
	timedelta)

# Bot
#####

TRANSCEIVER_RESPONSE_DELAY: int = 2
'''Delay between polling for new responses to send.'''

RESPONSE_DELVE_TIME: timedelta = timedelta(hours=1)
'''How long ago to look for unsent responses.'''

# System

DISCORD_CHARACTER_LIMIT: int = 2000
'''Discord message character limit'''

# Redis
#######

REDIS_MESSAGE_EXPIRE_SECONDS: int = 25920060 # 3 Days
'''How long to persist Discord messages in Redis.'''

# Keys

REDIS_KEY_MESSAGES: str = 'messages'
'''Key for messages'''

REDIS_KEY_SERVERS: str  = 'servers'
'''Key for servers'''

REDIS_KEY_CHANNELS : str = 'channels'
'''Key for channels'''

REDIS_KEY_USERS: str  = 'users'
'''Key for users'''

REDIS_KEY_RESPONSES: str  = 'responses'
'''Key for responses'''

# Key-Prefixes

REDIS_KEY_MESSAGE_PREFIX: str = 'message'
'''Key-prefix for a Message'''

REDIS_KEY_SERVER_PREFIX: str = 'server'
'''Key-prefix for a Server'''

REDIS_KEY_CHANNEL_PREFIX: str = 'channel'
'''Key-prefix for a Channel'''

REDIS_KEY_USER_PREFIX: str = 'user'
'''Key-prefix for a user'''

REDIS_KEY_RESPONSE_PREFIX: str = 'response'
'''Key-prefix for a Response'''
