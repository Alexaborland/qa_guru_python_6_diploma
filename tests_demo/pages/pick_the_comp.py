from time import sleep

from selene import have, browser, be
from tests_demo import resourсe
from tests_demo.users.users import User


class PickTheComputer:

    def open(self):
        browser.open('/computers')

    def pick_desktop_computer(self):
        browser.all('[class="sub-category-item"]').element_by(have.exact_text('Desktops')).click()

    def sort_by_high_to_low_price(self):
        browser.element('[id="products-orderby"]').click()
        browser.element('[value="https://demowebshop.tricentis.com/desktops?orderby=11"]').click()


    def filter_by_price(self):
        browser.all('[class="PriceRange"]')[3].click()


    def pick_the_computer(self):
        browser.element('[class="price actual-price"]').should(have.tag('span'))
        browser.element('[class="button-2 product-box-add-to-cart-button"]').click()


    def pick_characteristics(self):
        browser.element('[id="product_attribute_74_5_26_82"]').click()
        browser.element('[id="product_attribute_74_6_27_85"]').click()
        browser.element('[id="product_attribute_74_3_28_87"]').click()
        browser.element('[id="product_attribute_74_8_29_89"]').click()
        browser.element('[id="add-to-cart-button-74"]').click()
        sleep(3)



    def check_the_cart(self):
        browser.element('[id="topcartlink"]').click()


