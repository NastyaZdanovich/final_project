import allure
from source_code.pages.basket_page import BasketPage
from source_code.pages.catalog_page import CatalogPage
from source_code.pages.item_page import ItemPage


class TestBasket:
    def test_add_to_a_basket(self, driver, main_page, sign_in):
        with allure.step("1. Выбрать категорию товаров и перейти на страницу каталога"):
            main_page.choose_a_category()

        with allure.step("2. Выбрать товар и перейти на страницу товара"):
            catalog_page = CatalogPage(driver)
            catalog_page.choose_an_item()

        with allure.step("3. Определить название товара, добавить товар в корзину и перейти в корзину"):
            item_page = ItemPage(driver)
            item_name = item_page.get_a_text(item_page.item_name_xpath)
            item_page.click_by_xpath(item_page.add_to_basket_btn_xpath)
            item_page.click_by_xpath(item_page.go_to_basket_btn_xpath)

        with allure.step("4. Определить название товара в корзине и сравнить с названием товара, кот. д.б. добавлен "):
            basket_page = BasketPage(driver)
            item_name_in_bskt = basket_page.get_a_text(basket_page.item_in_a_basket_name_xpath)
            assert item_name == item_name_in_bskt, f'Expected item {item_name}, actual item {item_name_in_bskt}'

        with allure.step("5. Удалить товар из корзины"):
            basket_page.remove_item_from_cart()
            text = basket_page.get_a_text(basket_page.empty_cart_xpath)
            assert 'В корзине пусто' in text

    def test_fill_a_form(self, driver, main_page, sign_in):
        with allure.step("1. Выбрать категорию товаров и перейти на страницу каталога"):
            main_page.choose_a_category()

        with allure.step("2. Выбрать товар и перейти на страницу товара"):
            catalog_page = CatalogPage(driver)
            catalog_page.choose_an_item()

        with allure.step("3. Добавить товар в корзину и перейти в корзину"):
            item_page = ItemPage(driver)
            item_page.click_by_xpath(item_page.add_to_basket_btn_xpath)
            item_page.click_by_xpath(item_page.go_to_basket_btn_xpath)

        with allure.step("4. Выбрать город для доставки"):
            basket_page = BasketPage(driver)
            basket_page.get_a_town()

        with allure.step("5. Выбрать магазин для доставки"):
            address_xpath = basket_page.get_random_element_by_xpath(basket_page.chosen_address_xpath)
            address = basket_page.get_a_text(address_xpath)
            basket_page.click_by_xpath(address_xpath)

        with allure.step("6. Выбрать способ оплаты товара"):
            payment_method = basket_page.get_a_payment_method()
            basket_page.click_by_xpath(basket_page.continue_btn)

        with allure.step("7. Проверить заполненную форму"):
            assert_address = basket_page.get_a_text(basket_page.assert_address_xpath)
            assert assert_address == address, f"Expected text {assert_address}, actual text {address}"

            assert_payment = basket_page.get_a_text(basket_page.assert_payment_xpath)
            assert assert_payment == payment_method, f"Expected text {assert_payment}, actual text {payment_method}"

        with allure.step("8. Удалить товар из корзины"):
            basket_page.remove_item_from_cart()
            text = basket_page.get_a_text(basket_page.empty_cart_xpath)
            assert 'В корзине пусто' in text, f"Expected text 'В корзине пусто', actual text {text}"
