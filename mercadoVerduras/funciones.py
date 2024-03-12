import os

def calcularDescuento (cantidad,precio):
    if cantidad ==30 :
        print("Descuento especial")
        descuento = (cantidad * precio)*.2
        print(f"el descuento es de {descuento}")
    elif cantidad >= 10:
        print("Descuento normal")
        descuento = (cantidad * precio)*.1
        print(f"el descuento es de {descuento}")
    else :
        descuento = 0
        print("Gracias por pagar el precio completo")
    return descuento


def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        
def menu():
    print("""
    1.-manzanas
    2.-peras
    3.-uvas""")
    opcion = int(input("Ingresa tu opcion"))
    if opcion == 1 :
        nombreFruta = "manzana"
    elif opcion == 2 :
        nombreFruta = "peras"
    elif opcion == 3 :
        nombreFruta = "uvas"
    else :
        nombreFruta = ""
        print("valor no valido")
    return opcion , nombreFruta