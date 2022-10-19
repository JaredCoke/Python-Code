"""
Logging:
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
### Log Handler w/ Config Files: Handler objects are responsible for dispatching appropiate log messages to the handlers specific destination
# i.e. use different handlers to send log messages to the standard output stream to files via HTTP or via email

### [Log Handler]
import logging
import logging.config

logging.config.fileConfig('logging.conf') # acquire config information
#alternatively you could use a dict config

# logger = logging.getLogger(__name__) #default format
logger = logging.getLogger("simpleExample") # creates a logger
logger.debug('This is a debug message.') #calls a message to return in the console

# create handler