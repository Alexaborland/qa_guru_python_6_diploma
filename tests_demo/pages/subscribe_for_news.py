from selene import have, browser, be
from tests_demo.users.users import User


class SubscribeForNews:

    def __init__(self):
        self.email = browser.element('[id="newsletter-email"')

    def open_main_page(self):
        browser.open('/')

    def type_user_email(self, user: User):
        self.email.type(user.email)

    def press_the_button_subscribe(self):
        browser.element('[value="Subscribe"]').click()

    def submit_subscribing(self):
        browser.element('.newsletter-result-block').should(have.text('Thank you for signing up!'))
