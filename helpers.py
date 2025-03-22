from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_email():
    return fake.free_email()


def create_random_password():
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def create_random_name():
    return fakeRU.first_name()