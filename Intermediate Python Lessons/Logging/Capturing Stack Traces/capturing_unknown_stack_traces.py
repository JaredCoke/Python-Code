"""
Logging:
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
# ### [Stack Tracing] Helpful for troubleshooting issues

# Catching an Unknown Error in a Try-Except Block w/ Stack Tracing Error
import logging
import traceback

try:
    a = [1,2,3]
    val = a[c]
except:
    logging.error("The error is %s",traceback.format_exc()) # returns what ever the error is as an error in the console

print("This message still executes after the Traceback error is shown, but is randomly shown before/after the Traceback error details. ")