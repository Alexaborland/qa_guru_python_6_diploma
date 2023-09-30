from time import sleep

from tests_demo.users import users
from tests_demo.pages.registration import Registration


def test_with_high_level_registration_page():
    user = users.new_user
    registration = Registration()

    # Регистрация
    registration.open_registration_page()
    registration.registration_new_user(user)
    registration.submit_registration()
    sleep(10)

    #registration_page.registration(user)
    #registration_page.submit_registration(user)