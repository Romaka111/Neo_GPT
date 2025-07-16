import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URL = os.getenv("MONGO_URL")
BASE_URL = os.getenv("BASE_URL")
YOOMONEY_TOKEN = os.getenv("YOOMONEY_TOKEN", "")