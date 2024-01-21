import allure
from source_code.constants import Search
from source_code.pages.catalog_page import CatalogPage
from source_code.pages.item_page import ItemPage


class TestSearch:
    def test_searching_by_brand_name(self, driver, main_page):
        with allure.step("1. В строку поиcка ввести название"):

            main_page.fill_in_a_form(main_page.input_form_xpath, Search.BRAND)
            main_page.click_by_xpath(main_page.search_button_xpath)

        with allure.step("2. Выбрать случайный найденный товар и определить его бренд"):
            catalog_page = CatalogPage(driver)
            brand_names = catalog_page.get_random_element_by_xpath(catalog_page.brand_name_xpath)
            name = catalog_page.get_a_text(brand_names)

        with allure.step("3. Проверить,совпадает ли введенный бренд с брендом найденных товаров"):
            assert Search.BRAND in name, f'Expected brand {Search.BRAND}, actual brand {name}'

    def test_searching_by_item_number(self, driver, main_page):
        with allure.step("1. В строку поиска ввести артикул"):
            main_page.fill_in_a_form(main_page.input_form_xpath, Search.ITEMNUMBER)
            main_page.click_by_xpath(main_page.search_button_xpath)

        with allure.step("2. Проверить,совпадает ли номер товара с номером найденного товара"):
            item_page = ItemPage(driver)
            item_number = item_page.get_a_text(item_page.item_number_xpath)
            assert Search.ITEMNUMBER in item_number, f'Expected item number {Search.ITEMNUMBER}, actual item number {item_number}'
