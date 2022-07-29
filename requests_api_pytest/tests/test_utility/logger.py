import logging
import logging.config
from requests_api_pytest.tests.test_utility.constants import LogConst

DEFAULT_LOGGER_NAME = LogConst.DEFAULT_LOGGER_NAME


class LoggerFactory:

    @classmethod
    def get_conf_file_path(cls):
        return LogConst.ENVIRONMENT_LOG_PATH

    @classmethod
    def get_logger(cls, logger_name=DEFAULT_LOGGER_NAME):
        logging.config.fileConfig(fname=cls.get_conf_file_path())
        return logging.getLogger(logger_name)
