import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
        The variable "update.message.text" contains the text content that the user sent.
        This can be passed into OpenAI's API, for example, to generate a response
    '''


    # Send back the same text that was sent by the user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    load_dotenv()
    application = ApplicationBuilder().token(os.environ['TELEGRAM_BOT_KEY']).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()