from os import environ
from dotenv import load_dotenv

load_dotenv(".env")

GUID = "00000000-0000-0000-0000-000000000000"
PHONE = "+7-777-777-77-77"

DB_URL = environ.get("DB_URL")
JWT_KEY = environ.get("JWT_KEY")
JWT_ALGORITHM = environ.get("JWT_ALGORITHM")
API_TOKEN = environ.get("API_TOKEN")
URL_1C = environ.get("URL_1C")

AUTHORIZATION = environ.get("AUTHORIZATION")
REPRESENTATIVE = environ.get("REPRESENTATIVE")
BUYER = environ.get("BUYER")
DATE = "0001.01.01"
DATE_TWO = "01-01-0001"
DATE_THREE = "01010001"
BINARY_IMAGE =  "base64"
PATH_IMAGE = "./templates/"


REP = {
    "text": "hello world"
}