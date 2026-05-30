from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class isolatedServicePage(BasePage):
    """Page Object de la pantalla Isolated Services Controller con chekbox  y boton."""

    _BOTON2 = (AppiumBy.ID, "io.appium.android.apis:id/start2")
    _CHECK2 = (AppiumBy.ID, "io.appium.android.apis:id/bind2")

    
    def is_displayed(self) -> bool:
        """Verifica que el checkbox 2 está visible."""
        return self.is_element_present(self._CHECK2)

    def select_boton2(self) -> "isolatedServicePage":
        """Selecciona el boton 2."""
        self.wait_and_click(self._BOTON2)
        return self

    def select_check2_if_unchecked(self) -> "isolatedServicePage":
        """Selecciona el checkbox 2 si no está marcado."""
        check = self.wait_for_element(self._CHECK2)
        if not check.is_selected():
            check.click()
        return self

    def go_back(self):
        """Vuelve un nivel y retorna ServicePage."""
        from pages.isolated_service_page import isolatedServicePage
        self.driver.back()
        return isolatedServicePage(self.driver)
