# crear una clase estudiantes y otra clase cursos y manjear ambo

class alumnos:
    listado_alumnos=[]
    listado_nombres=[]
    
    def __init__(self,nombre,apellidos,dni,edad):
        self.apellido=apellidos
        self.nombre=nombre
        self.dni=dni
        self.edad=edad 
        
    @classmethod
    def agrega_alumnos(cls, alumno_a_agregar):
        cls.listado_alumnos.append(alumno_a_agregar)
        
    @classmethod
    def ver_alumnos(cls):
        for x in cls.listado_alumnos:
            print(x.nombre)
        
                
class cursos:
    lista_cursos=[]
    asignados=[]
    
    
    def __init__(self,nombre): 
        self.nombre_curso=nombre
        

    
    @classmethod     
    def agrega_curso(cls,curso_a_agregar):
        cls.lista_cursos.append(curso_a_agregar)
        
    @classmethod    
    def ver_cursos(cls):
        for i in cls.lista_cursos:
            print(i.nombre_curso)
    
    @classmethod
    def seleccionar(cls):
        for i in alumnos.listado_nombres:
            for j in cursos.lista_cursos:
                cls.       
            
    
                
            
                
        
    
    @staticmethod
    def ver_asigandos(cls):
        for i in cls.asignados:
            print(i)
            

                

    
    
    
   
       
                
    

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
        Inscripcion = False
        break

    if Inscripcion == 1:
        
        nom = input("Introduce el nombre")
        ap = input("Introduce el apellido")
        dni = input("introduce el dni")
        ed = input("introduce la edad")
        alumnos.agrega_alumnos(alumnos(nom,ap,dni,ed))
       
                
    elif Inscripcion == 2:
        nomb=input("Introduce el nombre del curso")
        cursos.agrega_curso(cursos(nomb))
                    
    elif Inscripcion == 3:
        cursos.ver_cursos()
                
    elif Inscripcion == 4:
        alumnos.ver_alumnos()
        
    elif Inscripcion == 5:
        alum=input("selecciona un alumno")
        curs=input("selecciona un curso")
        cursos.agregar(alumnos.listado_nombres)
        
    elif Inscripcion == 6:
        cursos.asignados()
                
                
    
    
    
    
      
        
        
        
        
        
        
    
  
        
        
        
        
        
        
        
        
        
    
    

            
            
        
      
    



     
  
 
    
 

  






    


        
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


