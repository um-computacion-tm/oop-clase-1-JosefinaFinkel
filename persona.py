
class Persona: 

#como poner un parametro como optativo = cuando le pongp un valor por defecto
#esto es una caja negra, no se puede ver lo que esta adentro

#parte publica, lo que se puede ver en todas pertes, llamada interface. Metodos
#parte oculta, caja negra 

    def __init__(self, nombre: str = "juan", apellido: str = "doe", dni: int = "123456"):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def mostrar_datos(self):
        print(f"Mis datos son snombres = (self.__nombre__)apellido = (self.__apellido__) documento = (self.__dni__)") 



