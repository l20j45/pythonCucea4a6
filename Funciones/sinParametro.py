
nombre = "Rafa" #Contexto global
def mostrarUsuario(variable1,variable2):#contexto local
    print(SuperDuperVariable)
    print("Hola mundo")

def noMostrarUsuario(SuperDuperVariable):#contexto local
    print(SuperDuperVariable)
    print("Adios mundo")
    SuperDuperVariable ="Giovanni"
    mostrarUsuario(SuperDuperVariable)


mostrarUsuario('Solaire')
noMostrarUsuario(nombre)
print(nombre)