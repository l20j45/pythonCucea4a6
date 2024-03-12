def calcularImpuesto(cantidadSinIva,porcentajeDeIva=21):
    iva = cantidadSinIva * (porcentajeDeIva*.01)
    return iva