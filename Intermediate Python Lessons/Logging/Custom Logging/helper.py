"""
Custom Logging: callable logging across different modules
"""

### [Custom Logger] w/ propagation
import logging
logger = logging.getLogger(__name__)
logger.info('Hello from helper module')