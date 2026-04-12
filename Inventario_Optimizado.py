from typing import Dict, List


class GestorInventario:
    """
    Clase que centraliza la lógica de negocio del inventario.
    Aplica el principio de Responsabilidad Única (SoC) - Clean Code.
    """

    def __init__(self):
        # Uso de Type Hints para definir la estructura del diccionario
        self.productos: Dict[str, List[float]] = {}

    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> None:
        """Registra un nuevo producto en el inventario."""
        self.productos[nombre] = [float(cantidad), precio]

    def obtener_inventario(self) -> Dict[str, List[float]]:
        """Retorna el diccionario completo de productos."""
        return self.productos


def ejecutar_registro(gestor: GestorInventario) -> None:
    """
    Función modular para la entrada de datos.
    Implementa robustez mediante manejo de excepciones.
    Incluye validación de consistencia en el nombre (IA Generativa).
    """
    nombre = input("Nombre del producto: ").strip()

    if not nombre:
        print("Error: El nombre del producto no puede estar vacío.")
        return

    if not nombre.replace(" ", "").isalpha():
        print("Error: El nombre solo debe contener letras y espacios.")
        return

    try:
        # Bloque try-except para evitar colapsos por datos no numéricos
        cantidad = int(input("Cantidad en stock: "))
        precio = float(input("Precio unitario: "))

        # Validación de lógica de negocio: valores positivos
        if cantidad < 0 or precio < 0:
            print("Error: El stock y el precio no pueden ser valores negativos.")
        else:
            gestor.agregar_producto(nombre, cantidad, precio)
            print(f"Éxito: Producto '{nombre}' registrado correctamente.")

    except ValueError:
        # Captura de error de tipo para estabilidad del sistema
        print("Error: Debe ingresar valores numéricos válidos para stock y precio.")


def mostrar_inventario(gestor: GestorInventario) -> None:
    """Muestra los productos registrados con formato de moneda."""
    items = gestor.obtener_inventario()

    if not items:
        print("\nEl inventario está actualmente vacío.")
    else:
        print("\n" + "=" * 20)
        print(" REPORTE DE STOCK")
        print("=" * 20)
        for nombre, datos in items.items():
            # Formato de salida para legibilidad - Clean Code (Estilo)
            print(f"- {nombre}: {int(datos[0])} unidades | S/. {datos[1]:.2f}")


def main():
    """
    Punto de entrada principal.
    Controla el flujo de la aplicación aplicando
    metodologías ágiles (Iteración funcional).
    """
    gestor = GestorInventario()

    while True:
        print("\nSISTEMA DE INVENTARIO OPTIMIZADO")
        print("1. Registrar Producto")
        print("2. Ver Inventario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_registro(gestor)
        elif opcion == "2":
            mostrar_inventario(gestor)
        elif opcion == "3":
            print("Saliendo del sistema... Gracias.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
