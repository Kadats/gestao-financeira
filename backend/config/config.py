import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/gestao.db")
DEBUG = os.getenv("DEBUG", "False") == "True"
