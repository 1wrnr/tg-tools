import os
from dotenv import load_dotenv
import pprint

load_dotenv()

# AUTH
TG_TOKEN = os.getenv("TG_TOKEN")
COINMARKETCAP_TOKEN = os.getenv("COINMARKETCAP_TOKEN")

# API ENDPOINTS
STABLE_API_URL = os.getenv("STABLE_API_URL")

class Env:
    TG_TOKEN = TG_TOKEN
    COINMARKETCAP_TOKEN = COINMARKETCAP_TOKEN
    STABLE_API_URL = STABLE_API_URL
