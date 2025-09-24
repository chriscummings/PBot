# Development Overview

This section will cover writing your own custom middleware against the API of
PBot.

PBot has two main service APIs: the **bot** and **transceiver**. It is the bot's
job to send channel history through any loaded
middleware whenever there is activity. The transceiver handles storing messages and sending
them to Discord.



**Current PBot Version:**
--8<-- "version"

[:fontawesome-solid-download:  Download PBot by Version](https://github.com/chriscummings/PBot/releases){ .md-button .md-button--primary }

-----





**Starting Points**

<div class="grid cards" markdown>
- [Writing Custom Middleware](writing-middleware.md)
</div>

<div class="grid cards" markdown>
- [Middleware API](bot/middleware.md)
</div>

<div class="grid cards" markdown>
- [Models API](models.md)
</div>

<br /><br /><br /><br /><br /><br /><br /><br /><br />