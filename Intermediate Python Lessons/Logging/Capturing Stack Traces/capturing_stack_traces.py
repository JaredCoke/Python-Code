"""
Logging:
- log in different modules
- using different log handlers
- capture stack traces in your log
- using rotating file handler
"""
# ### [Stack Tracing] Helpful for troubleshooting issues

# Simple Try-Except Block w/ ERROR case
import logging

try:
    a = [1,2,3]
    val = a[4]
except IndexError as error_type:
    logging.error(error_type) # returns error as an error in the console


# Try-Except Block w/ Stack Tracing Error
import logging

try:
    a = [1,2,3]
    val = a[4]
except IndexError as error_type:
    logging.error(error_type, exc_info = True) # returns error as an error in the console AND the entire Traceback message

print("This message still executes after the Traceback error is shown, but is shown before the Traceback error details. ")