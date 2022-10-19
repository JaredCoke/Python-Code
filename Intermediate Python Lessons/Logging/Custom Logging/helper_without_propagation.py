"""
Custom Logging: callable logging across different modules
"""

### [Custom Logger] w/o propagation
import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('Hello from helper w/o propagation module')
print('no propagation')