"""Using wrapper functions from placeholder, perform CRUD tests for users"""

import json
import logging
import pytest
import requests

from actions import JsonPlaceholderActions as Jpa
from conftest import with_session


@pytest.mark.users
def test_get_all_users(with_session: requests.Session):
    logging.info(f"Test GET all users")
    response = Jpa.get_users(with_session)
    assert(response.status_code == 200)

