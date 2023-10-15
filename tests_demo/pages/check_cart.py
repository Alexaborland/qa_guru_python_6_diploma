from selene import have, browser, be

class CheckCart:
    def click_the_shopping_cart(self):
        browser.element('.ico-cart').click()

    def checking(self):
        browser.element('.product-price order-total').should(not have.text('0'))
        browser.all('.country-input valid')[35].click()
        browser.all('.state-input valid').should(have.exact_text('Other (Non US)'))
        browser.element('#ZipPostalCode').type('123456')
        browser.element('.inputs').click()
        browser.element('#termsofservice').click()
        browser.element('#checkout').click()

    def transition_to_login_page(self):
        browser.element('.page-title').should(have.text('Welcome, Please Sign In!'))
