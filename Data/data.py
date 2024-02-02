from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_Address: str = None
    permanent_Address: str = None
    mobile_number: int = None
    birth_date: list = None
    subject: str = None


@dataclass
class Date:
    year: str = None
    month: str = None
    day: str = None
    time: str = None
