import os
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://invitationnation.in/"
APP_URL = "https://app.invitationnation.in/"

EMAIL = os.getenv("INVITATION_EMAIL")
PASSWORD = os.getenv("INVITATION_PASSWORD")