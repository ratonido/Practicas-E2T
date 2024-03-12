class persona:
    
    
    def __init__(self,nombre,apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
        
    def saludar(self):
        print("hola"+ " "+ self.nombre +" "+ self.apellidos)
        
        
        
        
        
class estudiante(persona):
    def __init__(self, nombre, apellidos,edad=20):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
    def despedirse(self):
        print("Adios",self.nombre,self.apellidos,self.edad)
        
maria=estudiante("Maria","Navarro",27)
kerry=estudiante("Kerry","kaverga",20)
maria.saludar()



    