import random

class puertas:
    
    def __init__(self,rondas):
        self.rondas=rondas
        self.stats=[0,0,0,0,0]

    
            
    def gana_pierde(self):  # se define un método para ver que ocurre dependiendo de la decision que tome el concursante
        while self.rondas >0:
            self.rondas-=1
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
            if self.rondas==0:
                print('El jugador ha perdido',self.stats[0],'cambiando de puerta',)
                print('El jugador ha perdido',self.stats[2],'sin cambiar de puerta')
                print('El jugador ha ganado',self.stats[1],'cambiando de puerta')
                print('El jugador ha ganado',self.stats[3],'sin cambiar de puerta')

            while eleccion == True:# con un bucle while se analiza los supuestos en los que el concursante 
                                                                
                            
                if seleccion == 'coche':
                    self.perdedor=print(seleccion,"\n Decidiste cambiar y tenias el coche,lo siento has perdido")   
                    self.stats[0]+=1
                    break
                                
                if seleccion != 'coche':
                    self.ganador=ultima=random.choice(restante)
                    self.stats[1]+=1
                    if ultima == 'coche':
                        print(ultima,"\n Felicidades has ganado")
                            
                        break
                                        
                    else:
                        self.perdedor=print(ultima,"\n lo siento has perdido")
                        self.stats[0]+=1
                                        
                    break
                                    
            while eleccion == False:  # con otro bucle while se analizan los supuestos en los que no cambia de puerta
                                    
                if seleccion != 'coche':
                    self.perdedor=print(seleccion,"\nLo siento has perdido")
                    self.stats[2]+=1
                    break
                                    
                if seleccion == 'coche':
                    premio=seleccion
                    ultima=random.choice(restante)
                    self.stats[3]+=1    
                    self.ganador=print(premio,"\nFelicidades has ganado")
                            
                    break 
        
            
                          
                
            
            
concurso1=puertas(30)
concurso1.gana_pierde()

# el código no funciona del todo bien en el conteo ya que no me dio tiempo a acbarlo
   
    
