# Project Overview

!!! example

    Warning: This is pre version 1 software (
    --8<-- "version"
    ).


PBot is a Dockerized application composed of two core services:

- **Transceiver** – Handles communication with Discord.
- **Bot** – Runs the middleware logic that powers your chatbot.

```mermaid
---
title: PBot Flow
---
graph LR
  Discord@{shape: cloud}<-->Y[Tranceiver Service];
  subgraph Docker

  Y[Tranceiver Service]<-->Redis[(Redis Database)];
  Redis[(Redis Database)]<-->Bot[PBot Service];
  Bot[PBot Service]-->Middleware@{shape: processes};
  Middleware@{shape: processes}-->Bot[PBot Service];
  end
  style Docker fill: none, stroke-dasharray: 5 5
```

PBot takes inspiration from MVC-style web frameworks, centering its design on
middleware. The framework handles the boilerplate and peripheral details of
writing a Discord bot, so you can focus entirely on your bot's logic.

## Middleware

Middleware in PBot is a stack of one or more modules. Each module receives the
current message history, can transform or act on it, and then passes the
result along to the next module in the chain.

At its simplest, middleware is a single Python class that inherits from
`pbot.middleware.base.Middleware`. To create your own, you only need to
implement one method:

```py title="handle_messages()"
def handle_messages(self, messages: list[dict]) -> list[dict]:
  return []
```

This method accepts a list of messages and must return a list. What happens in
between—filtering, transforming, augmenting, or generating responses—is
entirely up to you.

## Project Structure

```text
pbot/
├─ docs/
├─ services/
│  ├─ bot/
│  │  ├─ src/
│  │  │  ├─ pbot/
│  │  │  │  ├─ middleware/
│  │  │  │  │  └─ base.py (Abstract class all middleware inherit)
│  │  │  │  ├─ bot.py (PBot class)
│  │  │  │  ├─ constants.py
│  │  │  │  ├─ logger.py
│  │  │  │  └─ utils.py
│  │  │  ├─ app.py
│  │  │  └─requirements.txt
│  │  └─ Dockerfile (Docker entry point)
│  └─ transceiver/
│     ├─ src/
│     │  ├─ transceiver/
│     │  │  ├─ constants.py
│     │  │  ├─ logger.py
│     │  │  ├─ models.py
│     │  │  ├─ process_mgs.py (Logic for storing and sending message)
│     │  │  └─ utils.py
│     │  ├─ app.py (Docker entry point)
│     │  └─ requirements.txt
│     └─ Dockerfile
├─ docker-compose.yaml
├─ example.env (Template for .env)
├─ LICENSE
├─ README.md
├─ requirements.txt
└─ version
```
