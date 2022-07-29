import sys
import pytest
import logging
from pytest_reportportal import RPLogHandler, RPLogger
from requests_api_pytest.tests.test_utility.read_property_files import PropertyFileReader
from requests_api_pytest.common.api_request.requests_config import RestAPIConfig
from requests_api_pytest.tests.test_utility.logger import LoggerFactory

logger = LoggerFactory.get_logger("TEST")


@pytest.fixture(scope="session")
def url_configuration():
    logger.info("Loading properties file..")
    PropertyFileReader.all_property_loader()
    url_configuration = RestAPIConfig()
    logger.info("Setting up base configurations for the API ..")
    url_configuration.base_url = PropertyFileReader.environment_prop['api.base.uri'].data
    url_configuration.content_type = "application/json"
    return url_configuration


@pytest.fixture(scope="session")
def url_configuration2():
    PropertyFileReader.all_property_loader()
    url_configuration2 = RestAPIConfig()
    url_configuration2.base_url = PropertyFileReader.environment_prop['api.base.uri2'].data
    url_configuration2.content_type = "application/json"
    return url_configuration2


# @pytest.fixture(scope="session")
# def log_configuration():
#     PropertyFileReader.all_property_loader()
#     log_configuration = LogHandler()
#     return log_configuration


@pytest.fixture(scope="session")
def url_configuration3():
    PropertyFileReader.all_property_loader()
    url_configuration3 = RestAPIConfig()
    url_configuration3.base_url = PropertyFileReader.environment_prop['api.base.uri3'].data
    url_configuration3.content_type = "application/json"
    return url_configuration3


@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger
