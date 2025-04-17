"""Using wrapper functions from placeholder, perform CRUD tests for users"""

import logging
import pytest
import requests
from actions.user_actions import UserActions

user_api = UserActions()

class TestUsers:

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_get_all_users(self, with_session: requests.Session):
        logging.info(f"Test GET all users")
        response = user_api.get_users(with_session)
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_get_user_by_id(self, with_session: requests.Session):
        logging.info(f"Test GET user by id")
        response = user_api.get_user_by_id(with_session, 1)
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.sad_path
    def test_get_unknown_user(self, with_session: requests.Session):
        logging.info(f"Test GET unknown user id 42 fails gracefully")
        response = user_api.get_user_by_id(with_session, 42)
        assert(response.status_code == 404)

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_create_user(self, with_session: requests.Session, random_user: dict):
        logging.info(f"Test create user")
        response = user_api.create_user(with_session, random_user)
        assert(response.status_code == 201)

        # Delete user to go back to good state
        response = user_api.delete_user(with_session, response.json()['id'])
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.happy_path
    @pytest.mark.skip  # skipping because slow
    def test_create_100_users(self, with_session: requests.Session, random_user: dict):
        logging.info(f"Test create 100 users")
        user_ids = []
        for i in range(100):
            response = user_api.create_user(with_session, random_user, verbose=False)
            user_ids.append(response.json()['id'])
            assert(response.status_code == 201)

        # Delete users to go back to good state
        for j in range(len(user_ids)):
            response = user_api.delete_user(with_session, user_ids.pop())
            assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_crud_user(self, with_session: requests.Session, random_user: dict):
        logging.info(f"Test CRUD user")
        response = user_api.create_user(with_session, random_user)
        assert(response.status_code == 201)
        new_user_id = response.json()['id']

        logging.info(f"updating user {random_user['name']} name to Zaphod")
        response = user_api.update_user(with_session, {'id': new_user_id, 'name': "Zaphod"})
        assert(response.status_code == 200)
        assert(response.json()['name'] == "Zaphod")

        # Delete user to go back to starting state
        response = user_api.delete_user(with_session, new_user_id)
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.sad_path
    @pytest.mark.skip  # Found a bug! File a JIRA and follow up
    def test_delete_unknown_user(self, with_session: requests.Session, random_user: dict):
        logging.info(f"Test delete unknown user")
        response = user_api.delete_user(with_session, 42)
        logging.info(f"delete unknown user 42 status_code[{response.status_code}]")
        assert(response.status_code == 404)
