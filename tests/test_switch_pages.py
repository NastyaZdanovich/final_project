import allure
from source_code.pages.catalog_page import CatalogPage


class TestSwitchPages:
    def test_switch_pages(self, driver, main_page):
        with allure.step("1. В строку поиcка ввести название"):
            main_page.choose_a_category()

        with allure.step("2. Проверить номер страницы, которая сейчас просматривается"):
            catalog_page = CatalogPage(driver)
            initial_page = catalog_page.get_a_text(catalog_page.current_page_xpath)

        with allure.step("3. Перейти на другую страницу и определить номер страницы"):
            new_page_xpath = catalog_page.get_random_element_by_xpath(catalog_page.pages_xpath)
            catalog_page.click_by_xpath(new_page_xpath)
            new_page = catalog_page.get_a_text(new_page_xpath)

        with allure.step("4. Проверить несовпадение начального номера страницы и после перехода на другую страницу"):
            assert initial_page != new_page, f'Initial page {initial_page}, new page {new_page}'
