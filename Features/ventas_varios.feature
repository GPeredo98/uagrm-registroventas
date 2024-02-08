# Created by waldy at 6/2/24
Feature: Gestion de venta de varios productos
  # Enter feature description here

  Scenario Outline: Agregar varios productos al carrito
    Given se agrega al carrito item(s) con codigo "<cod_producto>", nombre "<nombre>", en la cantidad de <cantidad> unidades, al precio unitario de <precio_unitario> y con un descuento del <descuento>%
    When se verifica el producto
    Then el producto debe estar en el carrito con un precio de <precio_total>
    Examples:
      | cod_producto | nombre    | cantidad | precio_unitario | descuento | precio_total |
      | P001         | Producto1 | 3        | 5.00            | 10        | 13.50        |
      | P002         | Producto2 | 1        | 50.00           | 20        | 40.00        |
      | S001         | Servicio1 | 1        | 100.00          | 10        | 90.00        |
      | P003         | Camiseta  | 2        | 30.00           | 10        | 50.00        |
      | P005         | Mac       | 1        | 2000.00         | 10        | 1800.00      |