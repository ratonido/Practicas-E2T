#Objetos

#Defino con la sentencia class y el nombre, generalmente la primera en mayúscula
class Militar:            
                # en esta parte puedo definir propiedades pero es mejor hacerlo en el init o iniciador
    def __init__(self,nombre,apellidos,edad): # Constructor(def __init__).Palabras mágicas self e init.
                                              # Self hace referencia a las variables del propio objeto
        self.nombre= nombre
        self.apellido=apellidos
        self.edad=edad
        print("se ha creado el militar", self.nombre,apellidos,edad,"en",self.pais)
        
    def desfila(self):          # creamos un método. es igual que una función pero la diferencia es que el método pertenece a un objeto.
        print("Ahora",self.nombre,"está desfilando")
    
    def flexiones(self,cuantas):
        print("Ahora",self.nombre,"está haciendo",cuantas,"flexiones")
        

    @classmethod        # Cuando modificamos cosas de la clase creada, como hacer uso de una clase dentro de una misma clase y crear
                        #otro objeto con las propiedades que le defina dentro del metodo 
    def cambia_pais(cls,nuevo): # Con classmethod se usa cls en lugar de self
        cls.pais=nuevo
        
    def cumple(self):
        self.edad+=1
        print(self.nombre, "ha cumplido",self.edad,'años' )
        
    def nacimiento(self):
        print("El año de nacimiento de",self.nombre,'es',2024-self.edad)
    @staticmethod           # Decorador, cuando no necesita atributos de la clase ni de la instancia
    
    def frase(variable):
        variable='hola'
        print('Dime algo' + variable)
    

manuel=Militar('Manuel','Raton',30) #se le da nombre al objeto junto con el nombre de la clase a la que pertenece
jorge=Militar('Jorge','gomez',20)

jorge.cumple() # Con esta llamada al método, cambiará el valor de la propiedad definida en la clase
manuel.cumple()
jorge.nacimiento()
manuel.nacimiento()

