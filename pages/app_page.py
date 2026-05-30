from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AppPage(BasePage):
    """Page Object del submenú App."""

    _SEARCH = (AppiumBy.ACCESSIBILITY_ID, "Search")
    _FRAGMENT = (AppiumBy.ACCESSIBILITY_ID, "Fragment")
    _SERVICE = (AppiumBy.ACCESSIBILITY_ID, "Service")
    _ACTIVITY = (AppiumBy.ACCESSIBILITY_ID, "Activity")
    

    def is_displayed(self) -> bool:
        """Verifica que la pantalla App está visible."""
        return self.is_element_present(self._SEARCH)

    def go_to_search(self):
        """Navega al submenú Search y retorna SearchPage."""
        from pages.search_page import SearchPage
        self.wait_and_click(self._SEARCH)
        return SearchPage(self.driver)

    def go_to_fragment(self):
        """Navega al submenú Fragment y retorna FragmentPage."""
        from pages.fragment_page import FragmentPage
        self.wait_and_click(self._FRAGMENT)
        return FragmentPage(self.driver)
    
    def go_to_service(self):
        """Navega al submenú Service y retorna ServicePage."""
        from pages.services_page import ServicePage
        self.wait_and_click(self._SERVICE)
        return ServicePage(self.driver)
    
    def go_to_activity(self):
        """Navega a la opción Activity."""
        from pages.activity_page import ActivityPage
        self.wait_and_click(self._ACTIVITY)
        return ActivityPage(self.driver)
    
    
