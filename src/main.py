from dotenv import load_dotenv
import os

load_dotenv()

print("This comes from env: ", os.getenv('MY_API_KEY'))

