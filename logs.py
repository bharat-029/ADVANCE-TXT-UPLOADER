# Don't Remove Credit Tg - @Bharat00029 
# Ask Doubt on telegram @Bharat00029 

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.ERROR,
    format=
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


logging = logging.getLogger()
