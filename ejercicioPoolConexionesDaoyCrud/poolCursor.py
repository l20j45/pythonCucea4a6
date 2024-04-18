from logger_base import log
from ConexionPool import ConexionPool

class poolCursor:
    def __init__(self):
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = ConexionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuto metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}  ')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')
        self._cursor.close()
        ConexionPool.liberarConexion(self._conexion)
        
if __name__ == '__main__':
    with poolCursor() as cursor:
        log.debug(f'dentro del bloque with')
        cursor.execute('SELECT * from persona')
        log.debug(cursor.fetchall())
        
        