from time import sleep

from tests_demo.pages.add_book import AddBookToCard


def test_with_high_level_registration_page():
    add_book = AddBookToCard()

    # Выбираем комп
    add_book.open_book_section()
    add_book.pick_the_book()
    add_book.add_book_to_cart()
    add_book.check_the_cart()
   # pick_the_comp.sort_by_high_to_low_price()
   # pick_the_comp.filter_by_price()
    sleep(10)

    #registration_page.registration(user)
    #registration_page.submit_registration(user)