import os
from dotenv import load_dotenv
load_dotenv()
consumer_key = os.getenv("consumer_key_p")
consumer_secret = os.getenv("consumer_secret_p")
access_token = os.getenv("access_token_p")
access_token_secret = os.getenv("access_token_secret_p")
