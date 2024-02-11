from APIs import  auth
from imports import token
from dotenv import load_dotenv
import os
load_dotenv()
def main():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")
    token_client = token(client_id, client_secret,redirect_uri)
    