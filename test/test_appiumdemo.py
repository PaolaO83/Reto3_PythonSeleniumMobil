"""
Tests de UI para ApiDemos — entorno LOCAL.
Requiere: servidor Appium corriendo en http://127.0.0.1:4723 y emulador Pixel_9 activo.

Ejecutar:
    pytest test/test_apidemos.py -v --alluredir=allure-results
"""
import allure
import pytest
from scenarios import scenario_invoke_search_and_back_home, scenario_select_checks_and_back, scenario_select_checks_isolated_service,scenario_select_checks_intent_activity

pytestmark = pytest.mark.local


@allure.feature("ApiDemos - Búsqueda")
@allure.story("Invoke Search y volver al Home")
@allure.tag("local")
def test_invoke_search_and_back_home(driver):
    scenario_invoke_search_and_back_home(driver)


@allure.feature("ApiDemos - Fragment")
@allure.story("Seleccionar checkboxes en Nesting Tabs y volver a Fragment")
@allure.tag("local")
def test_select_checks_and_back(driver):
    scenario_select_checks_and_back(driver)

@allure.feature("AppiumDemos - Service")
@allure.story("Seleccionar checkbox2 y boton2 en Service")
@allure.tag("saucelabs")
def test_scenario_select_checks_isolated_service(driver):
    scenario_select_checks_isolated_service(driver)

@allure.feature("AppiumDemos - Activity")
@allure.story("Seleccionar Intent Activity en Activity")
@allure.tag("saucelabs")
def test_scenario_select_checks_intent_activity(driver):
    scenario_select_checks_intent_activity(driver)


