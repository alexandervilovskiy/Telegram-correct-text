# Telegram-correct-text

Этот бот для Telegram помогает исправлять грамматические ошибки в текстах на русском языке с использованием библиотеки language_tool_python.

## 📜 Описание

Бот принимает текстовые сообщения от пользователей и возвращает исправленный текст, используя инструменты проверки языка. Просто отправьте боту текст, и он предоставит вам исправления.

## 🚀 Установка

### Шаги по установке:

1. **Клонируйте репозиторий:**

   bash
   git clone https://github.com/gomoseky/Telegram-correct-text.git
   cd Telegram-correct-text
   
2. **Создайте виртуальное окружение (рекомендуется):**

   bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac,
   Для Windows: venv\Scripts\activate
   
3. **Установите необходимые библиотеки:**

   bash
   pip install pyTelegramBotAPI language-tool-python
   
4. **Получите API токен для вашего Telegram бота:**
   - Найдите [BotFather](https://t.me/botfather) в Telegram.
   - Создайте нового бота и получите токен.

5. **Настройте токен:**
   - Замените строку API_TOKEN = "Твой токен бота" в коде на ваш токен.

## 🛠️ Запуск

Запустите бота с помощью следующей команды:

bash
python main.py

## 📩 Использование

1. Найдите вашего бота в Telegram.
2. Нажмите "Старт" или отправьте команду /start.
3. Отправьте текст, который вы хотите исправить.
4. Получите исправленный текст в ответ.


## 🤝 Контрибьюция

Если вы хотите внести изменения или улучшения, пожалуйста, создайте pull request или откройте issue.

## 📞 Связь

Если у вас есть вопросы, не стесняйтесь обращаться через Telegram - @alexandervilovskiy
