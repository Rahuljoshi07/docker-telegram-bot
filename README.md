# 🤖 Dockerized Telegram Bot

A simple Telegram bot built with [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) that runs completely inside a Docker container using Docker Compose.

This bot responds to basic commands like `/start`, `/help`, and `/info`, and is designed to help developers learn how to containerize small API-based Python services securely and efficiently. Perfect for DevOps learning!

---

## 📦 Features

- ✅ Responds to:
  - `/start` — Welcome message
  - `/help` — List available commands
  - `/info` — Info about bot and author
- ✅ Containerized with a `Dockerfile`
- ✅ Secrets managed via `.env` file (not hardcoded!)
- ✅ Lightweight, production-ready base image (`python:3.11-slim`)
- ✅ Run with just one command using Docker Compose

---

## 🧱 Project Structure

```
.
├── Dockerfile
├── bot.py
├── docker-compose.yml
├── .env              # Not committed – contains your BOT_TOKEN
└── requirements.txt
```

---

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rahuljoshi07/docker-telegram-bot.git
   cd docker-telegram-bot
   ```

2. **Create a `.env` file**
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Test your bot**
   Go to Telegram and send `/start` to your bot.

---

## 💡 Commands in Bot

| Command   | Description           |
|-----------|------------------------|
| `/start`  | Shows welcome message  |
| `/help`   | Lists all commands     |
| `/info`   | Shows bot + author info |

---

## 📸 Bot in Action

```
![Screenshot 2025-06-22 144626](https://github.com/user-attachments/assets/07d2ef50-855c-4a03-b197-6d1d9f4b5b67)

```

---

## 🔧 Future Improvements

- 🧠 Add more interactive commands
- 📊 Add webhook mode deployment option
- 💬 Enable inline query support
- 🚨 Add error handling and logging

---

## 📄 License

This project is created for learning purposes by Rahul Joshi. Feel free to explore and use the code.

---

👨‍💻 Made with ❤️ by Rahul Joshi  
🔗 [github.com/Rahuljoshi07](https://github.com/Rahuljoshi07)
