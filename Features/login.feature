# Created by waldy at 8/2/24
Feature: Login al Sistema de Ventas
  # Enter feature description here

  Scenario: Verificar la funcionalidad de login del Sistema
    Given Usuario navega hasta la pagina del login
    When el usuario ingresa sus credenciales, usuario: "atuny0" y password: "9uQFF1Lh"
    And hace click en el boton Ingresar
    Then el usuario puede acceder al sistema de Ventas