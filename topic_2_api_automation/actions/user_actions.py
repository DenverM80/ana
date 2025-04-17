"""This class wraps common user related actions for the {JSON}Placeholder API"""

import json
import requests

from conftest import with_session
from utils.logger import logger

JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"


class UserActions:

    def get_users(self, client: requests.Session) -> requests.Response:
        logger.info("Getting all users...")
        response = client.get(url=f"{JSON_PLACEHOLDER_URL}/users")
        logger.debug(f"Received in get_users: {json.dumps(response.json(), indent=2)}")
        logger.debug(f"{len(response.json())}")

        if not 200 <= response.status_code < 300:
            logger.warning(f"Non success response[{response.status_code}]")

        return response

    def get_user_by_id(self, client: requests.Session, user_id: int) -> requests.Response:
        logger.info(f"Getting user {user_id}...")
        response = client.get(url=f"{JSON_PLACEHOLDER_URL}/users/{user_id}")
        logger.debug(f"Received in get_user_by_id: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logger.warning(f"Non success response[{response.status_code}]")

        return response

    def create_user(self, client: requests.Session, user: dict, verbose: bool=True) -> requests.Response:
        logger.info(f"Creating user: {user['name']}...")
        logger.debug(f"{json.dumps(user, indent=2)}...")
        response = client.post(url=f"{JSON_PLACEHOLDER_URL}/users", json=user)
        logger.debug(f"Received in create_user: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logger.warning(f"Non success response[{response.status_code}]")

        return response

    def update_user(self, client: requests.Session, user: dict) -> requests.Response:
        logger.info(f"Updating user: {user['name']}...")
        logger.debug(f"{json.dumps(user, indent=2)}...")
        response = client.patch(url=f"{JSON_PLACEHOLDER_URL}/users/{user['id']}", json=user)
        logger.debug(f"Received in update_user: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logger.warning(f"Non success response[{response.status_code}]")

        return response

    def delete_user(self, client: requests.Session, user_id: int) -> requests.Response:
        logger.info(f"Deleting user: {user_id}...")
        response = client.delete(url=f"{JSON_PLACEHOLDER_URL}/users/{user_id}")
        logger.debug(f"Received status {response.status_code} in delete_user: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logger.warning(f"Non success response[{response.status_code}]")

        return response
