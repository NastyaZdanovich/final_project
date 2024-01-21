from source_code.pages.common_page import CommonPage


class CatalogPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.goods_xpath = "//*[@class='products__item item product-card ']//*[@class='link product-card__link']"

        self.brand_name_xpath = "//*[@class='products__item item product-card ']//*[@class='product-card__subtitle']"

        self.current_order_xpath = "//*[contains(@class, 'top-filters__eselect__item')]"

        self.top_filters_xpath = "//*[@class='top-filters__eselect__item top-filters__viewer__open']"

        self.list_sorting_xpath = "//*[@class='filters__chkslist__li ']"

        self.current_page_xpath = "//*[contains(@class, 'pg-current')]//*[contains(@class, 'active')]"

        self.pages_xpath = "//*[@class='g-pagination__list__li pg-link']"

        self.out_of_stock_xpath = "//*[@for='availability_3']"

        self.availability_one = "//*[@for='availability_1']"

        self.availability_two = "//*[@for='availability_2']"

        self.show_results_xpath = "//*[@class='filters__searchbtn__btn']"

    def choose_an_item(self):
        item = self.get_random_element_by_xpath(self.goods_xpath)
        self.click_by_xpath(item)

    def wait_list_items(self):
        self.click_by_xpath(self.availability_one)
        self.click_by_xpath(self.availability_two)
        self.click_by_xpath(self.out_of_stock_xpath)
        self.click_by_xpath(self.show_results_xpath)

