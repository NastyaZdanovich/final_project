import allure
from source_code.pages.catalog_page import CatalogPage
from source_code.pages.item_page import ItemPage
from source_code.pages.my_oz_page import MyOZPage


class TestAddingTo:
    def test_adding_to_wish_list(self, driver, main_page, sign_in):
        with allure.step("1. Выбрать категорию товаров и перейти на страницу каталога"):

            main_page.choose_a_category()

        with allure.step("2. Открыть страницу товара"):
            catalog_page = CatalogPage(driver)
            catalog_page.choose_an_item()

        with allure.step("3. Определить название товара и добавить его в избранное"):
            item_page = ItemPage(driver)
            item_name = item_page.get_a_text(item_page.item_name_xpath)
            item_page.click_by_xpath(item_page.go_to_favorite_xpath)

        with allure.step("4. Перейти в 'Избранное' и проверить, какой товар был добавлен"):
            item_page.click_by_xpath(item_page.favorites_xpath)
            my_oz_page = MyOZPage(driver)
            item_in_faves = my_oz_page.get_a_text(my_oz_page.name_of_an_item_xpath)
            assert item_name == item_in_faves, f'Expected name {item_name}, actual name {item_in_faves}'

        with allure.step("5. Удалить товар из избранного и проверить,что wish-list пустой"):
            my_oz_page.click_by_xpath(my_oz_page.delete_fave_item_xpath)
            my_oz_page.refresh_page()
            text = my_oz_page.get_a_text(my_oz_page.check_wish_list_xpath)
            assert 'нет товаров.' in text, f"Expected text 'В «Избранном» пока нет товаров.', actual text {text}"

    def test_adding_to_wait_list(self, driver, main_page, sign_in):
        with allure.step("1. Выбрать категорию товаров и перейти на страницу каталога"):

            category = main_page.get_random_element_by_xpath(main_page.out_of_stock_catalog_xpath)
            main_page.click_by_xpath(category)

        with allure.step("2. Отобразить товары,которых нет в наличии"):
            catalog_page = CatalogPage(driver)
            catalog_page.wait_list_items()

        with allure.step("3. Открыть страницу товара"):
            catalog_page.choose_an_item()

        with allure.step("4. Определить название товара и переместить в wait-list, нажав на кнопку 'Оставить заявку'"):
            item_page = ItemPage(driver)
            item_name = item_page.get_a_text(item_page.item_name_xpath)
            item_page.click_by_xpath(item_page.wait_list_xpath)

        with allure.step("5. Перейти в личный кабинет и определить название товара,который был добавлен в wait-list"):
            item_page.click_by_xpath(catalog_page.my_oz_xpath)
            my_oz_page = MyOZPage(driver)
            my_oz_page.click_by_xpath(my_oz_page.wait_list_xpath)
            wait_list_item = my_oz_page.get_a_text(my_oz_page.wait_list_item_xpath)

        with allure.step("6. Проверить, какой товар был добавлен в wait-list"):
            assert item_name in wait_list_item, f'Expected item name {item_name}, actual item name {wait_list_item}'

        with allure.step("7. Удалить товар из wish-list"):
            my_oz_page.click_by_xpath(my_oz_page.delete_wait_list_item)
            my_oz_page.accept_alert()
            text = my_oz_page.get_a_text(my_oz_page.check_wait_list_xpath)
            assert text == 'У вас нет подписок.', f"Expected text 'У вас нет подписок, actual text {text}' "
