# Writing Middleware

Middleware in PBot allows you to intercept, inspect, modify, or respond to messages as they flow through the system. By writing custom middleware, you can add domain-specific logic without touching the core bot architecture.

**In this guide, you'll learn how to:**

- Create custom middleware by subclassing Middleware and implementing required methods.
- Manage dependencies and resources, such as Redis connections.
- Add custom logic, such as responding to specific keywords.
- Load and run your middleware.

We'll demonstrate with a “taco recipes” middleware example.

## Subclass Middleware

Create a Python file in `services/bot/src/pbot/middleware/`:

```text
pbot/
├─ docs/
└─ services/
   └─ bot/
      └─ src/
         └─ pbot/
            └─ middleware/
               └─ base.py
               └─ tacos.py
```
### Create a Minimal Class

Create a class that inherits from `Middleware` and implements the `handle_messages()` function.

```py title="tacos.py" linenums="1"
from pbot.middleware.base import Middleware

class TacoRecipes(Middleware):

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []
```

:white_check_mark: At this point, your class satisfies the Middleware interface.

### Redis Access

To interact with Redis, define an initializer that stores the Redis connection passed by PBot:

```py title="tacos.py" hl_lines="6 7" linenums="1"
from redis import Redis
from pbot.middleware.base import Middleware

class TacoRecipes(Middleware):

  def __init__(self, redis: Redis) -> None:
    self.redis = redis

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []

```

### Responding to Keywords

Add a KEYWORDS constant to define triggers for your middleware:

```py title="tacos.py" hl_lines="6" linenums="1"
from redis import Redis
from pbot.middleware.base import Middleware

class TacoRecipes(Middleware):

  KEYWORDS: list[str] = ["taco"]

  def __init__(self, redis: Redis) -> None:
    self.redis = redis

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []
```


###  Overriding `handle_messages()`

Update `handle_messages()` to:

- Sort messages by timestamp.
- Ignore bot messages and previously responded messages.
- Create a response containing a random taco recipe when a keyword is found.
- Return messages for downstream middleware.

```py title="tacos.py"
import random
from datetime import datetime
from pbot.utils import create_response
from recipes import TACO_RECIPES

[...]

def handle_messages(self, messages: list[dict]) -> list[dict]:
  # Sort earliest messages first.
  messages.sort(key=lambda m: float(m['time']))

  for message in messages:

      # Don't respond to bot messages.
      if int(message['user']['bot']) == 1:
          continue

      # Don't respond to already responded messages.
      if message['response']:
          continue

      for keyword in self.KEYWORDS:

          # Respond if keyword is found in the message.
          if keyword.lower() in message['content'].lower():

              # Create a unique, arbitrary GUID for the response.
              id = f'taco{datetime.now().timestamp()}'

              # Preach the gospel of tacos.
              create_response(
                  self.redis,
                  id,
                  random.choice(TACO_RECIPES),
                  message['id'])

              # Move on to next message.
              break

  # Return messages for any follow-on middleware to handle.
  return messages
```

## Loading the Middleware

### Import the Middleware

In `pbot/services/bot/src/app.py`:

```text title="pbot/app.py"
pbot/
├─ docs/
└─ services/
   └─ bot/
      └─ src/
         └─ pbot/
         └─ app.py
```

```py title="app.py"
from pbot.middleware.tacos import TacoRecipes
```

### Add the Middleware Module

Add middleware to the bot with the `add_middleware()` method.


```py title="app.py" hl_lines="18"
[...]

from pbot.middleware.tacos import TacoRecipes

[...]

# Set up Redis client
redis = Redis(
  host=REDIS_HOST,
  port=REDIS_PORT,
  decode_responses=True)

[...]

# Load bot middleware (Order matters!)
# ------------------------------------------------------------------------------

bot.add_middleware(TacoRecipes(redis))

[...]
```

### Restart the Bot

After adding your middleware, restart the bot service to apply changes.