from selene import have, browser, be


class AddJewelryInWishlist:
    def open_jewelry(self):
        browser.open('/jewelry')

    def pick_jewelry(self):
        browser.all('.product-title').element_by(have.exact_text('Diamond Pave Earrings')).click()

    def add_in_wishlist(self):
        browser.element('[value="Add to compare list"]').click()

    def check_adding_in_wishlist(self):
        browser.element('.page-title').should(be.visible.and_(have.text('Compare products')))
        browser.element('.product-name').should(be.clickable.and_(have.text('Diamond Pave Earrings')))
