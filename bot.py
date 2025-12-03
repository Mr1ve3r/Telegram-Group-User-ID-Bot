import logging
import os
import sys

from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatType
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply with the user or group ID depending on the chat type."""
    chat = update.effective_chat
    user = update.effective_user

    if not chat:
        logger.warning("update without chat: %s", update)
        return

    if chat.type == ChatType.PRIVATE:
        if user:
            await update.message.reply_text(
                f"Ваш Telegram ID: {user.id}"
            )
        else:
            await update.message.reply_text(
                "Не удалось определить ваш Telegram ID."
            )
        return

    if chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        await update.message.reply_text(
            f"ID этой группы: {chat.id}"
        )
        return

    await update.message.reply_text("Команда поддерживается только в чатах и группах.")


def main() -> None:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN is not set. Create a .env file with BOT_TOKEN=<token>")
        sys.exit(1)

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    logger.info("Bot started. Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == "__main__":
    main()
