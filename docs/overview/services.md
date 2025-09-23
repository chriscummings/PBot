# Services

### Tranceiver Service

A lightweight, event-driven service meant to transmit responses to and from Discord. If you don’t need to modify the models stored in Redis, you won’t need to delve into the transceiver service.

### Bot Service

The bot proper constantly scans for new messages stored in Redis and submits message history through the middleware stack.

### Redis Service

In-memory data store between the bot and the transceiver service.

### Redis Insight Service

Provides a local GUI for the Redis service.
