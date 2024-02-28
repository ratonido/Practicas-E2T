import random

class jugador:
    
    def __init__(self,nombre):
       self.nombre=nombre 
        
    puerta=['oveja','coche','nada']
    random.shuffle(puerta)
    seleccion=random.choice(puerta)
    print(seleccion)   ## se muestra la opción que elige el concursante
    puerta.remove(seleccion) 
    restante=puerta     # se asignan a una variable las dos puertas restantes
    print(restante)
    decision=[True,False]  # con un true o false se decide si se cambia o no de puerta y se asigna a una variable
    eleccion=random.choice(decision)
    print(eleccion)
        
    def gana_pierde(self):
    
        while self.eleccion == True:          # con un bucle while se analiza los supuestos en los que el concursante 
                                              #cambia de puerta
                
            if self.seleccion == 'coche':
                premio=self.seleccion
                random.choice(self.restante)
                print(premio,"\nFelicidades has ganado")
                break
                
            if self.seleccion != 'coche':
                ultima=random.choice(self.restante)
                if ultima == 'coche':
                    print(ultima,"\n Felicidades has ganado")
                    break
                else:
                    print(ultima,"\n lo siento has perdido")
                    break
                
        while self.eleccion == False:  # con otro bucle while se analizan los supuestos en los que no cambia de puerta
                
            if self.seleccion != 'coche':
                print(self.seleccion,"\n lo siento has perdido")
                break
                
            if self.seleccion == 'coche':
                premio=self.seleccion
                random.choice(self.restante)     
                print(premio,"\nFelicidades has ganado")
                break 
        

jugador1=jugador('manuel')
jugador1.gana_pierde()
    
          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
