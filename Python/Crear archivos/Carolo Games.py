# Concurso con 3 puertas, detrás de las puertas hay una oveja, detrás de la otra un coche y la otra nada
# el programa asigna automáticamente la oveja y el coche a cada una de las puertas 
# Una vez que elige la puerta, el programa  abre una de las otras dos y le da la opción de cambiar
#estadística de las personas que cambiaron de puerta y al elegir cuales ganaron y cuales perdieron



import random
class puerta:
    
    def __init__(self,puertas):   
        premios=['oveja','coche','nada']
        self.premios=puertas
        random.shuffle(premios)
    def eliminar(self):
        elegir=random.choices([self.premios])
        print(elegir)
        if elegir == 'coche':
            self.premios=['oveja','nada']
        elif elegir =='nada':
            self.premios=['coche','oveja']
        else:
            self.premios=['coche','nada']
        
            print(self.premios)
            
            
        
            
         
   
       
        
puerta1=puerta() 
puerta1.eliminar('oveja')   
  



                
 
    

        
        
 
        
                        
        
        



