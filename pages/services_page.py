from appium.webdriver.common.appiumby import AppiumBy #importar el appiumby para identificar
from pages.base_page import BasePage


class ServicePage(BasePage):
    """Page Object del submenú Service de App Demo."""

    _SERVICE = (AppiumBy.ACCESSIBILITY_ID, "Services") #Metodo de appium para encontrar un accibility por el nombre
    _ISOLATED_SERVICE = (AppiumBy.ACCESSIBILITY_ID, "Isolated service Controller")
    #Messenger Service

    #se agrega los metodosde navegacion

    def is_displayed(self) -> bool:
        """Verifica que la pantalla Service está disponible."""
        return self.is_element_present(self._SERVICE)

    def go_to_isolated_service(self):
        """Navega a Isolated Service y retorna InvokeSearchPage."""
        from pages.isolated_service_page import isolatedServicePage
        self.wait_and_click(self._ISOLATED_SERVICE)
        return isolatedServicePage(self.driver)
    