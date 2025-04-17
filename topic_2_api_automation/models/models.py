from dataclasses import dataclass

@dataclass
class Coordinates:
    """subproperty of an Address"""
    lat: str
    lng: str

@dataclass
class Company:
    """subproperty of a User"""
    name: str
    catch_phrase: str
    bs: str

@dataclass
class Address:
    """subproperty of a User"""
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Coordinates

@dataclass
class User:
    """dataclass with properties for a user"""
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

# Add more dataclasses below for posts, comments, albums etc