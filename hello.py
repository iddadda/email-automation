import os
from dotenv import load_dotenv

print('hello python')

sender_email = os.getenv('SECRET_ID')  # sender email
password = os.getenv('SECRET_PWD')  # sender email password
    
print(f"{sender_email}")
print(f"{password}")