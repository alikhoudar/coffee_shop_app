from dotenv import load_dotenv
import os

load_dotenv()

DB_FILENAME=os.environ.get("DB_FILENAME")
PROJECT_DIR=os.path.dirname(os.path.abspath(__file__))