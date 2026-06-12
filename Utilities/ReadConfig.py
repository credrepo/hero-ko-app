import os
from configparser import ConfigParser

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Configuration", "config.ini")

config = ConfigParser()
config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_application_url():
        baseUrl = config.get("details","baseUrl")
        return baseUrl

    @staticmethod
    def get_browser():
        browser = config.get("details","browser")
        return browser