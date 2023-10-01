from selene import have, browser, be

class CreateJewelry:
    def open_jewelry(self):
        browser.open('/jewelry')
