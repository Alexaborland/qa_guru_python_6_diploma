from time import sleep
import allure
from allure_commons.types import Severity
from tests_demo.pages.add_book import AddBookToCard
from tests_demo.pages.pick_the_comp import PickTheComputer
from tests_demo.pages.create_jewelry import CreateJewelry
from tests_demo.users import users
from tests_demo.pages.registration import Registration


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Register a new user")
@allure.link('https://demowebshop.tricentis.com/register', name='Testing')
def test_registration():
    user = users.new_user
    registration = Registration()

    with allure.step('Open the register section'):
        registration.open_registration_page()

    with allure.step('Register new user'):
        registration.registration_new_user(user)

    with allure.step('Submit registration'):
        registration.submit_registration()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Adding n-quantity of books to cart")
@allure.link('https://demowebshop.tricentis.com/books', name='Testing')
def test_add_book_to_cart():
    add_book = AddBookToCard()

    with allure.step('Open the book section'):
        add_book.open_books_section()

    with allure.step('Pick the book'):
        add_book.pick_the_book()

    with allure.step('Enter the number of books'):
        add_book.pick_n_count_books()

    with allure.step('Press "Add to Cart" button'):
        add_book.add_book_to_cart()

    sleep(2)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Adding created jewerly to cart")
@allure.link('https://demowebshop.tricentis.com/jewelry', name='Testing')
def test_pick_the_jewelry():
    create_jewelry = CreateJewelry()

    with allure.step('Open the jewelry section'):
        create_jewelry.open_jewelry()

    with allure.step('Create new jewelry'):
        create_jewelry.create_new()

    with allure.step('Add new jewelry to cart'):
        create_jewelry.add_to_cart()

    sleep(2)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Adding computer with characteristics to cart")
@allure.link('https://demowebshop.tricentis.com/computers', name='Testing')
def test_add_computer_to_cart():
    pick_the_comp = PickTheComputer()

    with allure.step('Open the computer section'):
        pick_the_comp.open_computer_section()

    with allure.step('Open the desktop computer section'):
        pick_the_comp.pick_desktop_computer()

    with allure.step('Sort by high to low price'):
        pick_the_comp.sort_by_high_to_low_price()

    with allure.step('Filter by price "Over 1200"'):
        pick_the_comp.filter_by_price()

    with allure.step('Pick the most expensive computer'):
        pick_the_comp.pick_the_computer()

    with allure.step('Pick computer`s characteristics'):
        pick_the_comp.pick_characteristics()

    with allure.step('Add computer to cart'):
        pick_the_comp.add_to_cart()

    with allure.step('Click the button "Shopping Cart"'):
        pick_the_comp.click_the_shopping_cart()

    with allure.step('Add information for shipping and checkout'):
        pick_the_comp.checking()





