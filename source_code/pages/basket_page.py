from source_code.pages.common_page import CommonPage


class BasketPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.item_in_a_basket_name_xpath = "//*[contains(@class, 'goods-table-cell__line_title')]"

        self.select_delivery_xpath = "//*[@id='select-delivery-link']"

        self.town_options = "//*[contains(@class, 'i-context')]//*[@class='i-pseudolink']"

        self.chosen_town_xpath = "//*[@class='i-pseudolink__select']//*[contains(text(), 'область') and not(contains(text(), 'Ратомка'))]"

        self.chosen_address_xpath = "//li[not(contains(@style,'display: none;'))]//*[contains(text(), 'Самовывоз')]"

        self.payment_title = "//*[@class='i-context-box-main__title i-h i-h_2']"

        self.payment_methods_xpath = "//*[@id='select-payment-link']"

        self.choose_payment_method_xpath = "//*[@class='i-context-box-list__item ']//*[@class='i-context-box-list__line']"

        self.check_item_xpath = "(//*[@class='i-checkbox i-checkbox_large'])[1]"

        self.remove_item_xpath = "//*[contains(@class, 'goods-table')]//*[@role='button' and contains(@class, 'remove')]"

        self.confirm_removing_xpath = "//*[contains(@class, 'remove') and @data-popup-button='submit']"

        self.empty_cart_xpath = "//*[contains(@class, 'i-textual__plain')]"

        self.continue_btn = "//*[@type='button' and @name='payment-apply']"

        self.assert_address_xpath = "//*[@href='#pickDelivery']//*[@class='i-input__sub']"

        self.assert_payment_xpath = "//*[@href='#pickPayment']//*[@class='i-input__sub']"

    def remove_item_from_cart(self):
        self.click_by_xpath(self.check_item_xpath)
        self.click_by_xpath(self.remove_item_xpath)
        self.click_by_xpath(self.confirm_removing_xpath)

    def get_a_town(self):
        self.click_by_xpath(self.select_delivery_xpath)
        self.click_by_xpath(self.town_options)
        chosen_town_xpath = self.get_random_element_by_xpath(self.chosen_town_xpath)
        self.click_by_xpath(chosen_town_xpath)

    def get_a_payment_method(self):
        self.click_by_xpath(self.payment_methods_xpath)
        title = self.get_a_text(self.payment_title)
        assert title == 'Способ оплаты', f"Expected text 'Способ оплаты', actual text {title}"
        payment_method_xpath = self.get_random_element_by_xpath(self.choose_payment_method_xpath)
        self.click_by_xpath(payment_method_xpath)
        payment_method = self.get_a_text(payment_method_xpath)
        return payment_method
