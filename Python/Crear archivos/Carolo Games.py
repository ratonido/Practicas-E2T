# Concurso con 3 puertas, detrás de las puertas hay una oveja, detrás de la otra un coche y la otra nada
# el programa asigna automáticamente la oveja y el coche a cada una de las puertas 
# Una vez que elige la puerta, el programa  abre una de las otras dos y le da la opción de cambiar
#estadística de las personas que cambiaron de puerta y al elegir cuales ganaron y cuales perdieron



import random
        
puerta=['oveja','coche','nada']
random.shuffle(puerta)
seleccion=random.choice(puerta)
print(seleccion)
puerta.remove(seleccion)
restante=puerta
print(restante)
decision=[True,False]
eleccion=random.choice(decision)
print(eleccion)
def gana_pierde(eleccion):
    
    while eleccion == True:
        
        if seleccion == 'coche':
            premio=seleccion
            random.choice(restante)
            print(premio,"\nFelicidades has ganado")
            break
        
        if seleccion != 'coche':
            ultima=random.choice(restante)
            if ultima == 'coche':
                print(ultima,"\n Felicidades has ganado")
                break
            else:
                print(ultima,"\n lo siento has perdido")
                break
    while eleccion == False:
        
        if seleccion != 'coche':
            print(seleccion,"\n lo siento has perdido")
            
            break
        
        if seleccion == 'coche':
            premio=seleccion
            random.choice(restante)     
            print(premio,"\nFelicidades has ganado")
            break 

gana_pierde(eleccion)        


                
 
    

        
        
 
        
                        
        
        



