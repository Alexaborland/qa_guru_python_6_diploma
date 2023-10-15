from selene import have, browser, be
from selenium.webdriver import Keys
from tests_demo.users.values import view_as_list
from tests_demo.users.values import chain_thickness
from tests_demo.users.values import pendant
from tests_demo.users.values import chain_length


class CreateJewelry:
    def open_jewelry(self):
        browser.open('/jewelry')

    def create_new(self):
        browser.element('#products-viewmode').click()
        browser.element(view_as_list).click()
        browser.all('.product-title').element_by(have.exact_text('Create Your Own Jewelry')).click()
        browser.element(chain_thickness).click().press(Keys.DOWN).press_enter()
        browser.element(chain_length).type('15')
        browser.element(pendant).click()

    def add_to_cart(self):
        browser.element('#add-to-cart-button-71').click()

    def check_adding_to_cart(self):
        browser.element('#bar-notification').should(be.visible.and_(have.text('The product has been added to your ')))


