from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class DragAndDropPage(BasePage):

  A_BLOCK = (By.CSS_SELECTOR, "[id='column-a']")
  B_BLOCK = (By.CSS_SELECTOR, "[id='column-b']")
    
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

  def drag_and_drop_action(self, src, dest):
    src_locator = self.A_BLOCK if src == 'A' else self.B_BLOCK
    dest_locator = self.B_BLOCK if dest == 'B' else self.A_BLOCK
    
    action_chains = ActionChains(self.driver)
    action_chains.drag_and_drop(self.get_element(src_locator), self.get_element(dest_locator)).perform()
    time.sleep(2)

  def verify_src_and_dest_text(self, srcText, destText):
    expected_a_block_txt = self.get_element_text(self.A_BLOCK)
    expected_b_block_txt = self.get_element_text(self.B_BLOCK)
    assert srcText == expected_a_block_txt, f"Expected: {srcText}, Actual: {expected_a_block_txt}"
    assert destText == expected_b_block_txt, f"Expected: {destText}, Actual: {expected_b_block_txt}"