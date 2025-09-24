# General Settings
##################

BOT_NAME: str = 'PBot'
'''Name the bot'''

# System Settings
#################

ACTIVE_CHANNEL_CUTOFF_HOURS: int = 2
'''How recent is active'''

MESSAGE_HISTORY_CUTTOFF_HOURS: int = 8
''''How old is irrelevent'''

# Redis keys
############

# Prefixes

REDIS_CHANNEL_KEY_PREFIX: str = 'channel'
'''Key-prefix for a channel'''

REDIS_MESSAGE_KEY_PREFIX: str = 'message'
'''Key-prefix for a message'''

REDIS_RESPONSE_KEY_PREFIX: str = 'response'
'''Key-prefix for a response'''

# Containers

REDIS_MESSAGES_KEY: str = 'messages'
'''Key for all messages'''

REDIS_RESPONSES_KEY: str = 'responses'
'''Key for all responses'''

# TODO: Move these to OpenAi middleware.
# OpenAI-Related
################

REDIS_PROMPT_KEY = 'prompt'
'''(DEPRECATION WARNING)'''

OPENAI_MAX_TOKENS = 4097
'''(DEPRECATION WARNING) OpenAI max tokens. This is model dependant.'''

OPENAI_MODEL = 'gpt-3.5-turbo'
'''(DEPRECATION WARNING) OpenAI model to use.'''

OPENAI_TEMP = 1 # 0-2
'''(DEPRECATION WARNING) Default model 'temperature' to use.'''

DEFAULT_TOKEN_ENCODING = 'cl100k_base'
'''(DEPRECATION WARNING) How to count tokens.'''
