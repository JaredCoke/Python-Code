"""
Logging: simple messages; for advanced and complex messages - use JSON format!
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
### [] Rotating FIle Handlers
# Useful if you have a large application w/ a lot of log messages, and you want to keep track of the most recent events - use a rotating file handler to keep the files small

#
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__) # define logger
logger.setLevel(logging.INFO) # define level

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc
handler = RotatingFileHandler("app.log", maxBytes = 2000, backupCount = 5) # define the name of the logs, max file size, and # of backups
logger.addHandler(handler)

for _ in range(10000): # define the end of the file size
    logger.info("Hello, waffles!")