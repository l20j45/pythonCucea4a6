usuario = {
    'id_usuario':'',
    'usuario':'',
    'correo':'',
    'nombre':'',
    'apellidoPaterno':'',
    'apellidoMaterno':'',
    'puesto':'',
    'telefono':''
}

def asignarDatos (data):
        usuario['id_usuario']=data[0]
        usuario['usuario']=data[1]
        usuario['correo']=data[3]
        usuario['nombre']=data[4]
        usuario['apellidoPaterno']=data[5]
        usuario['apellidoMaterno']=data[6]
        usuario['puesto']=data[7]
        usuario['telefono']=data[8]
        return usuario