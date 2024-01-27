from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class FormAuthenticationSuccessPage(BasePage):
  SUCCESS_TEXT = (By.CSS_SELECTOR, "[class='example'] h2")
  LOGOUT_BTN = (By.CSS_SELECTOR, "[href='/logout']")
    
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

  def verify_success_text(self, text_verify):
    actual_text = self.get_element_text(self.SUCCESS_TEXT)
    assert actual_text == text_verify

  def click_on_logout(self):
    self.click_on(self.LOGOUT_BTN)