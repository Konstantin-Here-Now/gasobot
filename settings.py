import os
from pathlib import Path

import yaml

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# virtual environment variables
TOKEN = os.getenv("TOKEN")

# Stages
FIRST_STATE, SECOND_STATE, THIRD_STATE = range(3)

# text variables
with open(os.path.join(BASE_DIR, r'config.yaml'), 'r', encoding="utf-8") as data_f:
    CONFIG = yaml.load(data_f, yaml.BaseLoader)

GREETINGS_TEXT = CONFIG["GREETINGS_TEXT"]
OPTIONS_FIRST_TEXT = CONFIG["OPTIONS_FIRST_TEXT"]
OPTIONS_FURTHER_TEXT = CONFIG["OPTIONS_FURTHER_TEXT"]
ABOUT_COMPANY_TEXT = CONFIG["ABOUT_COMPANY_TEXT"]
PRODUCTION_LEVEL_TEXT = CONFIG["PRODUCTION_LEVEL_TEXT"]
ORDERS_TEXT = CONFIG["ORDERS_TEXT"]
NOT_REALIZED_YET = CONFIG["NOT_REALIZED_YET"]
UNKNOWN_COMMAND = CONFIG["UNKNOWN_COMMAND"]
