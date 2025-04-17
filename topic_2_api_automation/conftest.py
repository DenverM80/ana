#Fixtures related to session level setup, teardown, and persistent properties

from dataclasses import asdict
from faker import Faker # provides random data
from models.models import User, Address, Company, Coordinates
import pytest
import requests

fake = Faker()

@pytest.fixture(scope="session")
def with_session() -> requests.Session:
    """Provide a fixture with a persistent requests.Session"""
    return requests.Session()

@pytest.fixture()
def random_user() -> dict:
    """Provide a random user as a dataclass"""
    coords = Coordinates(lat=str(fake.latitude()), lng=str(fake.longitude()))
    addr = Address(
        street=fake.street_address(),
        suite=fake.building_number(),
        city=fake.city(),
        zipcode=fake.zipcode(),
        geo=coords
    )
    co = Company(
            name=fake.company(),
            catch_phrase=fake.catch_phrase(),
            bs=fake.sentence()
        )
    rando = User(
        name=fake.name(),
        username=fake.user_name(),
        email=fake.email(),
        address=addr,
        phone=fake.phone_number(),
        website=fake.uri_page(),
        company=co
    )
    return asdict(rando)