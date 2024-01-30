from source_code.constants import Info
from source_code.pages.common_page import CommonPage


class SignInPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.registration_xpath = "//*[@id='loginFormRegisterLink']"

        self.phone_number_input = "(//*[contains(@class, 'input focus') and @type='tel'])[2]"

        self.register_button_xpath = "//*[@value='register']"

        self.accepting_button_xpath = "//*[@role='button' and @form='pp_form']"

        self.email_registration = "(//*[contains(@href, 'id=mailru')])[1]"

        self.confirm_email_xpath = "//*[@id='login']"
        self.confirm_password_xpath = "//*[@id='password']"
        self.enter = "//*[@class='ui-button-main']"


    def fill_in_a_form_to_sign(self, index):
        self.switch_handler(index)
        self.fill_in_a_form(self.confirm_email_xpath, Info.EMAIL)
        self.fill_in_a_form(self.confirm_password_xpath, Info.PASSWORD)
        self.click_by_xpath(self.enter)


