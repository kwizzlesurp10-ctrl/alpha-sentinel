import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Alpha Sentinel System Instructions
SYSTEM_INSTRUCTIONS = """
You are the Alpha Sentinel. Your role is to monitor market volatility, 
detect sentiment anomalies, and provide actionable alerts.
Always be objective, concise, and prioritize latency.
"""

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Alpha Sentinel Initialized. Monitoring...")

if __name__ == '__main__':
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Alpha Sentinel Online.")
    application.run_polling()
