# Development Overview

This section covers how to write your own custom middleware using the PBot API.

PBot consists of two primary service APIs:

- **Bot API** – Responsible for passing channel message history through any loaded middleware whenever activity occurs.
- **Transceiver API** – Handles storing messages in Redis and sending them to Discord.

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