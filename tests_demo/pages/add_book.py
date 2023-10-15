from selene import have, browser, be
from tests_demo.users.values import quantity


class AddBookToCard:

    def open_books_section(self):
        browser.open('/books')

    def pick_the_book(self):
        browser.all('.product-title').element_by(have.exact_text('Computing and Internet')).click()

    def pick_n_count_books(self):
        browser.element(quantity).click().clear().type('3')

    def add_book_to_cart(self):
        browser.element('#add-to-cart-button-13').click()

    def check_adding_to_cart(self):
        browser.element('#bar-notification').should(be.visible.and_(have.text('The product has been added to your ')))
