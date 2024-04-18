from logger_base import log

class Persona():
    def __init__(self,idpersona=None,nombre=None,apellido=None,email=None):
        self._idpersona=idpersona
        self._nombre=nombre
        self._apellido=apellido
        self._email=email
    @property
    def idpersona(self):
        return self._idpersona
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,value):
        self._nombre=value
        
    @property
    def apellido(self):
       return self._apellido
    @apellido.setter
    def apellido(self,value):
        self._apellido=value
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        self._email=value
    
    def __str__(self) -> str:
        return f'Persona: idpersona: {self._idpersona}, nombre: {self._nombre} , apellido: {self._apellido}, email: {self._email}'
    
if __name__ == '__main__':
    persona1 = Persona(1,'danie','rojas','daniel@gmail.com')
    log.debug(persona1)
    persona2 = Persona(nombre='victor',apellido='garcia',email='asd.com')
    log.debug(persona2)