from selene import have, browser, be
from selenium.webdriver import Keys


class CreateJewelry:
    def open_jewelry(self):
        browser.open('/jewelry')


    def create_new(self):
        browser.element('[id="products-viewmode"]').click()
        browser.element('[value="https://demowebshop.tricentis.com/jewelry?viewmode=list"]').click()
        browser.all('[class="product-title"]').element_by(have.exact_text('Create Your Own Jewelry')).click()
        browser.element('[id="product_attribute_71_9_15"]').click().press(Keys.DOWN).press_enter()


