descuento = 0
total = 0
cantidadManzana = 1

print("Hola buenas tardes")

while cantidadManzana != 0:
    cantidadManzana = float(input('Dime la cantidad de manzanas vendidas: '))
    if cantidadManzana == 0:
        break
    precioManzana = float(input('Dime el precio de la manzana: '))
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


