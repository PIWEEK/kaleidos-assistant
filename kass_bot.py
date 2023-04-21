#!/usr/bin/env python

import os

from mmpy_bot import Bot, Settings
from kass_plugin.kass_plugin import KassPlugin


bot = Bot(
    settings=Settings(
        MATTERMOST_URL=os.getenv('MATTERMOST_URL'),
        MATTERMOST_PORT=os.getenv('MATTERMOST_PORT'),
        BOT_TOKEN=os.getenv('BOT_TOKEN'),
        BOT_TEAM=os.getenv('BOT_TEAM'),
        SSL_VERIFY=os.getenv('SSL_VERIFY'),
    ),  # Either specify your settings here or as environment variables.
    plugins=[KassPlugin()],  # Add your own plugins here.
)
bot.run()
