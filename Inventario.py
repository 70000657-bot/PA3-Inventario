inventario = {}

while True:
    print("\nSISTEMA DE INVENTARIO")
    print("1. Agregar Producto")
    print("2. Ver Inventario")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario[nombre] = [cantidad, precio]
        print("Producto agregado.")

    elif opcion == "2":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\nLista de Productos:")
            for nombre, datos in inventario.items():
                print(f"Producto: {nombre} | Stock: {datos[0]} | Precio: S/. {datos[1]}")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")
