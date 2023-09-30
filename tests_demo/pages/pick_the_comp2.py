from selene import have, browser, be
from tests_demo import resourсe
from tests_demo.users.users import User


class Registration:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.sex = browser.all('.custom-radio')
        self.mobile_number = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.hobbies = browser.all('#hobbiesWrapper label')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.submit_button = browser.element('#submit')

    def open_registration_page(self):
        browser.open('/register')

    def pick_desktop_computer(self):
        browser.all('[class="sub-category-item"]').element_by(have.exact_text('Desktops')).click()

    def sort_by_high_to_low_price(self):
        browser.element('[id="products-orderby"]').click()

    # browser.all('[id="products-orderby"]').element_by(have.text('Price: High to Low')).press_enter()
    # вспомнить как зафроузить список. сейчас он открывается, но не выбирается элемент

    def filter_by_price(self):
        browser.all('[class="PriceRange"]').element_by(have.exact_text('1200')).click()

    # понять как отфильтровать по цене

    def pick_the_most_expensive_computer(self):
        # создать переменную для цены компа и сравнить с ценой общей(по фильтру), что она больше или равна 1200
        browser.element('[class="prices"]').should(have.value())



    def registration(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.sex.element_by(have.text(user.sex)).click()
        self.mobile_number.type(user.mobile_number)
        self.fill_a_date_of_birth(user)
        self.subject.click().type(user.subject).press_enter()
        self.hobbies.element_by(have.text(user.hobbies)).click()
        self.picture.send_keys(resourсe.path(user.picture))
        self.address.type(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_button.should(be.visible).click()

    def fill_a_date_of_birth(self, user):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().type(user.date_of_birth.strftime('%B')).press_enter()
        browser.element('.react-datepicker__year-select').click().type(user.date_of_birth.year).click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.strftime("%d")}').click()

    def fill_state(self, value):
        browser.element('#state').click()
        browser.element('#react-select-3-input').should(be.blank).type(value).press_enter()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()

    def submit_registration(self, user: User):
        browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
        browser.element('[class="modal-body"]').should(have.text(f'Student Name {user.first_name} {user.last_name}'))
        browser.element('[class="modal-body"]').should(have.text(f'Student Email {user.email}'))
        browser.element('[class="modal-body"]').should(have.text(f'Gender {user.sex}'))
        browser.element('[class="modal-body"]').should(have.text(f'Mobile {user.mobile_number}'))
        browser.element('[class="modal-body"]').should(have.text('Date of Birth {0} {1},{2}'.format(
            user.date_of_birth.strftime("%d"), user.date_of_birth.strftime("%B"), user.date_of_birth.strftime("%Y"))))
        browser.element('[class="modal-body"]').should(have.text(f'Subjects {user.subject}'))
        browser.element('[class="modal-body"]').should(have.text(f'Hobbies {user.hobbies}'))
        browser.element('[class="modal-body"]').should(have.text(f'Picture {user.picture}'))
        browser.element('[class="modal-body"]').should(have.text(f'Address {user.address}'))
        browser.element('[class="modal-body"]').should(have.text(f'State and City {user.state} {user.city}'))
