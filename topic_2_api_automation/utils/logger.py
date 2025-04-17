import logging
import os
from datetime import datetime

# Create directory for logs (if it does not yet exist)
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# strftime pattern for datetime stamp
datetime_stamp = "%Y-%m-%d_%H-%M-%S"

# Create new log file per run with datestamp
log_file = os.path.join(log_dir, f"ana_test_log_{datetime.now().strftime(datetime_stamp)}.log")


# Formatter
formatter = logging.Formatter("{asctime} - {levelname}: {message}", datefmt=datetime_stamp, style="{")

# Custom logger
logger = logging.getLogger("anaApiTestLogger")
logger.setLevel(logging.DEBUG)

# Avoid duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

logger.info("Logger initialized")