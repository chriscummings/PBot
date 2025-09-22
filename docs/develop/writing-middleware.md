# Writing Middleware

This first step in writing custom middleware is to create a Python file in services/bot/src/pbot/middleware/

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

In this tutorial, we will recreate the tacos middleware seen in the Getting Started section.

## Create middleware

Create a class that inherits from Middleware and implements the handle_messages() function.

```py title="tacos.py" linenums="1"
from pbot.middleware.base import Middleware


class TacoRecipes(Middleware):

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []
```

We’ll want our middleware to have access to Redis, so let’s create an initializer method to accept and store a Redis connection.

```py title="tacos.py" hl_lines="7 8" linenums="1"
from redis import Redis
from pbot.middleware.base import Middleware


class TacoRecipes(Middleware):

  def __init__(self, redis: Redis) -> None:
    self.redis = redis

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []

```

We also want to respond to specific keywords, so let’s create a KEYWORDS constant to contain those.

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

The requirements for our handle_messages() implementation are:

- Create a response under the right conditions.
- Provide a UID for that response.
- Populate the response with a random taco recipe from a list.

We will thus add the following imports:

```py title="tacos.py"
import random
from datetime import datetime
from pbot.utils import create_response
from recipes import TACO_RECIPES
```

Click here to see the [Taco Recipes Module](https://pbot.readthedocs.io/en/latest/recipes.html).

!!! note "A timestamp as a UID isn’t the ideal solution, but it will work for now."

Now, let’s focus on the business logic of the handle_messages() method.

The code below does the following:

- Sort messages by time.
- Skips bot and previously responded messages.
- Creates a response containing a random taco recipe if a keyword is found.
- Returns the messages (to be passed to any following middleware).

At the end of the middleware chain, each message in the list is marked as read.

```py title="tacos.py"

def handle_messages(self, messages: list[dict]) -> list[dict]:

  # Sort earliest messages first
  messages.sort(key=lambda m: float(m['time']))

  for message in messages:

    # Don't respond to bot messages
    if int(message['user']['bot']) == 1:
      continue

    # Don't respond to already responded-to messages
    if message['response']:
      continue

    for keyword in self.KEYWORDS:

      # Respond if a keyword is found in the message
      if keyword.lower() in message['content'].lower():

        # Create a unique, arbitrary GUID for the response
        resp_id = f'taco{datetime.now().timestamp()}'

        # Create a response about the gospel of tacos
        create_response(
          self.redis,
          resp_id,
          random.choice(TACO_RECIPES),
          message["id"])

        # Move on to any additional messages
        break

  # Return message list to any follow-on middleware to handle.
  return messages
```

## Loading the Middleware

To load middleware, import it in the bot pbot/services/bot/src/app.py file.

```text
pbot/
├─ docs/
└─ services/
   └─ bot/
      └─ src/
         └─ pbot/
         └─ app.py
```

Import the middleware module.

Then, add it to the bot using the add_middleware() method.

```py title="tacos.py" hl_lines="3 18"
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

Notice that the redis connection object is being passed to the middleware initializer here.

After restarting the bot, the middleware will be loaded.
