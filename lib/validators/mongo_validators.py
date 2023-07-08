from lib.utils.configs import Configs

def check_mongodb_parameters():
    # check if .env variables are defined
    # if Configs.DB_USERNAME is None:
    #     raise Exception("DB_USERNAME is not defined!")
    # if Configs.DB_PASSWORD is None:
    #     raise Exception("DB_PASSWORD is not defined!")
    if Configs.DB_CONNECTION_STRING is None:
        raise Exception("DB_CONNECTION_STRING is not defined!")
    if Configs.DB_NAME is None:
        raise Exception("DB_NAME is not defined!")
    if Configs.DB_COLLECTION_NAME is None:
        raise Exception("DB_COLLECTION_NAME is not defined!")

    return True