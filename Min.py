from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging to track any errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetch bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Start command: It sends a welcome message when the bot is started
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your user bot. How can I assist you today?')

# Help command: It gives the user a list of available commands
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here are the commands you can use:\n/start - Start the bot\n/help - List commands')

# Echo function: It replies with the same text the user sends
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f"You said: {user_message}")

# Function to handle errors (if the bot encounters any issue)
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Main function to set up and run the bot
def main():
    # Create the Updater and pass your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Register message handler for text messages (echoes back the user message)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot and run it until the user interrupts
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
