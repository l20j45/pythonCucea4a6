globalnumero1 = 2 
globalnumero2 = 2 

def suma(numero1, numero2):
    #print(numero1 + numero2)
    total = numero1 + numero2
    print("estoy imprimiendo en una funcion")
    return total

def multiplicacion(numero1, numero2):
    #print(numero1 * numero2)
    total = numero1 * numero2
    print("estoy imprimiendo en una funcion")
    return total
    
totalFuncion = suma(globalnumero1,globalnumero2)
print(totalFuncion)
totalFuncion = multiplicacion(globalnumero1,globalnumero2)
print(totalFuncion)

# suma(10,15)
