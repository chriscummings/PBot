# Middleware

All PBot middleware must inerit from the `Middleware` class. It's a minimal interface with
a singular, `handle_messages()` function to implement.

## Example

```py title="Example"  linenums="1"  hl_lines="4"
from pbot.middleware.base import Middleware


class MySuperCoolMiddleware(Middleware):

  def handle_messages(self, messages: list[dict]) -> list[dict]:
    return []
```

For a more detailed example of custom middleware, see the `TacoRecipes` example in [**Writing Middleware**](../writing-middleware.md#create-a-minimal-class).

------

## Class API

::: services.bot.src.pbot.middleware.base
