from playwright.sync_api import Page

class HomePage(Page):
    def __init__(self, page : Page):
        self.page = page
        self.filter_button = page.get_by_text("Name (A to Z)Name (A to Z)")
        self.option_button = page.locator("[data-test=\"product-sort-container\"]")
        self.jacket_button = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")

    def filter(self):
        self.filter_button.click()


    def option(self):
        self.option_button.select_option("hilo")

    def jacket(self):
        self.jacket_button.click()