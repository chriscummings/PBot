Writing Middleware
#####################

This first step in writing custom middleware is to create a Python file in ``services/bot/src/pbot/middleware/``

.. raw:: html
   :file: _static/writing-middleware/folder.html

----

In this tutorial, we will recreate the tacos middleware seen in the Getting Started section.

Create a class that inherits from ``Middleware`` and implements the ``handle_messages()`` function.

.. raw:: html
   :file: _static/writing-middleware/first-middleware-1.html

----

We'll want our middleware to have access to Redis, so let's create an initializer method to accept and store a Redis connection.

.. raw:: html
   :file: _static/writing-middleware/first-middleware-2.html

-----

We also want to respond to specific keywords, so let's create a ``KEYWORDS`` constant to contain those.

.. raw:: html
   :file: _static/writing-middleware/first-middleware-3.html

-----


The requirements for our ``handle_messages()`` implementation are:

- Create a response under the right conditions.
- Provide a UID for that response.
- Populate the response with a random taco recipe from a list.

We will thus add the following imports:

.. code-block:: python

   import random
   from datetime import datetime
   from pbot.utils import create_response
   from recipes import TACO_RECIPES

Click here to see the :doc:`recipes`.

.. note::
   A timestamp as a UID isn't the ideal solution, but it will work for now.

-----

Now, let's focus on the business logic of the ``handle_messages()`` method.

The code below does the following:

- Sort messages by time.
- Skips bot and previously responded messages.
- Creates a response containing a random taco recipe if a keyword is found.
- Returns the messages (to be passed to any following middleware).

At the end of the middleware chain, each message in the list is marked as read.

.. raw:: html
   :file: _static/writing-middleware/first-middleware-5.html


Loading the Middleware
-------------------------------------

To load middleware, import it in the bot ``pbot/services/bot/src/app.py`` file.

.. raw:: html
   :file: _static/writing-middleware/load-app-file.html


Import the middleware module.

Then, add it to the bot using the ``add_middleware()`` method.

.. raw:: html
   :file: _static/writing-middleware/add-your-middleware.html

Notice that the redis connection object is being passed to the middleware initializer here.

After restarting the bot, the middleware will be loaded.