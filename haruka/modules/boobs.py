from telegram import ChatAction
from haruka.modules.helper_funcs.filters import CustomFilters
import html
import urllib.request
import re
import json
import random
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from haruka import dispatcher
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler

def boobs(bot: Bot, update: Update):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    final = "http://media.oboobs.ru/{}".format(nsfw)
    update.message.reply_photo(final)

def khiladi(bot: Bot, update: Update):
    final1 = "https://telegra.ph/file/051227609674fc788d030.jpg"
    update.message.reply_photo(final1)

def avn(bot: Bot, update: Update):
    avengers = (
      "https://telegra.ph//file/8201c6a5363061b4f0196.jpg"
      "https://telegra.ph//file/8a525ec13114d1fa62e5d.jpg"
      "https://telegra.ph//file/ff0a5befc03599643be59.jpg"
    )
    avn1 = random.choice(avn1)
    update.message.reply_photo(avn)
		
BOOBS_HANDLER = DisableAbleCommandHandler("boobs", boobs, filters=CustomFilters.sudo_filter)
KHILADI_HANDLER = DisableAbleCommandHandler("khiladi", khiladi)
AVN_HANDLER = DisableAbleCommandHandler("avn", avn)

dispatcher.add_handler(AVN_HANDLER)
diapatcher.add_handler(BOOBS_HANDLER)
dispatcher.add_handler(KHILADI_HANDLER)
