from source_code.pages.common_page import CommonPage


class StoresPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.all_towns_xpath = "(//*[@aria-label='Навигация по городам'])[2]//*[contains(@class, 'item_arrow')]//*[contains(@class,'city-nav__title')]"

        self.chosen_location_xpath = "//*[@class='city-nav__submenu']//*[@class='city-nav__title']"

        self.go_to_store = "//*[@class='city-nav__submenu']//*[@class='link city-nav__link']"

        self.address_xpath = "(//*[@class='place-info__description content']//*)[1]"
