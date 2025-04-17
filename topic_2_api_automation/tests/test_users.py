"""Using wrapper functions from placeholder, perform CRUD tests for users"""

from utils.logger import log
import pytest
import requests
from actions.user_actions import UserActions

user_api = UserActions()

class TestUsers:

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_get_all_users(self, with_session: requests.Session):
        """
        Test GET /users returns status_code 200
        :param with_session: fixture that provides a persistent requests.Session
        :return:
        """
        log.info(f"Test GET all users")
        response = user_api.get_users(with_session)
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_get_user_by_id(self, with_session: requests.Session):
        """
        Test GET /users/1 returns status_code 200
        :param with_session: fixture that provides a persistent requests.Session
        :return:
        """
        log.info(f"Test GET user by id")
        response = user_api.get_user_by_id(with_session, 1)
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.sad_path
    def test_get_unknown_user(self, with_session: requests.Session):
        """
        Test unknown user with id 42 at /users/42 returns 404 gracefully
        :param with_session: fixture that provides a persistent requests.Session
        :return:
        """
        log.info(f"Test GET unknown user id 42 fails gracefully")
        response = user_api.get_user_by_id(with_session, 42)
        assert(response.status_code == 404)

    @pytest.mark.users
    @pytest.mark.happy_path
    def test_create_user(self, with_session: requests.Session, random_user: dict):
        """
        Test POST /users with a JSON dict payload returns status_code 201
        :param with_session: fixture that provides a persistent requests.Session
        :param random_user: fixture which provides a valid random values for a new user
        :return:
        """
        log.info(f"Test create user")
        response = user_api.create_user(with_session, random_user)
        assert(response.status_code == 201)

        # Delete user to go back to good state
        response = user_api.delete_user(with_session, response.json()['id'])
        assert(response.status_code == 200)

    @pytest.mark.users
    @pytest.mark.happy_path
    @pytest.mark.integration
    @pytest.mark.skip  # skipping because slow
    def test_create_100_users(self, with_session: requests.Session, random_user: dict):
        """
        Longer running test for DB performance
        :param with_session: fixture that provides a persistent requests.Session
        :param random_user: fixture which provides a valid random values for a new user
        :return:
        """
        log.info(f"Test create 100 users")
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
    @pytest.mark.e2e
    def test_crud_user(self, with_session: requests.Session, random_user: dict):
        """
        E2E test to create, update, and delete a user
        :param with_session: fixture that provides a persistent requests.Session
        :param random_user: fixture which provides a valid random values for a new user
        :return:
        """
        log.info(f"Test CRUD user")
        response = user_api.create_user(with_session, random_user)
        assert(response.status_code == 201)
        new_user_id = response.json()['id']

        log.info(f"updating user {random_user['name']} name to Zaphod")
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
        """
        Test to attempt to delete a non-existent user fails gracefully with status_code 404
        :param with_session: fixture that provides a persistent requests.Session
        :param random_user: fixture which provides a valid random values for a new user
        :return:
        """
        log.info(f"Test delete unknown user")
        response = user_api.delete_user(with_session, 42)
        log.info(f"delete unknown user 42 status_code[{response.status_code}]")
        assert(response.status_code == 404)
