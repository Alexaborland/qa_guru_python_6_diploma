from time import sleep

from tests_demo.users import users
from tests_demo.pages.pick_the_comp import PickTheComputer
from tests_demo.pages.pick_the_comp2 import Registration


def test_with_high_level_registration_page():
    user = users.new_user
    pick_the_comp = PickTheComputer()

    # Выбираем комп
    pick_the_comp.open()
    pick_the_comp.pick_desktop_computer()
    pick_the_comp.sort_by_high_to_low_price()
    pick_the_comp.filter_by_price()
    sleep(10)

    #registration_page.registration(user)
    #registration_page.submit_registration(user)