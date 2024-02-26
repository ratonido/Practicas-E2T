import os
import random
def creacion(bas):
    os.makedirs(bas)
    
    for i in range(4):
        creacion_carpeta= bas + '/' + str(i) 
        
        os.makedirs(creacion_carpeta)
        
        for j in range(1,5):
            extension=random.choice(['.txt','.doc','.xls','.csv'])
            archivo = creacion_carpeta + '/' + str(j) + extension 
            with open(archivo, 'w') as fichero:
                fichero.write('Esto es fichero'+ str(j) )
                
        
          
        
base='pruebas'
creacion(base)