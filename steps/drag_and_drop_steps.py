from pages.DragAndDropPage import DragAndDropPage
from behave import *
import time

@when('user on DragAndDropPage drags "{src}" on top of "{dest}"')
def user_performs_drag_and_drop_action(context, src, dest):
  context.drag_and_drop_page = DragAndDropPage(context.driver)
  context.drag_and_drop_page.drag_and_drop_action(src, dest)

@then('user on DragAndDropPage verifies the first block text as "{src}" and second block text as "{dest}"')
def user_verifies_drag_and_drop_data(context, src, dest):
  context.drag_and_drop_page.verify_src_and_dest_text(src, dest)
  time.sleep(5)

