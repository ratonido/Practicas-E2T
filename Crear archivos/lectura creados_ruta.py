import os

directorio=os.listdir('pruebas')
diccionario={'doc':0,'txt':0,'csv':0,'xls':0}


for i in directorio:
    actual=os.listdir('pruebas/'+ str(i))
    for j in actual:
        extension=j[(len(j)-3):]
        diccionario[extension] = diccionario[extension]+1


print(diccionario,"Total de archivos", sum(diccionario.values()))
        
        
