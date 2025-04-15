"""Fixtures related to session level setup, teardown, and persistent properties"""

import logging
import pytest
import requests

"""logging.basicConfig can only be called once, so put it in a session level fixture
   Default to DEBUG level for verbose"""
@pytest.fixture(scope="session")
def configure_logging():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
            filename="ana.log",
            encoding="utf-8",
            filemode="w",
            format="{asctime} - {levelname}: {message}",
            level=logging.DEBUG,
            datefmt="%Y-%m-%d %H:%M:%S")
    logger.info("Configured Logging.")

"""Provide a fixture with a persistent requests.Session"""
@pytest.fixture(scope="session")
def with_session() -> requests.Session:
    return requests.Session()