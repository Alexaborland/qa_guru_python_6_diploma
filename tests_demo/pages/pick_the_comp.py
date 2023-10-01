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

    # browser.all('[id="products-orderby"]').element_by(have.text('Price: High to Low')).press_enter()
    # вспомнить как зафроузить список. сейчас он открывается, но не выбирается элемент

    def filter_by_price(self):
        browser.all('[class="PriceRange"]')

    # понять как отфильтровать по цене

    def pick_the_computer(self):
        browser.element('[class="price actual-price"]').should(have.tag('span'))
        browser.element('[class="button-2 product-box-add-to-cart-button"]').click()


    def pick_characteristics(self):
        browser.element('[id="product_attribute_72_5_18_65"]').click() #потом переделать на дорогой (82)
        browser.element('[id="product_attribute_72_6_19_91"]').click()
        browser.element('[id="product_attribute_72_3_20_58"]').click()
        browser.element('[id="product_attribute_72_8_30_95"]').click()
        browser.element('[id="add-to-cart-button-72"]').click()

    def check_the_cart(self):
        browser.element('[class="cart-label"]').click()


