#Objetos

#Defino con la sentencia class y el nombre, generalmente la primera en mayúscula
class Militar:    
    pais="España"   #Atributos de clase: nuestro objeto puede tener valores comunes a toda la clase Atributos de instancia. Palabras mágicas self e init.Self hace referencia a
                    # las variables del propio objeto

    
    def __init__(self,nombre,apellidos,edad):
        self.nombre= nombre
        self.apellido=apellidos
        self.edad=edad
        print("se ha creado el militar", self.nombre,apellidos,edad,"en",self.pais)
        
    def desfila(self):
        print("Ahora",self.nombre,"está desfilando")
    
    def flexiones(self,cuantas):
        print("Ahora",self.nombre,"está haciendo",cuantas,"flexiones")
        

    @classmethod        # Cuando modificamos cosas de la clase creada
    def cambia_pais(cls,nuevo): 
        cls.pais=nuevo
        
    def cumple(self):
        self.edad+=1
        print(self.nombre, "ha cumplido",self.edad,'años' )
        
    def nacimiento(self):
        print("El año de nacimiento de",self.nombre,'es',2024-self.edad)
    @staticmethod           #Decorador, cuando no necesita atributos de la clase ni de la instancia
    
    def frase(variable):
        print('Dime algo' + variable)
    

manuel=Militar('Manuel','Raton',30)
jorge=Militar('Jorge','gomez',20)

jorge.cumple()
manuel.cumple()
jorge.nacimiento()
manuel.nacimiento()

