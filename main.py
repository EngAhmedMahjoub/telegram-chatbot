from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes  

BOT_USERNAME: final = '@ttemprano_bot'

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am your friendly weather assistant Temprano! How can I help?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Select the location for weather")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")
    
#Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hello there'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    return 'I do not understand what you wrote'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot: ', response)
    await update.message.reply_text(response)