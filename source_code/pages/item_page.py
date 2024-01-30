from source_code.pages.catalog_page import CatalogPage


class ItemPage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_favorite_xpath = "(//*[@class='b-product-action__content'])[1]"

        self.item_name_xpath = "//*[@class='b-product-title']//*[@itemprop='name']"

        self.item_number_xpath = "//*[@class='b-product-title__art']"

        self.wait_list_xpath = "//*[@id='frm-wait']"

        self.add_to_basket_btn_xpath = "//*[@method='GET']//*[@type='submit' and @onclick='this.blur();']"

        self.go_to_basket_btn_xpath = "//*[@class='b-product-control__btn-container']//*[@href='/checkout/']"
