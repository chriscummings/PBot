A Note on Privacy
#################

==========================
Discord is Not Private
==========================

This project is based on Discord, a private 3rd party service.
You should have no expectation of true privacy.
Do **not** transmit sensitive information over Discord.

==========
Middleware
==========

Middleware you load into the bot may also have privacy concerns.
The OpenAI middleware, for example, is a direct integration with OpenAI's ChatGPT that sends channel chat snippets to another private 3rd party.

=============================
Data Collection and Retention
=============================

PBot (optionally) stores messages from every channel of any server it's invited to.
These messages are temporarily stored within a local Redis database.
By default, each stored chat message is automatically deleted after 72 hours based on an `expiration configuration setting <api_transceiver.constants.html#transceiver.constants.REDIS_MESSAGE_EXPIRE_SECONDS>`_.

The PBot project has zero code for telemetry and no interest in your data.
