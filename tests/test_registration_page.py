import allure
from source_code.constants import Info
from source_code.pages.sign_in_page import SignInPage


class TestRegistration:
    def test_sign_in_process(self, driver, main_page):
        with allure.step("1. Нажать кнопку 'Войти'"):
            main_page.click_by_xpath(main_page.sign_in_xpath)

        with allure.step("2. Перейти на форму регистрации"):
            sign_in_page = SignInPage(driver)
            sign_in_page.click_by_xpath(sign_in_page.registration_xpath)

        with allure.step("3. Ввести номер телефона"):
            sign_in_page.fill_in_a_form(sign_in_page.phone_number_input, Info.PHONENUMBER)

        with allure.step("4. Нажать кнопку 'Зарегистрироваться и войти'"):
            sign_in_page.click_by_xpath(sign_in_page.register_button_xpath)

        with allure.step("5. Нажать кнопку 'Подтверждаю'"):
            sign_in_page.click_by_xpath(sign_in_page.accepting_button_xpath)

    def test_log_in_process(self, driver, main_page):
        with allure.step("1.Нажать кнопку 'Войти'"):
            main_page.click_by_xpath(main_page.sign_in_xpath)

        with allure.step("2. Войти с помощью своего профиля Mail.ru "):
            sign_in_page = SignInPage(driver)
            sign_in_page.click_by_xpath(sign_in_page.email_registration)

        with allure.step("3.Заполнить поля 'Электронная почта' и 'Пароль'"):
            sign_in_page.fill_in_a_form_to_sign(-1)

        with allure.step("4. Проверить, что вход в кабинет произошел "):

            main_page.switch_handler(0)
            text = main_page.get_a_text(main_page.my_oz_xpath)
            assert text == 'Мой OZ', f"Expected text 'Мой OZ', actual text {text}"
