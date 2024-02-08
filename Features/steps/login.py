from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


@given('Usuario navega hasta la pagina del login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:4200/")
    time.sleep(1)
    context.driver.get("http://localhost:4200/login")
    print("Given... abrimos el navegador")


@when('el usuario ingresa sus credenciales, usuario: "{user}" y password: "{passw}"')
def step_impl(context, user, passw):
    username = context.driver.find_element(By.ID, 'email')
    username.clear()
    username.send_keys(user)
    time.sleep(1)
    password = context.driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys(passw)
    time.sleep(1)
    print(f"When...introducimos el username: {user} y password: {passw}")


@step('hace click en el boton Ingresar')
def step_impl(context):
    buton = context.driver.find_element(By.ID, 'Aceptar')
    buton.click()
    print("And... hacemos click en INGRESAR si esta habilitado y correcto debe ingresar")
    time.sleep(2)


@then('el usuario puede acceder al sistema de Ventas')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 3).until(
            EC.url_to_be("http://localhost:4200/admin/home")
        )
        time.sleep(2)
        print("Then...ingreso el usuario con exito!!!")
        assert True
    except:
        context.driver.get("http://localhost:4200/")
        time.sleep(2)
        assert False, "No se puede acceder"
