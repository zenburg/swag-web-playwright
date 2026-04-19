from playwright.sync_api import Page

class LogoutPage(Page):
    def __init__(self,page: Page):
        self.menu = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.locator("[data-test=\"logout-sidebar-link\"]")

    def logout(self):
        self.menu.click()
        self.logout_button.click()

