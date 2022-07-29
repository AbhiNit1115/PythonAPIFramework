import logging

logger = logging.getLogger(__name__)

logger.warning("Warning Message:")
logger.info("Information: ")
logger.debug("Debug Information: ")
logger.error("Error Message: ")
logger.critical("Critical Error")


file_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_handler)
