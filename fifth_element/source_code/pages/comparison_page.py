from fifth_element.source_code.pages.search_by_page import SearchPage

class ComparisonPage(SearchPage):
    def __init__(self, driver):
        super().__init__(driver)

        # .text возвращает названия товаров
        self.names_of_items_to_compare = "//*[@class='c-part-info']//*[@class='c-text']"

    def assert_added_item_for_comparison(self, index):
        item_name = self.get_text_from_list(self.names_of_items_xpath, index)
        self.click_element_from_list(self.add_to_compare, index)
        self.click_by_xpath(self.comparison_button)
        get_a_name = self.get_a_text(self.names_of_items_to_compare)
        assert item_name == get_a_name, f'{item_name}, {get_a_name}'
