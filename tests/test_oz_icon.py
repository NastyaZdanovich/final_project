import allure
from source_code.pages.catalog_page import CatalogPage


class TestOzIcon:
    def test_oz_icon(self, driver, main_page):
        with allure.step('1. Открыть главную страницу и получить url страницы'):
            starting_url = main_page.get_an_url()

        with allure.step('2. Перейти на другую страницу и получить url страницы'):
            main_page.choose_a_category()
            catalog_page = CatalogPage(driver)
            url_after_click = catalog_page.get_an_url()

        with allure.step('3. Сравнить starting url и url_after_click'):
            assert starting_url != url_after_click, f'Starting page url: {starting_url}, page url after click: {url_after_click}'

        with allure.step("4. Нажать на иконку '5 элемент и получить url страницы после клика'"):
            catalog_page.click_by_xpath(catalog_page.oz_icon_xpath)
            back_to_starting_page = main_page.get_an_url()

        with allure.step('5. Сравнить starting_url и back_to_starting_page'):
            assert starting_url == back_to_starting_page, f'Starting page url: {starting_url}, page url after click: {back_to_starting_page}'
