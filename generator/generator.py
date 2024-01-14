import random

from Data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(1000,20000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_Address=faker_ru.address(),
        permanent_Address=faker_ru.address(),
    )