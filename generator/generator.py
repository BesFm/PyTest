import random
import time
from Data.data import Person, Date
from faker import Faker

faker_ru = Faker("ru_RU")
faker_en = Faker("En")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(1000, 20000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_Address=faker_ru.address(),
        permanent_Address=faker_ru.address(),
        mobile_number=random.randint(1000000000, 9999999999),
        birth_date=faker_ru.date().split("-"),
    )


def generated_file():
    path = rf"C:\Users\Bes.fm\Downloads\filetest{random.randint(0, 500)}.txt"
    file = open(path, "w+")
    file.write("Hello World")
    file.close()
    return file.name


def generated_subject():
    subject_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                    "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    sr = random.randint(0, len(subject_list) - 4)
    return subject_list[sr: sr + 3]


def generated_state():
    state_list = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
    state = random.choice(state_list)
    state_city_list = {"NCR": ["Delhi", "Gurgaon", "Noida"], "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
                       "Haryana": ["Karnal", "Panipat"], "Rajasthan": ["Jaipur", "Jaiselmer"]}
    return state, random.choice(state_city_list[state])


def generated_colors():
    yield random.sample(["Red", "Blue", "Green", "Yellow", "Purple", "Black",
                         "White", "Voilet", "Indigo", "Magenta", "Aqua"], 3)


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=time.strftime("%H:", time.localtime()) + str(random.randrange(0, 45, 15))
    )
