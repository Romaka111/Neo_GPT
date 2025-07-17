import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = os.getenv("BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URL = os.getenv("MONGO_URL")
YOOMONEY_WALLET = os.getenv("YOOMONEY_WALLET")
YOOMONEY_SECRET_TOKEN = os.getenv("YOOMONEY_SECRET_TOKEN")
