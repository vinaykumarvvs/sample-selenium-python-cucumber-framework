from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class FormAuthenticationLoginPage(BasePage):

  USERNAME_TXT = (By.CSS_SELECTOR, "[id='username']")
  PASSWORD_TXT = (By.CSS_SELECTOR, "[id='password']")
  LOGIN_BTN = (By.CSS_SELECTOR, "[type='submit']")
  LOGIN_SUCCESS_TXT = (By.CSS_SELECTOR, "[id='content'] h2")
  ERROR_TXT = (By.CSS_SELECTOR, "[id='flash']")
    
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

  def fill_username_and_password(self, username, password):
    self.enter_text(self.USERNAME_TXT, username)
    self.enter_text(self.PASSWORD_TXT, password)

  def click_on_login(self):
    self.click_on(self.LOGIN_BTN)

  def verify_login_text(self, text_verify):
    actual_text = self.get_element_text(self.LOGIN_SUCCESS_TXT)
    assert actual_text == text_verify

  def verify_error_text(self, error_message):
    time.sleep(2)
    actual_text = self.get_element_text(self.ERROR_TXT)
    assert error_message in actual_text