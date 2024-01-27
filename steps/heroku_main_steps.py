from pages.HerokuMainPage import HerokuMainPage
from behave import *

@given('user navigates to HerokuMainPage')
def user_navigate_to_heroku_main_page(context):
  context.heroku_main_page = HerokuMainPage(context.driver)
  context.heroku_main_page.navigate_heroku_url()

@when('user on HerokuMainPage clicks on Form Authentication')
def user_on_heroku_main_page_clicks_on_form_authentication(context):
  context.heroku_main_page.click_on_form_authentication()

@when('user on HerokuMainPage clicks on DragAndDrop')
def user_on_heroku_main_page_clicks_on_drag_and_drop(context):
  context.heroku_main_page.click_on_drag_and_drop()