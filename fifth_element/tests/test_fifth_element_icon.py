import allure

from fifth_element.source_code.constants import Host
from fifth_element.source_code.pages.main_page import MainPage
from fifth_element.source_code.pages.search_by_page import SearchPage


class TestClass:
    def test_fifth_element_icon(self, driver):
        with allure.step('1. Открыть главную страницу и получить url страницы'):
            main_page = MainPage(driver)
            main_page.open(Host.FIFTH_EL)
            starting_url = main_page.get_an_url()

        with allure.step('2. Закрыть сообщение о cookie-файлах'):
            main_page.delay_and_click()

        with allure.step('3. Перейти на другую страницу и получить url страницы'):
            main_page.click_element_from_list(main_page.slider_for_product_categories, 4)
            search_page = SearchPage(driver)
            url_after_click = search_page.get_an_url()

        with allure.step('4. Сравнить starting url и url_after_click'):
            assert starting_url != url_after_click, f'Starting page url: {starting_url}, page url after click: {url_after_click}'

        with allure.step("5. Нажать на иконку '5 элемент и получить url страницы после клика'"):
            search_page.click_by_xpath(search_page.fifth_element_icon_xpath)
            back_to_starting_page = main_page.get_an_url()

        with allure.step('6. Сравнить starting_url и back_to_starting_page'):
            assert starting_url == back_to_starting_page, f'Starting page url: {starting_url}, page url after click: {back_to_starting_page}'



