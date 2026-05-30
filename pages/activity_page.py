from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ActivityPage(BasePage):
    """Page Object de la pantalla Activity page."""

    # 1. Define los localizadores como atributos privados de clase
    _ACTIVITY = (AppiumBy.ACCESSIBILITY_ID, "Activity")
    _INTENT = (AppiumBy.ID, "android:id/list")
   

    def is_displayed(self) -> bool:
        """Verifica que esta pantalla Activity está visible."""
        return self.is_element_present(self._ACTIVITY)

    def go_to_intent_activity_flags(self):
        """Navega a la  pantalla Intent Activity."""
        from pages.intent_activity_page import IntentActivityPage
        self.wait_and_click(self._INTENT)
        return IntentActivityPage(self.driver)

