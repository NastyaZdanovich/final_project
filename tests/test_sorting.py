import allure
from source_code.pages.catalog_page import CatalogPage


class TestSort:
    def test_sorting_by_order(self, driver, main_page):
        with allure.step("1. Перейти на страницу каталога с товарами"):
            main_page.choose_a_category()

        with allure.step("2. Определить,каким образом упорядочены товары"):
            catalog_page = CatalogPage(driver)
            initial_order_txt = catalog_page.get_a_text(catalog_page.current_order_xpath)

        with allure.step("3. Поменять порядок расположения товара"):
            catalog_page.click_by_xpath(catalog_page.top_filters_xpath)

            new_order = catalog_page.get_random_element_by_xpath(catalog_page.list_sorting_xpath)
            catalog_page.click_by_xpath(new_order)

        with allure.step("4. Определить, каким образом упорядочены товары после изменения"):
            new_order_txt = catalog_page.get_a_text(catalog_page.current_order_xpath)

        with allure.step("5. Сравнить изначальный и  измененный порядок расположения товаров"):
            assert initial_order_txt != new_order_txt, f'Initial order {initial_order_txt}, order after change {new_order_txt}'
