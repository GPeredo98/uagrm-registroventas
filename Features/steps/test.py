from behave import *

use_step_matcher("re")


@given("enviamos los datos de prueba")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("enviamos los datos de prueba")


@when("cuando ocurra lo siguiente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("cuando ocurra lo siguiente")


@then("esperamos el resultado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("esperamos el resultado")