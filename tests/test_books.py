from time import sleep

from tests_demo.pages.add_book import AddBookToCard


def test_with_high_level_registration_page():
    add_book = AddBookToCard()

    # Выбираем комп
    add_book.open_book_section()
    add_book.pick_the_book()
    add_book.add_book_to_cart()
    add_book.check_the_cart()
    sleep(10)
