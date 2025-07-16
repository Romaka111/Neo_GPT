# 🤖 NeoGPT — Телеграм-бот с поддержкой GPT-4o, изображений и подписок

NeoGPT — это мощный Telegram-бот с интеграцией OpenAI GPT-4o, поддержкой генерации изображений, системой подписок, Webhook и быстрой работой 24/7.

---

## 🚀 Возможности

- 📚 Многоуровневые подписки: Base, Student Pro, Smart+, Ultra
- 💬 Поддержка GPT-4o для Pro-пользователей
- 🧠 Память и история пользователей
- 🖼 Генерация изображений (ограничения по подписке)
- 💳 Автоматические оплаты через ЮMoney
- 🔗 Webhook (на Railway)
- 🔒 Безопасное использование переменных окружения

---

## 🔧 Переменные окружения

Создай `.env` файл или настрой переменные в Railway:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_key
MONGO_URL=your_mongodb_url
YOOMONEY_WALLET=your_yoomoney_wallet
YOOMONEY_SECRET=your_yoomoney_secret
BASE_URL=https://your-railway-app-name.up.railway.app
