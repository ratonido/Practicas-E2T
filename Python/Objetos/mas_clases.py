# crear una clase estudiantes y otra clase cursos y manjear ambo

class alumnos:
    

    def __init__(self,nombre,apellidos,dni,edad):
        self.nombre=nombre
        self.apellido=apellidos
        self.dni=dni
        self.edad=edad 
        self.listado=[]
        
    
    def agrega_alumnos(self):
        self.listado.append(self.nombre)
        return self.listado
        
    def ver_alumnos(self):
        for i in range(len(self.listado)):
            self.nombre[i]
        print(self.nombre)
                
class cursos:
    
    def __init__(self,nombre): 
        self.nombre_curso=nombre
        self.lista_curso=[]
    
          
    def agrega_curso(self):
        self.lista_curso.append(self.nombre_curso)
        
        
        
    
  
    def ver_cursos(self):
        for i in range(len(self.lista_curso)) :
            self.lista_curso[i]
        print(self.lista_curso)
    
    
    """ def agrega_alumnos(self):
    self.agregado=[]
    for i in (alumnos.listado):
        for j in range(len(self.lista_curso)):
                self.agregado=alumnos.listado[i:0],self."""

while True: 
    print("""Selecciona una de las siguientes  opciones
1.Agregar estudiante
2.Agregar curso
3.Ver cursos
4.Ver estudiantes
5.Inscribir alumno en un curso
6.Ver alumnos de un curso
7.Salir""")
    Inscripcion=int(input("Selecciona una de las opciones"))
    if Inscripcion == 7:
        inscripcion=False
        break

    if Inscripcion ==1:
        nom=input("Introduce el nombre")
        ap=("Introduce el apellido")
        dni=input("introduce el dni")
        ed=input("introduce la edad")
        estudiante=alumnos(nom,ap,dni,ed)
        alumnos.
    elif Inscripcion ==2:
        curs=input("Introduce el nombre el curso")
        curso=cursos(curs)
        cursos.agrega_curso(curso)
        
        
        
            
    elif Inscripcion == 3:
        print(curso.ver_cursos())
                
    elif Inscripcion == 4:
        print(alumnos.ver_alumnos(estudiante))
        
        
        
        
        
        
    
    

            
            
        
      
    



     
  
 
    
 

  






    


        
#ver cursos
#ver estudiantes
#agregar curso
#agregar estudiante
#inscribir alumno en curso
#ver estudiantes cursos
#finalizar
"""
def alumno(nombre,apellidos,dni,edad):
    for x in range(4):
        inscripciones=[nombre,apellidos,dni,edad]       
        
def curso(nombre_curso):
    Curso=nombre_curso
    return Curso        
         
   alm=input("Introduce el nombre del alumno")
    ap=input("Introduce el apellido del alumno")
    dni=input("Introduce el dni del alumno")
    ed=input("Introduce la edad del alumno")
    
"""


