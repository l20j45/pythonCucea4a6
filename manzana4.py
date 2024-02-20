descuento = 0
total = 0
cantidadManzana = 1
cantidadManzana = float(input('Dime la cantidad de manzanas vendidas: '))
while cantidadManzana != 0:
    precioManzana = float(input('Dime el precio de la manzana: '))
    print("Hola buenas tardes")
    total = cantidadManzana * precioManzana
    if cantidadManzana ==30 :
        print("Descuento especial")
        descuento = (cantidadManzana * precioManzana)*.2
        print(f"el descuento es de {descuento}")
        total = total - descuento
    elif cantidadManzana >= 10:
        print("Descuento normal")
        descuento = (cantidadManzana * precioManzana)*.1
        print(f"el descuento es de {descuento}")
        total = total - descuento
    else :
        print("Gracias por pagar el precio completo")
    print(f"Total: {total}" )
    cantidadManzana = float(input('Dime la cantidad de manzanas vendidas: '))