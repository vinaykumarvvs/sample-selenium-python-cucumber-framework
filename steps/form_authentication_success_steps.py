from behave import *
from pages.FormAuthenticationSucessPage import FormAuthenticationSuccessPage

@then('user on FormAuthenticationSuccessPage verifies this message "{text_verify}"')
def user_on_form_authentication_success_verifies_message(context, text_verify):
  context.form_authentication_success_page = FormAuthenticationSuccessPage(context.driver)
  context.form_authentication_success_page.verify_success_text(text_verify=text_verify)

@when('user on FormAuthenticationSuccessPage clicks on logout')
def user_on_form_authentication_clicks_on_logout(context):
  context.form_authentication_success_page.click_on_logout()