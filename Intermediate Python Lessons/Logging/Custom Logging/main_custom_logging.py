"""
Custom Logging: Logging across different modules
- log in different modules
"""

### [Custom Logger] ...
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S') # defines the format of the messsage to be called
import helper #calls log message from helper.py