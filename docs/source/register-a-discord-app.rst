Register a Discord App
##############################

The first step in getting PBot running is registering your private bot with Discord to obtain an API key. Navigate to the `Discord Developer Portal <https://discord.com/developers/applications>`_.

-----

Click on the **New Application** button to start the process of registering your bot.

.. figure:: _static/discord-app-setup/discord-new-app.png
   :align: center

   Default Empty Applications Page

-----

You'll first be prompted to name your bot. This is how the bot will be displayed to your users.
In this guide, we will be building a bot that disseminates taco recipes to the masses; thus, we will name it simply "Taco Lover."


.. figure:: _static/discord-app-setup/discord-name-app.png
   :align: center

   Naming an Application

-----

Now that the bot is registered, we can add a profile picture for it.


.. figure:: _static/discord-app-setup/discord-app-created.png
   :align: center

   Newly Created Application

We will use McFriendy's *Taco Lover (2024)* as the bot's profile picture. `(Link) <https://www.instagram.com/p/C6l8TqEpDnf/>`_

.. figure:: _static/discord-app-setup/discord-app-pfp.png
   :align: center

   Delightful

( See more of Mcfriendy's paintings on `her Instagram <https://www.instagram.com/mcfriendy/>`_. )

-----

Once you've customized your application, navigate to the **Bot** page under **Settings** and click on the **Reset Token** button.

.. figure:: _static/discord-app-setup/discord-reset-token.png
   :align: center

   Reset Token button

-----

You will be prompted for confirmation, as this would usually break any apps using a previous token.


.. figure:: _static/discord-app-setup/discord-confirm-reset.png
   :align: center

   Confirm Token Reset

-----

.. figure:: _static/discord-app-setup/discord-token-generated.png
   :align: center

   New Token Generated

------

After doing so, the page will only display your secret token temporarily. Copy it down now in a secure location.


.. figure:: _static/discord-app-setup/discord-copy-token.png
   :align: center

   Copy Temporarily Visible Token

-----


Under **Privileged Gateway Intents**, you'll need to turn on **MESSAGE CONTENT INTENT** to allow your bot to view message contents.

.. figure:: _static/discord-app-setup/discord-privileged-intents.png
   :align: center

   Privileged Intents

-----

Now, navigate to the **Installation** page under **Settings**.

Beneath **Installation Contexts**, ensure **Guild Install** is checked.


.. figure:: _static/discord-app-setup/discord-installation-contexts.png
   :align: center

   Installation Contexts

-----

Scroll down to **Default Install Settings**, and then select **bot** for **SCOPES**.


.. figure:: _static/discord-app-setup/discord-default-installation-settings.png
   :align: center

   Guild Install Scopes

-----

For **PERMISSIONS**, you'll need a minimum of **Read Message History** and **Send Messages**. For more complex bots, you'll likely need additional permissions.

.. figure:: _static/discord-app-setup/discord-minimum-permissions.png
   :align: center

   Minimum Permissions

-----

Now, scroll up to **Install Link** and select **Discord Provided Link**.

Copy the generated Discord link. It'll start with *https://discord.com/oauth2/...*


.. figure:: _static/discord-app-setup/discord-install-link.png
   :align: center

   Install Link

-----

Open the provided Discord link and select **Add to Server**.

.. figure:: _static/discord-app-setup/discord-opened-install-link.png
   :align: center

   Opened Install Link


-----

Review the permissions listed.

.. figure:: _static/discord-app-setup/discord-add-app-1.png
   :align: center

   permissions

----

Select the server you wish to add the bot to.

.. figure:: _static/discord-app-setup/discord-add-app-2.png
   :align: center

   choose Server

-----

If you're satisfied, click Authorize.

.. figure:: _static/discord-app-setup/discord-authorize-app.png
   :align: center

   authorize

----

Success!

.. figure:: _static/discord-app-setup/discord-app-added-success.png
   :align: center

   Success

----

At this time, your bot should have already joined the server.

.. figure:: _static/discord-app-setup/discord-bot-joined.png
   :align: center

   Welcome

----

The bot, however, is not yet active. That will change when we get your instance of PBot running in the next section.

.. figure:: _static/discord-app-setup/discord-bot-offline.png
   :align: center

   offline bot
