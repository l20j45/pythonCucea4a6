import libreria
import os
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

borrarPantalla()
impuesto = libreria.calcularImpuesto(1000,16)
print(impuesto)