# Created by waldy at 4/2/24
Feature: Gestión de venta de un producto

  Scenario: Agregar un producto al carrito
    Given que hay un producto con código "P001", nombre "Camiseta", precio unitario 20.00, cantidad 5, y descuento del 10%
    When el usuario agrega el producto al carrito
    Then el producto "Camiseta" debe estar en el carrito con un precio de 90.00