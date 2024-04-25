from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import then, given, when
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@given("Target Signin button pressed")
def click_sign_in(context):
    context.app.login_page.click_sign_in()


@given("Target Signin button popup")
def click_signin_popup(context):
    context.app.login_page.click_signin_popup()


@given("Target input credentials")
def input_credentials(context):
    context.app.login_page.input_credentials()


@given("Click sign in user")
def click_sign_in_user(context):
    context.app.login_page.click_sign_in_user()


@then("Verify the account")
def verify_account(context):
    context.app.login_page.verify_account()


@given("Verify the name")
def name_verify(context):
    context.app.home_page.name_verify()


@then("Verify the URL")
def verify_home_page_url(context):
    context.app.home_page.verify_home_page_url('https://www.target.com/')
    sleep(10)