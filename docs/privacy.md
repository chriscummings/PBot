---
hide:
  - navigation
---

# Privacy

## Discord is Not Private

PBot operates on Discord, a third-party platform.
You should not assume any true privacy.

Do not transmit sensitive information over Discord.

## Middleware

Middleware you load into PBot may introduce additional privacy considerations. For example, the optional OpenAI middleware sends snippets of channel messages to OpenAI's ChatGPT service, which is a separate third-party platform.

## Data Collection and Retention

PBot can (optionally) store messages from any server it's invited to in a local Redis database. By default, messages are automatically deleted after 72 hours, based on an expiration configuration.

PBot does not include any telemetry or tracking features and does not collect or send your data.
