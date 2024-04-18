from Persona import *
from Conexion import *

class PersonaDAO:
    """DAO (DATA ACCESS OBJECT) """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _SELECCIONARESPECIFICO = 'SELECT * FROM persona where id_persona=%s ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona set nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personaslist = []
                for registro in registros:
                    persona1 = Persona(registro[0], registro[1], registro[2], registro[3])
                    personaslist.append(persona1)
                return personaslist
    
    @classmethod
    def seleccionarEspecifico(cls,id_persona):
        cursor = Conexion.obtenerCursor()
        cursor.execute(cls._SELECCIONARESPECIFICO,id_persona)
        registros = cursor.fetchone()
        return registros
    
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
            #with Conexion.obtenerCursor() as cursor:
                log.debug(f'Persona a insertar {persona}')
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertada {persona}')
                return cursor.rowcount 
            
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                    personaBuscada =  PersonaDAO.seleccionarEspecifico(persona.id_persona)
                    log.debug(f'Persona a modificar {personaBuscada}')
                    valores = (persona.nombre,persona.apellido,persona.email,persona.idpersona)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    log.debug(f'Persona a modificar {PersonaDAO.seleccionarEspecifico(persona.id_persona)}')
                    return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                    personaBuscada =  PersonaDAO.seleccionarEspecifico(persona.idpersona)
                    log.debug(f'Persona a borrar {personaBuscada}')
                    cursor.execute(cls._ELIMINAR, persona.idpersona)
                    return cursor.rowcount
                
if __name__ == '__main__':
    
    # Insertar un registro
    """     persona1 = Persona(nombre='rubi',apellido='sandoval',email='rsandoval@gmail.com')
    personas_Insertar= PersonaDAO.insertar(persona1)
    log.debug(f'Persona a insertada {personas_Insertar}') """
    
    # devolver registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    
    #eliminar registros
    persona1=Persona(idpersona='2')
    persona_Borrada= PersonaDAO.eliminar(persona1)
    log.debug(f'Persona a borrada {persona_Borrada}')
    
    # devolver registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    
    # Modificar registros
"""     id_persona = 1
    persona2 = Persona(id_persona = 1,nombre='riot',apellido='valdovino',email='mvald@gmail.com')
    personas_Modificadas = PersonaDAO.actualizar(persona2)
    log.debug(f'Persona a modificar {personas_Modificadas}') """