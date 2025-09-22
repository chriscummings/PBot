# Run PBot

## Install Docker

PBot has several moving parts and dependencies. To make PBot easy to use and run consistently across devices, it’s bundled as a Docker application. Docker is the only dependency you’ll need to install to run PBot.

### What is Docker?

Docker is a tool that allows software and any required services to run inside a sandboxed, containerized environment. This means the application is packaged with everything it needs, including databases, libraries, and any other necessary components.

### Downloading Docker

At a minimum, you’ll need Docker, the command-line tool. Optionally, you can also install Docker Desktop, a GUI for managing Docker containers.

## Download PBot

Visit the official PBot GitHub page, github.com/chriscummings/PBot, or directly download a zipped copy of the code.

## Configuring PBot for its First Run

### Set Your Discord Application Token

It’s common practice to store sensitive data, such as passwords or API keys, in environment variables instead of hard-coding them into the application.

An environment variable is simply a piece of data stored in memory while a program is running. An application can access the data without having to write it to disk. This keeps secrets out of the source code, limiting the risk of accidentally exposing them when sharing code or storing it in version control.

This data, initially at least, must be recorded somewhere. This place is a special file conventionally named .env.

In the root directory of PBot is a file named example.env. Create a copy of this file next to the original and rename it .env.

Renaming example.env to .env may cause the file to disapear depending on your operating system. Filenames starting with a dot are conventionally understood to be hidden system files and many operating systems hide these files by default.



__To show hidden files__

| OS      | Keyboard Shortcut          |
| ------- | -------------------------- |
| OSX     | press: Shift + Command + . |
| Windows | press: Ctrl + Shift + .    |
| Linux   | press: Ctrl + H            |

## Running PBot

Create a copy of the file example.env with the filename .env.

```text
docs/
├─ index.md
├─ guides/
│  ├─ getting-started.md
│  └─ usage.md
└─ reference/
   ├─ api.md
   └─ cli.md
```

Replace the ??? with the secret application token provided by Discord.

### Starting the Application container

Navigate to the root directory of PBot and execute the following command:

docker-compose up -d

The -d parameter signals to Docker that the session should be detached. This way, you can close the terminal without also closing the running Docker application.

Docker will pull down the required Docker images needed for PBot. The process may take a few minutes to complete.

<figure markdown="span">
	![weqwe](images/running/pulling-images.png)
	<figcaption>
		Docker Pulling Images
    </figcaption>
</figure>

Once the prerequisites are downloaded and the application built, four services should be listed as started.

<figure markdown="span">
	![weqwe](images/running/containers-running.png)
	<figcaption>
		Successful Launch
    </figcaption>
</figure>

If you have Docker Desktop installed, you will see a green indicator for all four services.

<figure markdown="span">
	![weqwe](images/running/docker-desktop-running.png)
	<figcaption>
		All Services Running on Docker Desktop
    </figcaption>
</figure>

At this point, if you check your Discord server, your bot should be listed as logged in.

<figure markdown="span">
	![weqwe](images/running/bot-online.png)
	<figcaption>
		A Live Bot
    </figcaption>
</figure>

You can test it by any mention of the word ‘taco.’

<figure markdown="span">
	![weqwe](images/running/bot-responds.png)
	<figcaption>
		Taco Time!
    </figcaption>
</figure>

Congratulations, your instance of PBot is running and connected.
