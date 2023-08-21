import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv


BEGINNING_TEXT = "Sup fam, I'm David Goggins!" # The text that the bot sends to the user when the the user first adds the bot
GOGGINS_PROMPT = '''
### INSTRUCTION: You are David Goggins, a US Navy Seal turned motivational public speaker. You are conversing with someone who has hired you as a life coach. Respond as if you are David Goggins.
### INPUT: {user_input}
'''

async def get_openai_response(query: str) -> str:
    # feed query into chatgpt's API and get a response
    openai_response = "[Response from ChatGPT]"
    return openai_response

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=BEGINNING_TEXT)

async def process_user_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = GOGGINS_PROMPT.format(user_input=update.message.text)
    response = await get_openai_response(query=prompt) # get a response from ChatGPT by feeding in the user's input plus a prompt template
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    load_dotenv()
    application = ApplicationBuilder().token(os.environ['TELEGRAM_BOT_KEY']).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), process_user_input)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()

