from clientes import clientes
from utilidades import pedir_numero

pedidos = []


class LineaPedido:
    """Clase que representa una línea de pedido con producto, precio y cantidad.
    """
    def __init__(self, producto, precio, cantidad):
        """setup de la clase LineaPedido

        Args:
            producto (): producto de la línea de pedido
            precio (): precio unitario del producto
            cantidad (): cantidad del producto en la línea de pedido
        """
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        return self.precio * self.cantidad


def calcular_total_lineas(lineas):
    """calculo el total de una lista de líneas de pedido

    Args:
        lineas (List[LineaPedido]): lista de objetos LineaPedido

    Returns:
        float: el total de las líneas de pedido
    """
    return sum(linea.subtotal() for linea in lineas)


def calcular_descuento(total):
    """ calculo el descuento a aplicar según el total de las líneas de pedido

    Args:
        total (float): total de las líneas de pedido

    Returns:
        float: descuento a aplicar
    """
    if total > 250:
        return total * 0.15

    if total > 100:
        return total * 0.10

    return 0


class Pedido:
    """Clase que representa un pedido con un cliente y una lista de líneas de pedido."""
    def __init__(self, cliente):
        self.cliente = cliente
        self.lineas = []

    def agregar_linea(self, linea):
        self.lineas.append(linea)

    def total_con_descuento(self):
        """total del pedido con descuento aplicado

        Returns:
            float: el total del pedido con descuento aplicado
        """
        subtotal = calcular_total_lineas(self.lineas)
        descuento = calcular_descuento(subtotal)
        return subtotal - descuento


def menu_pedidos():
    fin = False

    while not fin:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    print("\nCREAR PEDIDO")

    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    for i, cliente in enumerate(clientes):
        print(f"{i + 1}. {cliente['nombre']}")

    numero_cliente = pedir_numero("Elige cliente: ")

    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"

    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append({
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio
            })
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {
        "cliente": clientes[numero_cliente - 1],
        "lineas": lineas,
        "estado": "pendiente"
    }

    pedidos.append(pedido)
    print("Pedido creado")


def calcular_totales(pedido):
    subtotal = 0

    for linea in pedido["lineas"]:
        subtotal += linea["cantidad"] * linea["precio"]

    descuento = calcular_descuento(subtotal)

    base_imponible = subtotal - descuento
    iva = base_imponible * 0.21
    total = base_imponible + iva

    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "iva": iva,
        "total": total
    }


def ver_pedidos():
    print("\nLISTADO DE PEDIDOS")

    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    for i, pedido in enumerate(pedidos):
        resultado = calcular_totales(pedido)

        print(
            f"{i + 1}. Cliente: {pedido['cliente']['nombre']} | "
            f"Estado: {pedido['estado']} | "
            f"Total: {round(resultado['total'], 2)} €"
        )


def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")

    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    resultado = calcular_totales(pedidos[n - 1])

    print("Subtotal:", round(resultado["subtotal"], 2))
    print("Descuento:", round(resultado["descuento"], 2))
    print("IVA:", round(resultado["iva"], 2))
    print("TOTAL:", round(resultado["total"], 2))