from behave import *
from lambda_function import lambda_handler


@given(u'GitHub user "{user_name}"')
def step_impl(context, user_name):
    context.github_username = user_name


@when(u"rover fetches the data")
def step_impl(context):
    event = {"body": {"username": str(context.github_username)}}
    context.response = lambda_handler(event, {})


@then(u"a json object should be returned")
def step_impl(context):
    assert type(context.response) == "dict"


@then(u"login should equal the github user")
def step_impl(context):
    assert context.response.json().get("login") == context.github_username
