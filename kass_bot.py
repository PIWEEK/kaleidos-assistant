#!/usr/bin/env python

import os

from mmpy_bot import Bot, Settings
from kass_plugin.kass_plugin import KassPlugin


bot = Bot(
    settings=Settings(
        MATTERMOST_URL=os.getenv('MATTERMOST_URL'),
        MATTERMOST_PORT=443,
        BOT_TOKEN=os.getenv('BOT_TOKEN'),
        BOT_TEAM="PIWEEK",
        SSL_VERIFY=True,
    ),  # Either specify your settings here or as environment variables.
    plugins=[KassPlugin()],  # Add your own plugins here.
)
bot.run()
