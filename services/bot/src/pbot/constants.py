# General Settings
# ------------------------------------------------------------------------------

BOT_NAME: str = 'PBot'
'''Name the bot should respond to and identify as.'''

# System Settings
# ------------------------------------------------------------------------------

ACTIVE_CHANNEL_CUTOFF_HOURS: int = 2
'''How recent must a channel be active'''

MESSAGE_HISTORY_CUTTOFF_HOURS: int = 8
''''How old can a message still be considered relevent'''

# Redis keys
# ------------------------------------------------------------------------------

# Prefixes

REDIS_CHANNEL_KEY_PREFIX: str = "channel"
'''Redis key-prefix for a channel'''

REDIS_MESSAGE_KEY_PREFIX: str = "message"
'''Redis key-prefix for a message'''

REDIS_RESPONSE_KEY_PREFIX: str = "response"
'''Redis key-prefix for a response'''

# Containers

REDIS_MESSAGES_KEY: str = "messages"
'''Redis key for all messages'''

REDIS_RESPONSES_KEY: str = "responses"
'''Redis key for all responses'''



# OpenAI-Related
# ------------------------------------------------------------------------------
REDIS_PROMPT_KEY = 'prompt'
OPENAI_MAX_TOKENS = 4097
'''OpenAI max tokens. This is model dependant.'''
OPENAI_MODEL = 'gpt-3.5-turbo'
'''OpenAI model to use.'''
OPENAI_TEMP = 1 # 0-2
'''Default model 'temperature' to use.'''
DEFAULT_TOKEN_ENCODING = 'cl100k_base'
'''How to count tokens.'''
