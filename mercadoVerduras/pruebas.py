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

nombreFruta = menu()
print(nombreFruta)