from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

  def __init__(self, driver):
    self.driver = driver
    self.time_to_wait = 30

  def click_on(self, by_locator):
    WebDriverWait(self.driver, self.time_to_wait).until(EC.visibility_of_element_located(by_locator)).click()

  def enter_text(self, by_locator, text):
    WebDriverWait(self.driver, self.time_to_wait).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

  def get_element_text(self, by_locator):
    return WebDriverWait(self.driver, self.time_to_wait).until(EC.visibility_of_element_located(by_locator)).text
  
  def get_element(self, by_locator):
    return WebDriverWait(self.driver, self.time_to_wait).until(EC.visibility_of_element_located(by_locator))