import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

from config import Config
from pyrogram import Client

class AutoCaptionBot(Client):
    def __init__(self):
        super().__init__(
            name="Captioner",
            bot_token="6650529779:AAGYioPMLCR1ZPTq93DTSP_iTGDC7mATgpU",
            api_id="16536417",
            api_hash="f6e58a549da642d7b765744a2f82c6d9",
            workers=20,
            plugins=dict(root="Plugins"),
        )
        
        # Enable additional logging for Pyrogram
        self.log_verbosity = logging.INFO

    def run(self):
        try:
            logger.info("Bot is starting...")
            super().run()
            logger.info("Bot is up and running.")
        except Exception as e:
            logger.error(f"An error occurred during bot execution: {e}")
        finally:
            logger.info("Bot is shutting down.")

if __name__ == "__main__":
    AutoCaptionBot().run()
