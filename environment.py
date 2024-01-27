from utils.helper import *

def before_all(context):
  context.driver = None

def before_scenario(context, scenario):
  context.driver = create_driver()

def after_scenario(context, scenario):
  if context.driver:
    context.driver.quit()
    context.driver = None
