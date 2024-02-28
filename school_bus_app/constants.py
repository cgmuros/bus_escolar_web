from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv() 

base_url_backend = os.getenv("BASE_URL_BACKEND")



class Constants(Enum):
    ENDPOINT_AUTH = f"{base_url_backend}/auth"
    ENDPOINT_CITY = f"{base_url_backend}/city"
    ENDPOINT_COUNTRY = f"{base_url_backend}/country"
    ENDPOINT_REGION = f"{base_url_backend}/region"
    ENDPOINT_STUDENT = f"{base_url_backend}/student"
    ENDPOINT_USER = f"{base_url_backend}/user"