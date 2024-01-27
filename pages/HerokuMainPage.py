from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HerokuMainPage(BasePage):

  FORM_AUTHENTICATION = (By.XPATH, "//*[text()='Form Authentication']")
  DRAG_AND_DROP = (By.XPATH, "//*[text()='Drag and Drop']")

  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

  def navigate_heroku_url(self):
    self.driver.get("https://the-internet.herokuapp.com/")

  def click_on_form_authentication(self):
    self.click_on(self.FORM_AUTHENTICATION)

  def click_on_drag_and_drop(self):
    self.click_on(self.DRAG_AND_DROP)
  

