import mysql.connector
def dbConnection():
        conexion = mysql.connector.connect(
        host="148.202.39.38",  # Cambia esto al host de tu base de datos MySQL
        user="test",    # Cambia esto al nombre de usuario de tu base de datos
        password="test",  # Cambia esto a la contraseña de tu base de datos
        database="mercadocucea"  # Cambia esto al nombre de tu base de datos
    )
        
        return conexion
def dbClose(cursor,conexion):
    cursor.close()
    conexion.close()