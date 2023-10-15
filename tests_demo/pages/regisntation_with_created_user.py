from selene import have, browser, be
from tests_demo.users.users import User


class RegistrationWithRepeatedData:

    def __init__(self):
        self.gender = browser.all('[class="gender"]')
        self.first_name = browser.element('[id="FirstName"]')
        self.last_name = browser.element('[id="LastName"]')
        self.email = browser.element('[id="Email"]')
        self.password = browser.element('[id="Password"]')
        self.confirm_password = browser.element('[id="ConfirmPassword"]')
        self.submit_button = browser.element('[id="register-button"]')

    def open_registration_page(self):
        browser.open('/register')

    def registration_new_user(self, user: User):
        self.gender.element_by(have.text(user.gender)).click()
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.password.type(user.password)
        self.confirm_password.type(user.confirm_password)
        self.submit_button.should(be.visible).click()

    def submit_registration(self):
        browser.element('.message-error').should(have.text('The specified email already exists'))
