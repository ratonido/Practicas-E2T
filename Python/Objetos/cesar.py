"""Construir una clase para hacer cifrado cesar
el cifrado cesar funciona por desplazamiento, es decir

si nuestro cifrado tiene desplazamiento 3, desplaza 3 posiciones la letra

una A se convertiria en D (A->D)

para descifrar con desplazamiento 3, la D se convertiría en A

cuando tenemos un texto, podemos acceder a las letras de cada una de sus posiciones

variable = "HOLA"
variable[0] = "H"
variable[1] = "0"

podemos crear nuestro conversor
conversor = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmñopqrstuvwxyz0123456789-_.,:;*-+"

Si uso conversor.find("B") me devuelve la posicion de esa letra
Si uso conversor[4] me devuelve la letra en esa posición

- Construir con Programación Orientada a Objetos, una clase que realice cifrado cesar
- Para instanciar la clase, le diré el desplazamiento a usar
- Tendré una función para descifrar, otra para descifrar y otra para cambiar el desplazamiento
"""


  

class cifrado:    
    
    diccionario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmñopqrstuvwxyz0123456789-_.,:;*-+"
    
def __init__(self,desplazamiento):
    self.desplazamiento = desplazamiento
        
    def cifrado(self,texto):
        for i in texto:
            
            
        
    
 
     
        

 
            
        
        
        
        
        
     
        
       
        

