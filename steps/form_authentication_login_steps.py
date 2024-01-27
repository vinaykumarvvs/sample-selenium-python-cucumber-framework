from behave import *
from pages.FormAuthenticationLoginPage import FormAuthenticationLoginPage
import time

@when('user on FormAuthenticationLoginPage enter username as "{username}" and password as "{password}"')
def user_enters_username_password(context, username, password):
  context.form_authentication_page = FormAuthenticationLoginPage(context.driver)
  context.form_authentication_page.fill_username_and_password(username=username, password=password)

@when('user on FormAuthenticationLoginPage clicks on login')
def user_clicks_on_login(context):
  context.form_authentication_page.click_on_login()

@then('user on FormAuthenticationLoginPage verifies this message "{text_verify}"')
def user_verifies_message_on_form_authentication_login_page(context, text_verify):
  context.form_authentication_page.verify_login_text(text_verify)
  time.sleep(5)

@then('user on FormAuthenticationLoginPage verifies the error message as "{error_message}"')
def user_verifies_error_message_on_form_authentication_login_page(context, error_message):
  context.form_authentication_page.verify_error_text(error_message)
  time.sleep(5)