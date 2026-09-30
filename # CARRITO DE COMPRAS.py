# CARRITO DE COMPRAS

articulos = []
precios = []
total = 0

print("Bienvenido al carrito de compras. Ingrese los artículos y sus precios. Escriba 'listo' para finalizar.")

while True:
    opcion = input("1 AGREGAR AL CARRITO \n 2 QUITAR DEL CARRITO \n 3 VER CARRITO \n 4 SALIR \n")

    if opcion == "1":
        while True:
            articulo = input("\nIngrese el nombre del artículo (o 'listo' para terminar): ")
            moneda = "$"
            if articulo.lower() == 'listo':
                break
            precio = float(input(f"Ingrese el precio de {articulo}: {moneda} "))
            articulos.append(articulo)
            precios.append(precio)
            total += precio
            print(f"{articulo} cuesta {precio} {moneda} y ha sido agregado al carrito.")

    elif opcion == "2":
        while True:
            if not articulos:
                print("El carrito está vacío.")
                break
            remover = input("\nIngrese el nombre del artículo a quitar (o 'listo' para terminar): ")
            if remover.lower() == 'listo':
                break
            
            if remover in articulos:
                posicion = articulos.index(remover)
                total -= precios[posicion]
                articulos.pop(posicion)
                precios.pop(posicion)
                
                print(f"'{remover}' ha sido removido del carrito.")
            else:
                print(f"'{remover}' no se encuentra en el carrito.")

    elif opcion == "3":
        if not articulos:
            print("El carrito está vacío.")
        else:
            print("Carrito:")
            for i in range(len(articulos)):
                print(f" {articulos[i]}: ${precios[i]}")
            print(f"\nTotal: ${total}")

    elif opcion == "4":
        print("Gracias por usar el carrito de compras.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
