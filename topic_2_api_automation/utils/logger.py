import logging
import os
from datetime import datetime

"""
Util to initialize the logger
"""

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
log = logging.getLogger("anaApiTestLogger")
log.setLevel(logging.DEBUG)

# Avoid duplicate handlers
if not log.handlers:
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(stream_handler)

log.info("Logger initialized")