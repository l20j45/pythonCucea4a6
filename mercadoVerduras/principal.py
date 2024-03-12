import funciones
import time

descuento = 0
total = 0
cantidadManzana = 1

while cantidadManzana != 0:
    funciones.borrarPantalla()
    print("Hola buenas tardes")
    opcion, nombreFruta = funciones.menu()
    # PARTE 1
    # PEDIR DATOS
    cantidadManzana = float(input(f'Dime la cantidad de {nombreFruta} vendidas: '))
    if cantidadManzana == 0:
        break
    precioManzana = float(input(f'Dime el precio de la {nombreFruta}: '))
    
    total = cantidadManzana * precioManzana
    # PARTE 2
    # CALCULAR DESCUENTO
    descuento = funciones.calcularDescuento(cantidadManzana,precioManzana)
    total = total - descuento
    # PARTE 3
    # MOSTRAR RESULTADOS
    print(f"Total: {total}" )
    time.sleep(5)