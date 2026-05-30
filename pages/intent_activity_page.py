from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class intentActivityPage(BasePage):
    """Page Object de la pantalla Intent Activity page."""

    # 1. Define los localizadores como atributos privados de clase
    _TASK1= (AppiumBy.ACCESSIBILITY_ID, "FLAG_ACTIVITY_CLEAR_TASK")
    _TASK2 = (AppiumBy.ID, "io.appium.android.apis:id/flag_activity_clear_task_pi")
   

    def is_displayed(self) -> bool:
        """Verifica que esta pantalla Intent Activity está visible."""
        return self.is_element_present(self._TASK1)
    
    def select_task2(self) -> "intentActivityPage":
        """Selecciona el boton task (PI)."""
        self.wait_and_click(self._TASK2)
        return self
    
    def go_back(self):
        """Vuelve un nivel y retorna Intent Activity Page."""
        from pages.intent_activity_page import IntentActivityPage
        self.driver.back()
        return IntentActivityPage(self.driver)


   