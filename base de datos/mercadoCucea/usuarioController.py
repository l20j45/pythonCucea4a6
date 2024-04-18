import mysql.connector
import usuarioModel
from utils import connector

def extraeUsuarios():
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = []
    resultados = cursor.fetchall()
    for fila in resultados:
        usuario = usuarioModel.asignarDatos(fila)
        usuarios.append(usuario)
    return usuarios

def extraeUsuario(codigo):
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    cursor.execute(f"SElECT * FROM usuario WHERE id_usuario = {codigo}")
    usuarios = []
    resultados = cursor.fetchone()
    usuario = usuarioModel.asignarDatos(resultados)
    cursor.close()
    conexion.close()
    return usuario

def borrarUsuario(codigo):
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM usuario WHERE id_usuario = {codigo}")
    print(cursor.rowcount)
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarUsuario(usuario):
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO `mercadocucea`.`usuario` (`usuario`, `contrasenia`, `correo`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `puesto`, `telefono`) VALUES ('{usuario['usuario']}','', '{usuario['correo']}', '{usuario['nombre']}', '{usuario['apellidoPaterno']}', '{usuario['apellidoMaterno']}', '{usuario['puesto']}', '{usuario['telefono']}');")
    print(cursor.rowcount)
    conexion.commit()
    cursor.close()
    conexion.close()

usuarioAgregar = usuarioModel.usuario
usuarioAgregar['usuario']='test'
usuarioAgregar['correo']='test'
usuarioAgregar['nombre']='test'
usuarioAgregar['apellidoPaterno']='test'
usuarioAgregar['apellidoMaterno']='test'
usuarioAgregar['puesto']='test'
usuarioAgregar['telefono']='test'

agregarUsuario(usuarioAgregar)


