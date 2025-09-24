# Writing Middleware

Middleware in PBot serves as a way to intercept, inspect, modify, or respond to messages as they flow through the system. By writing custom middleware, you can add domain-specific logic without altering the core bot architecture.

**In this guide, you'll learn how to:**

- Create your own middleware by subclassing the `Middleware` class and implementing the required methods.

- Manage dependencies and resources (e.g., connections to Redis) in your middleware.

- Add custom logic, such as responding to particular keywords.

- Load your middleware.

This will be a hands-on example using a *“taco recipes”* middleware.

## Subclass Middleware

This first step in writing custom middleware is to create a Python file in `services/bot/src/pbot/middleware/`

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

:white_check_mark: The requirements of the Middleware class have been met with the implementation of the `handle_messages()` function.
From here you can experiment at will.

### Redis Access

We'll want our middleware to have access to the models in Redis, so let's create an
initializer method to accept and store the Redis connection that will be passed to it by PBot on instantiation.

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

We also want to respond to specific keywords in messages, so let's create a `KEYWORDS` constant to contain them.

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

We will change the `handle_messages()` function to address the following
example requirements:

- Create a response under the right keyword conditions.
- Provide a UID for that response.
- Populate the response with a random taco recipe from a list.

Add the following imports:

```py title="tacos.py"
import random
from datetime import datetime
from pbot.utils import create_response
from recipes import TACO_RECIPES
```

Update the business logic of the `handle_messages()` method to fullfil the example requirements.

The code below does the following:

- Sorts messages by time.
- Ignores bot messages and previously responded messages.
- Creates a response containing a random taco recipe if a keyword is found.
- Returns the messages (to be passed to any following middleware).

At the end of the middleware chain, each message in the list is marked as read.

```py title="tacos.py"
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

!!! note "A timestamp as a UID isn't the ideal solution. This will be patched 1.0."

## Loading the Middleware

### Import the Middleware

To load middleware, import it in the bot file: `pbot/services/bot/src/app.py`

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

The bot service will now need to be restarted.
