# Gestor de Pedidos - Práctica de Refactorización y Testing

## Descripción

Aplicación desarrollada en Python para la gestión de clientes y pedidos. Durante la práctica se han aplicado técnicas de análisis de código, refactorización, pruebas automatizadas y control de versiones con Git y GitHub.

---

# Ejercicio 4: Análisis del código

## Problemas detectados

### Problema 1

Los cálculos de subtotal, descuentos e IVA estaban duplicados en varias funciones del módulo `pedidos.py`. Esto dificultaba el mantenimiento porque cualquier cambio en las reglas de negocio debía realizarse en varios lugares.

### Problema 2

Existía código sin utilizar, como la función `cambiar_estado_pedido()`, que no era llamada desde ninguna parte del programa.

### Problema 3

Había una mezcla entre lógica de negocio e interfaz de usuario. Muchas funciones realizaban cálculos y al mismo tiempo utilizaban `input()` y `print()`, dificultando las pruebas y el mantenimiento.

---

## Mejoras propuestas

### Refactorización 1

Se creó una función centralizada para el cálculo de subtotales, descuentos, IVA y total del pedido.

### Refactorización 2

Se separó parcialmente la lógica de negocio de la interfaz de usuario, reduciendo la duplicación de código y mejorando la organización del proyecto.

---

# Ejercicio 5 y 6: Refactorización

## Cambios realizados

### Centralización de cálculos

Se creó la función:

```python
def calcular_totales(pedido):
```

Esta función calcula:

* Subtotal
* Descuento
* IVA
* Total final

evitando la duplicación de código.

### Mejora de descuentos

Se creó la función:

```python
def calcular_descuento(total):
```

para gestionar todas las reglas de descuento desde un único punto.

### Nuevas clases

Para permitir la ejecución de las pruebas automáticas se añadieron:

```python
class Cliente
class Pedido
class LineaPedido
```

---

# Ejercicio 7: Pruebas con Pytest

## Objetivo

Comprobar automáticamente el correcto funcionamiento del código.

### Instalación

```bash
pip install pytest
```

o

```bash
py -m pip install pytest
```

### Ejecución

```bash
py -m pytest
```

### Pruebas incluidas

#### Clientes

* Cliente válido.
* Email inválido.
* Nombre vacío.
* Validación de email.

#### Pedidos

* Cálculo de subtotal.
* Cálculo de totales.
* Aplicación de descuentos.
* Validación de cantidades.
* Total final del pedido.

---

# Ejercicio 8 y 9: Calidad del código

Se corrigieron avisos detectados por las herramientas de análisis estático.

### Ejemplos

Antes:

```python
while salir == False:
```

Después:

```python
while not salir:
```

Antes:

```python
if encontrado == False:
```

Después:

```python
if not encontrado:
```

Estas modificaciones mejoran la legibilidad y siguen las recomendaciones de PEP 8.

---

# Ejercicio 10: Trabajo con ramas

## Creación de rama

```bash
git switch -c refactor-descuentos
```

## Cambios realizados

* Refactorización de la lógica de descuentos.
* Mejora de la mantenibilidad del código.

## Commit realizado

```bash
git add .
git commit -m "Refactoriza lógica de descuentos"
```

## Publicación en GitHub

```bash
git push -u origin refactor-descuentos
```

---

# Tecnologías utilizadas

* Python 3
* Pytest
* Git
* GitHub

---

# Autor

Ismail Hammouch

Práctica de refactorización, testing y control de versiones.
