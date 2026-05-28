from dotenv import load_dotenv
from os import getenv


load_dotenv()
TOKEN = getenv('TOKEN')
REDIS_PASSWORD = getenv('REDIS_PASSWORD')