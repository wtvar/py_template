import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the variables
secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')


