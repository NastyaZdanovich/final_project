import allure
import pytest

from fifth_element.source_code.constants import Host
from fifth_element.source_code.pages.basket_page import BasketPage
from fifth_element.source_code.pages.main_page import MainPage
from fifth_element.source_code.pages.search_by_page import SearchPage


class TestClass:
    @pytest.mark.parametrize('category_index, item_index', [(6, 7)])
    def test_adding_an_item_to_a_basket(self, driver, item_index, category_index):
        with allure.step('1. Открыть главную страницу'):
            main_page = MainPage(driver)
            main_page.open(Host.FIFTH_EL)

        with allure.step('2. Открыть вкладку необходимой категории'):
            main_page.click_element_from_list(main_page.slider_for_product_categories, category_index)

        with allure.step('3. Найти названия  всех товаров в списке найденных товаров и найти одно опреденное название'):
            search_page = SearchPage(driver)
            name_of_an_item = search_page.get_text_from_list(search_page.names_of_items_xpath, item_index)

        with allure.step("4. Нажать на кпопку 'В корзину' какого-то из товаров"):
            search_page.click_element_from_list(search_page.add_to_a_basket_button_xpath, item_index)

        with allure.step("5. Нажать кнопку 'Перейти в корзину'"):
            search_page.click_by_xpath(search_page.go_to_a_basket_button_xpath)

        with allure.step('6. Определить название товара в корзине'):
            basket_page = BasketPage(driver)
            item_name_in_a_basket = basket_page.get_a_text(basket_page.item_name_in_a_basket)

        with allure.step('7. Сравнить название добавленного товара и товара в корзине'):
            assert name_of_an_item == item_name_in_a_basket, f'Expected name: {name_of_an_item}, Actual name: {item_name_in_a_basket}'
