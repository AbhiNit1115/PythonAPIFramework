from jproperties import Properties
from requests_api_pytest.tests.test_utility.constants import ConfConst
from requests_api_pytest.tests.test_utility.constants import LogConst


class PropertyFileReader:
    environment_prop = Properties()

    ENVIRONMENT_PROP_PATH = ConfConst.ENVIRONMENT_PROP_PATH
    ENVIRONMENT_LOG_PATH = LogConst.ENVIRONMENT_LOG_PATH

    @classmethod
    def env_property_loader(cls):
        with open(cls.ENVIRONMENT_PROP_PATH, 'rb') as env_file:
            cls.environment_prop.load(env_file)

    @classmethod
    def log_loader(cls):
        with open(cls.ENVIRONMENT_LOG_PATH, 'rb') as log_file:
            cls.environment_prop.load(log_file)

    @classmethod
    def all_property_loader(cls):
        cls.env_property_loader()
        cls.log_loader()

