# Services in Detail

### Tranceiver Service

A lightweight, event-driven service that handles communication with Discord.
In most cases, you won't need to interact with the Transceiver directly unless
you plan to modify the models stored in Redis.

### Bot Service

The heart of PBot. This service continuously scans Redis for new messages and
runs the message history through the middleware stack.

### Redis Service

An in-memory data store that sits between the Bot and Transceiver services, acting as the message bus.

### Redis Insight Service

A local GUI for inspecting and interacting with the Redis service, useful for debugging and monitoring.