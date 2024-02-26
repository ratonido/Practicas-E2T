""" Tipos de datos 
+ Enteros
+ Textos
+ Decimales
+ Booleanos

"""

"""
Estructuras de datos:
Listas
Tuplas: si se quiere recorrer los valores es más rápido que la lista
Sets: igual que los diccionarios per¡o sólo con claves
Diccionarios: Se puede recorrer tanto valores como claves
    
    
"""

booleano=True
booleano2 = False

if booleano == 1:
    print("ok")
    
"""Operador 'and' se ejecuta cuando los dos operandos son True.
Operador 'or' se ejecuta cuando uno de los dos operandos es True.
Operador 'not' se utiliza como inversor o negación.
Operador 'in' 'not in', podemos ver si un iterable se encuentra en una secuencia
Operador 'is' 'is not', comparan objetos. Tienen que ser iguales (además de su valor) 
"""

X=1 
y=2
x=y
y=X

print(x,y)


"""
Asignación múltiple. Se asigna valñores a las variables  sin necesidad de declara una por una
"""
x, y = y, x

print(x,y)

lista=[1, 2, 3]
x, y, z=lista

print(x, y, z)



"""
Comprobación de errores

Se utiliza 'try' y 'except'. si escreibimos try siempre tendrá que llevar un except.
       
"""

try:
    int("ba")
except ValueError and TypeError:
    print("no se puede")
except:
    print("Cualquier otro error")
    
    


try:
    numero=int( input("introduce un numero") )
    
except ValueError:
    
    print("Eso que has puesto no es un numero")
    