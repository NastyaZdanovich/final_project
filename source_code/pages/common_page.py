from source_code.pages.base_page import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.accept_cookie_xpath = "//*[@class='popup bg-light']//*[contains(@class, 'dark me')]"

        self.oz_icon_xpath = "//*[@href='/' and contains(@class, 'brand')]"

        self.catalog_xpath = "//li[@class='main-nav__list__li main-nav__list__li_wnav']//a[contains(@class, 'item') and not(contains(text(), 'Магазины OZ'))]"

        self.out_of_stock_catalog_xpath = "//li[@class='main-nav__list__li main-nav__list__li_wnav']//a[contains(@class, 'item') and not(contains(@href, '/books/'))]"

        self.sign_in_xpath = "//*[@class='user-bar__item' ]"

        self.my_oz_xpath = "//*[contains(@href, '/personal/orders/')]"

        self.favorites_xpath = "//*[@href='/personal/favorites']//*[@class='user-bar__icon-group']"

        self.input_form_xpath = "//*[@id='top-s']"

        self.search_button_xpath = "//*[@class='search-form__submit']"

        self.all_stores_xpath = "//*[@id='storesTab']//*[@href='/store/']"
