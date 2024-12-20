import pytest
import logging

from tests.loggers.log_handler import LogHandler

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create an instance of the LogHandler
log_handler = LogHandler()

# Add the log handler to the logger
logger.addHandler(log_handler)

# Test the logger
def test_logger():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")