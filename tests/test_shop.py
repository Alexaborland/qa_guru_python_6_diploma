from time import sleep
import allure
from allure_commons.types import Severity
from tests_demo.pages.add_book import AddBookToCard
from tests_demo.pages.pick_the_comp import PickTheComputer
from tests_demo.pages.create_jewelry import CreateJewelry
from tests_demo.pages.regisntation_with_created_user import RegistrationWithRepeatedData
from tests_demo.users import users
from tests_demo.pages.registration import Registration
from tests_demo.pages.add_jewelry_in_wishlist import AddJewelryInWishlist
from tests_demo.pages.subscribe_for_news import SubscribeForNews


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
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Register a user with already existed email")
@allure.link('https://demowebshop.tricentis.com/register', name='Testing')
def test_registration_with_repeated_email():
    user = users.new_user
    registration_with_repeated_email = RegistrationWithRepeatedData()

    with allure.step('Open the register section'):
        registration_with_repeated_email.open_registration_page()

    with allure.step('Register new user'):
        registration_with_repeated_email.registration_new_user(user)

    with allure.step('Failure of registration because of already existed email'):
        registration_with_repeated_email.submit_registration()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Subscribe for news with user email")
@allure.link('https://demowebshop.tricentis.com', name='Testing')
def test_subscribing_for_news():
    user = users.new_user
    subscribe_for_news = SubscribeForNews()

    with allure.step('Open the main page'):
        subscribe_for_news.open_main_page()

    with allure.step('Type the user`s email in the field'):
        subscribe_for_news.type_user_email(user)

    with allure.step('Click on the "subscribe" button'):
        subscribe_for_news.press_the_button_subscribe()

    with allure.step('Submit the subscribing'):
        subscribe_for_news.submit_subscribing()


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

    with allure.step('Check that book has been added to cart'):
        add_book.check_adding_to_cart()


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

    with allure.step('Check that created jewelry has been added to cart'):
        create_jewelry.check_adding_to_cart()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Alexandra Borland")
@allure.description("Adding jewelry in the wishlist")
@allure.link('https://demowebshop.tricentis.com/jewelry', name='Testing')
def test_add_jewelry_in_wishlist():
    add_jewelry_in_wishlist = AddJewelryInWishlist()

    with allure.step('Open the jewelry section'):
        add_jewelry_in_wishlist.open_jewelry()

    with allure.step('Pick the jewelry'):
        add_jewelry_in_wishlist.pick_jewelry()

    with allure.step('Add picked jewelry in the wishlist'):
        add_jewelry_in_wishlist.add_in_wishlist()

    with allure.step('Check that jewelry has been added in the wishlist'):
        add_jewelry_in_wishlist.check_adding_in_wishlist()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
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

    with allure.step('Check that computer has been added to cart'):
        pick_the_comp.check_adding_to_cart()

    with allure.step('Click the button "Shopping Cart"'):
        pick_the_comp.click_the_shopping_cart()

    with allure.step('Add information for shipping and checkout'):
        pick_the_comp.checking()

    with allure.step('If the user doesn`t log in, them go to the login page'):
        pick_the_comp.transition_to_login_page()





