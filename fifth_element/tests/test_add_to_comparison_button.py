import allure

from fifth_element.source_code.constants import Host
from fifth_element.source_code.pages.comparison_page import ComparisonPage
from fifth_element.source_code.pages.main_page import MainPage


class TestClass:
    def test_add_to_comparison_button(self, driver):
        with allure.step('1. Открыть главную страницу'):
            main_page = MainPage(driver)
            main_page.open(Host.FIFTH_EL)

        with allure.step('2. Закрыть сообщение о cookie-файлах'):
            main_page.delay_and_click()

        with allure.step('2. Выбрать катеорию товара и перейти на страницу c товарами'):
            main_page.click_element_from_list(main_page.slider_for_product_categories, 2)

        with allure.step('3. Добавить товар в сравнение и проверить,тот ли товар добавился'):
            comparison_page = ComparisonPage(driver)
            comparison_page.assert_added_item_for_comparison(3)
        # Надо ли добавлять второй товар

        with allure.step('4. Добавить товар в сравнение и проверить,тот ли товарр добавился'):
            comparison_page = ComparisonPage(driver)
            comparison_page.assert_added_item_for_comparison(9)
