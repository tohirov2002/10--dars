from dotenv import load_dotenv
import os
import logging

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logging.error("token olishda xatolik yuz berdi")