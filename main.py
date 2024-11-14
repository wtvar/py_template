import os
from dotenv import load_dotenv
from rich import print
from rich import traceback

# Load the .env file
load_dotenv()

# load the rich stuff
traceback.install()

# Access the variables
secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')


