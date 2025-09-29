import os
import telebot as tb
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
MY_ID = os.getenv('MY_ID')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")

bot = tb.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Отправьте сообщение")

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice', 'sticker', 'location', 'contact'])
def handle_all_messages(message):
    user = message.from_user
    chat = message.chat
    
    user_info = f"""**Новое сообщение от:**
│  ├ ID: `{user.id}`
│  ├ Имя: {user.first_name or "Нет"}
│  ├ Фамилия: {user.last_name or "Нет"}
│  ├ Username: @{user.username or "Нет"}
│  ├ Язык: {user.language_code or "Нет"}
│  └ Бот: {user.is_bot}
├ Информация о чате:
│  ├ Тип чата: {chat.type}
│  ├ ID чата: `{chat.id}`
│  ├ Название: {chat.title or "Нет"}
│  ├ Username чата: @{chat.username or "Нет"}
│  └ Описание: {chat.description or "Нет"}
└ Тип контента: {message.content_type}"""
    
    bot.send_message(MY_ID, user_info, parse_mode='Markdown')
    bot.forward_message(MY_ID, message.chat.id, message.message_id)
    bot.reply_to(message, "Отправлено")

if __name__ == '__main__':

    bot.infinity_polling()
