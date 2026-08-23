import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_DIR = os.path.join(os.path.dirname(BASE_DIR), "instance")


class BaseConfig:
    """
    Shared configuration used by all environments.
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-secret"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )


class DevelopmentConfig(BaseConfig):
    """
    Local development configuration.
    """

    DEBUG = True


class TestingConfig(BaseConfig):
    """
    Used during automated testing.
    """

    TESTING = True


class ProductionConfig(BaseConfig):
    """
    Production configuration.
    """

    DEBUG = False