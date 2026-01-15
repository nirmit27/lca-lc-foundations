"""
Settings and configuration
"""

import os
from datetime import datetime

import logging
from dotenv import load_dotenv

load_dotenv()

# Environment config.
try:
    PYSPARK_API_URL = os.getenv("PYSPARK_API_URL", "")

    if PYSPARK_API_URL == "":
        raise EnvironmentError("Missing PySpark API URL - Environment variable")
except EnvironmentError as env_err:
    print(f"\nERROR : {env_err}\n")
    exit(-1)

# Logging config.
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

logs_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s :::: %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(logs_dir, f"{timestamp}_client-app.log")),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("poc_app")
