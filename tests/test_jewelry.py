from time import sleep

from tests_demo.pages.create_jewelry import CreateJewelry


def test_with_high_level_registration_page():
    create_jewelry = CreateJewelry()

    create_jewelry.open_jewelry()
    create_jewelry.create_new()

    sleep(5)
