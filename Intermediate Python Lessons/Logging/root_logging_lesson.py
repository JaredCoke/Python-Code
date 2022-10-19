"""
Logging:
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
# ### [Root Logger] Logging to 5 different log levels; only levels warning or higher are printed by default

"""
maybe make this a new module?
"""

# import logging
# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.") # message printed by default
# logging.error("This is and error message.") # message printed by default
# logging.critical("This is a critical message.") # message printed by default
#
# print('')

### [Root Logger] Logging to 5 different log levels: specifying more log levels to print as well as time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.") # message printed by default
logging.error("This is an error message.") # message printed by default
logging.critical("This is a critical message.") # message printed by default