import os


class DevConfig:
    ENV_NAME = "dev"
    DEBUG = True
    TESTING = False


class StagingConfig:
    ENV_NAME = "staging"
    DEBUG = False
    TESTING = True


class ProdConfig:
    ENV_NAME = "production"
    DEBUG = False
    TESTING = False


def get_config():
    env = os.getenv("APP_ENV", "dev")
    configs = {
        "dev": DevConfig,
        "staging": StagingConfig,
        "production": ProdConfig,
    }
    return configs.get(env, DevConfig)
