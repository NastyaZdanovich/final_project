import allure
from source_code.pages.stores_page import StoresPage


class TestCheckTown:
    def test_check_stores_in_town(self, driver, main_page):
        with allure.step("1. Открыть вкладку с городами и выбрать город "):
            main_page.click_by_xpath(main_page.all_stores_xpath)

            stores_page = StoresPage(driver)
            town_xpath = stores_page.get_random_element_by_xpath(stores_page.all_towns_xpath)
            town_name = stores_page.get_a_text(town_xpath)
            stores_page.click_by_xpath(town_xpath)

        with allure.step("2. Определить название полученного города и проверить, совпадает ли название с названием выбранного города"):
            chosen_town = stores_page.get_a_text(stores_page.chosen_location_xpath)
            assert town_name == chosen_town

        with allure.step("3. Перейти по ссылке 'В магазин' на страницу магазина"):
            link = stores_page.get_random_element_by_xpath(stores_page.go_to_store)
            stores_page.click_by_xpath(link)
            address = stores_page.get_a_text(stores_page.address_xpath)

        with allure.step("4. Проверить,есть ли в адресе название города"):
            assert town_name in address
