from time import sleep
from selene import have, browser, be
from tests_demo.users.values import high_to_low_price, processor_fast, ram_8_gb, hdd_400, software


class PickTheComputer:

    def open_computer_section(self):
        browser.open('/computers')

    def pick_desktop_computer(self):
        browser.all('.sub-category-item').element_by(have.exact_text('Desktops')).click()

    def sort_by_high_to_low_price(self):
        browser.element('#products-orderby').click()
        browser.element(high_to_low_price).click()


    def filter_by_price(self):
        browser.all('.PriceRange')[3].click()


    def pick_the_computer(self):
        browser.all('.product-title').element_by(have.text('Build your own expensive computer')).click()


    def pick_characteristics(self):
        browser.element(processor_fast).click()
        browser.element(ram_8_gb).click()
        browser.element(hdd_400).click()
        browser.element(software).click()

    def add_to_cart(self):
        browser.element('#add-to-cart-button-74').click()
        sleep(2)

    def check_adding_to_cart(self):
        browser.element('#bar-notification').should(be.visible.and_(have.text('The product has been added to your ')))

    def click_the_shopping_cart(self):
        browser.element('.ico-cart').click()

    def checking(self):
        browser.element('#CountryId').click().type("ger").press_enter()
        browser.element('#StateProvinceId').should(have.text('Other (Non US)'))
        browser.element('#ZipPostalCode').type('123456')
        browser.element('.inputs').click()
        browser.element('#termsofservice').click()
        browser.element('#checkout').click()

    def transition_to_login_page(self):
        browser.element('.page-title').should(have.text('Welcome, Please Sign In!'))


