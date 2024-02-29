import random
class premios: 
    def __init__(self,rondas):
        self.rondas=rondas
    
    puerta=['oveja','coche','nada']
    random.shuffle(puerta)
    seleccion=random.choice(puerta)
    print(seleccion)   ## se muestra la opción que elige el concursante
    puerta.remove(seleccion) 
    restante=puerta     # se asigna a una variable las dos puertas restantes
    print(restante)
    decision=[True,False]  # con un true o false se decide si se cambia o no de puerta y se asigna a una variable
    eleccion=random.choice(decision)
    print(eleccion)
    def participa(self):
        while self.rondas > 0:
            self.rondas-=1
                            
    
    def gana_pierde(self):  # se define un método para ver que ocurre dependiendo de la decision que tome el concursante
            
        while self.eleccion == True:          # con un bucle while se analiza los supuestos en los que el concursante 
                                                        #cambia de puerta
            if self.seleccion == 'coche':
                self.perdedor=print(self.seleccion,"\n Decidiste cambiar y tenias el coche,lo siento has perdido")
                        
                break
                        
            if self.seleccion != 'coche':
                self.ganador=ultima=random.choice(self.restante)
                if ultima == 'coche':
                        print(ultima,"\n Felicidades has ganado")
                        break
                            
                else:
                    self.perdedor=print(ultima,"\n lo siento has perdido")
                                
                break
                            
        while self.eleccion == False:  # con otro bucle while se analizan los supuestos en los que no cambia de puerta
                            
            if self.seleccion != 'coche':
                self.perdedor=print(self.seleccion,"\nLo siento has perdido")
                            
                break
                            
            if self.seleccion == 'coche':
                premio=self.seleccion
                ultima=random.choice(self.restante)     
                self.ganador=print(premio,"\nFelicidades has ganado")
                            
                break 
                
   
            
jugador1=premios(28)
jugador1.participa()
