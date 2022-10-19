"""
Logging:
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
### Log Handler: Handler objects are responsible for dispatching appropiate log messages to the handlers specific destination
# i.e. use different handlers to send log messages to the standard output stream to files via HTTP or via email

### [Log Handler]
import logging

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler() # handler class which writes (formatted) logging records to a stream | console
file_h = logging.FileHandler('file.log') # handler class which writes formatted logging records to disk files | local files; creates a file if it doesn't exist

# define the level and the format for each handler
stream_h.setLevel(logging.WARNING) # sets logging level of the specified handler
file_h.setLevel(logging.ERROR) #we're choosing to only log & write 'ERROR' messages to a file

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s') # specifying the format
stream_h.setFormatter(formatter) # defines stream | console format
file_h.setFormatter(formatter) # defines log file format

logger.addHandler(stream_h) # add our handler to the logger
logger.addHandler(file_h) # add our handler to the file log

logger.warning('This is a warning.')
logger.error('This is an error.')

### Other Configuration methods