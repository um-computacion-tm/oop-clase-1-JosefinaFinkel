

#modelo de clase profesor
class Profesor:
    #metodod dentro de una clase. constructor
    def __init__(self, el_nombre, el_email):
        self.nombre = el_nombre
        self.email = el_email
    #esto es un metodo de esta clase
    def dame_tu_nombre(self):
        return self.nombre




#modelo de clase alumno
class Alumno:
    def __init__(self, el_nombre_del_alumno):
        #atributos
        self.nombre = el_nombre_del_alumno
        self.inasistencias = 0 #cuando see crea, todos tienen inasistencia 0
        self.dieta = ""
        self.mentor = None
    
    def mentoria(self, profesor):
        self.mentor = Profesor

#estos son metodos dentro de la class alumno
    def falta(self):
        self.inasistencias += 1

    def elegir_dieta_especial(self, la_dieta):
        self.dieta = la_dieta
    
    def es_vegano(self):
        self.dieta = "vegano"

    def esta_libre(self):
        if self.inasistencias >= 5:
            return "Esta Libre"
        else:
            return "Ok"


#dentro de las clases, cada objeto toma un valor de la variable diferente.La variable "nombre", puede ser Elio o Gabi.
#como pusimos dos objetos, Elio y Gabi, Los parametros van a tomar los valores de Elio y de Gabi, dependiendo cual usemos.
#cada uno tiene su propio atributo nombre y su propio atributo Email.
        
#objetos CLASE PROFESOR.
#ambos objetos tienen estado.
profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu")


#print(profe_elio.dame_tu_nombre())
#print(profe_gabi.dame_tu_nombre())


#objetos clase almuno, 
alumno_juan = Alumno ("Juancito")
alumno_maria = Alumno ("Maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()

print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())
#juan falto 4 veces

#dieta
alumno_maria.elegir_dieta_especial("vegetariana")
print(alumno_maria.dieta)

alumno_juan.es_vegano()
print(alumno_juan.dieta)

#mentoria
alumno_juan.mentoria(profe_elio)
print(alumno_juan.mentor)
#te da como resuletaod el nombre del profesor, osea Elio


los_alumno = [alumno_juan, alumno_maria]


