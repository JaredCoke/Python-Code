"""
Logging: simple messages; for advanced and complex messages - use JSON format!
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
### [Rotating] Rotating Timed File Handlers
# Useful if you have a large application w/ a lot of log messages, and you want to keep track of the most recent events - use a rotating file handler to keep the files small

# creates a rotating log based on how much time has passed.
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__) # define logger
logger.setLevel(logging.INFO) # define level

# roll over after s - seconds, m - minutes, h - hours, d - days, midnight, w0 - weekday 0 aka Monday, w1 - Tuesday
handler = TimedRotatingFileHandler("timed_test.log", when = 's', interval = 1, backupCount = 5) # define the name of the logs, when to roll over, and # of backups
logger.addHandler(handler)

for _ in range(6): # define the end of the file size
    logger.info("Hello, waffles!")
    time.sleep(5)