import os
import environ
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])


# Database Details
PMS_DB_NAME = env.str('PMS_DB_NAME')
PMS_DB_USER = env.str('PMS_DB_USER')
PMS_DB_PASSWORD = env.str('PMS_DB_PASSWORD')
PMS_DB_HOST = env.str('PMS_DB_HOST')
PMS_DB_PORT = env.int('PMS_DB_PORT', default=5432)
