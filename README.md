## Kaleidos AI assistant

This repository contains the code required to install a bot in Mattermost, which is able to answer direct questions from users, according to the `gpt3.5-turbo` model. 

Responses will be based on a context taken from a public text document.

### How to start

Install a new virtual environment for Python
```shell
python3.10 -m venv .venv
```

Load the .venv
```shell
. .venv/bin/activate
```

Install the requirements
```shell
pip install -r requirements.txt
```

Create an `.env` file with the following variables:
 - DOC_URL: text document with the context to feed the model in order to build its answers
- OPENAI_API_KEY: a valid API_KEY in [OpenAI](https://platform.openai.com/account/api-keys)
- OPENAI_ORGANIZATION: your organization in [OpenAI](https://platform.openai.com/account/org-settings)


- MATTERMOST_URL: the Mattermost url where the bot will run
- MATTERMOST_PORT: the port to access Mattermost
- SSL_VERIFY: is Mattermost running under http (True) or https (False)
- BOT_TOKEN: the Mattermost's token you get when the bot is created
- BOT_TEAM: the Mattermost's team you want the ot to be accesible

Example: 
```dotenv
# AI Context settings
DOC_URL=https://docs.google.com/document/u/0/export?format=txt&id=1iA8frcx75lQwsNNkCvs...
OPENAI_API_KEY=sk-JizVlXDGbYULx...
OPENAI_ORGANIZATION=org-jBUyIFlru...

# Mattermost Bot settings
MATTERMOST_URL=https://...
MATTERMOST_PORT=443
SSL_VERIFY=True
BOT_TOKEN=k77b5un...
BOT_TEAM=MATTERMOST_TEAM
```

### Mattermost bot

This bot takes any direct question performed to the `kaia`user answering according to the model `gpt-3.5-turbo`.

To start the bot, simply execute:

```bash
./kass_bot.py
```

### Making questions

Simply write a direct message to the Mattermost bot with your question and wait for the reponse. It just requires any running bot in the background.

> Note: If you have to running bots you'll get two answers!


### References
- https://platform.openai.com/docs/tutorials/web-qa-embeddings
- https://github.com/openai/openai-cookbook/tree/main/apps/web-crawl-q-and-a
- https://github.com/attzonko/mmpy_bot
