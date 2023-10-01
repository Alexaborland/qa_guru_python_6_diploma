from selene import have, browser, be



class AddBookToCard:

    def open_book_section(self):
        browser.open('/books')

    def pick_the_book(self):
        browser.all('[class="product-title"]').element_by(have.exact_text('Computing and Internet')).click()


    def add_book_to_cart(self):
        browser.element('[id="addtocart_13_EnteredQuantity"]').click().clear().type('3')
        browser.element('[id="add-to-cart-button-13"]').click()

    def check_the_cart(self):
        browser.element('[class="cart-label"]').click()