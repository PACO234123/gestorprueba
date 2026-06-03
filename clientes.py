clientes = []


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_email(email):
    return "@" in email and "." in email


class Cliente:
    def __init__(self, nombre, email, telefono=""):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def es_valido(self):
        return validar_nombre(self.nombre) and validar_email(self.email)


def menu_clientes():
    terminar = False

    while not terminar:
        print("\n--- CLIENTES ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")

        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            terminar = True
        else:
            print("No existe esa opción")


def crear_cliente():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío")
        return

    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    clientes.append(cliente)
    print("Cliente añadido")


def listar_clientes():
    print("\nLISTADO DE CLIENTES")

    if len(clientes) == 0:
        print("No hay clientes")
        return

    for i, cliente in enumerate(clientes):
        print(
            f"{i + 1}. {cliente['nombre']} - "
            f"{cliente['telefono']} - "
            f"{cliente['email']}"
        )


def buscar_cliente():
    texto = input("Texto a buscar: ")

    encontrado = False

    for cliente in clientes:
        if (
            texto.lower() in cliente["nombre"].lower()
            or texto in cliente["telefono"]
            or texto.lower() in cliente["email"].lower()
        ):
            print(
                f"{cliente['nombre']} - "
                f"{cliente['telefono']} - "
                f"{cliente['email']}"
            )
            encontrado = True

    if not encontrado:
        print("No se encontraron clientes")