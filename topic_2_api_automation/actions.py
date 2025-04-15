"""This class wraps common actions for the {JSON}Placeholder API"""

import json
import logging
import requests

JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/"


class JsonPlaceholderActions:

    @staticmethod
    def get_users(client: requests.Session) -> requests.Response:
        logger = logging.getLogger(__name__)
        logger.info("Getting all users...")
        response = client.get(url=JSON_PLACEHOLDER_URL + "users")
        logger.debug(f"Received: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logging.warning(f"Non success response[{response.status_code}]")

        return response

    @staticmethod
    def get_user_by_id(client: requests.Session, user_id: int) -> requests.Response:
        logger = logging.getLogger(__name__)
        logger.info(f"Getting user {user_id}...")
        response = client.get(url=JSON_PLACEHOLDER_URL + f"user/{user_id}")
        logger.debug(f"Received: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            logging.warning(f"Non success response[{response.status_code}]")

        return response
