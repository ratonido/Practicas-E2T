"""import random

def generado_lista(cuantos,inicio,fin):
    lista=[]
    for n in range (cuantos):
        lista.append(int(inicio + random.random()*(fin-inicio) ) )
    return lista

print(generado_lista(50,60,90))



# Realiza una función que sume todos los elementos de una lista.

print(sum(generado_lista(50,60,90)))
"""
# Realice una función, que cree una lista a partir de otras dos.
        # El resultado será la combinación de cada elemento de una lista con el de la otra
        # ejemplo: lista1 =['j', 'q'] lista2=[1,2] , resultado =['j1', 'q1', 'j2', 'q2']
"""  

def combinada( lista1,lista2):
    nueva=[]
    for n in lista1:
        for j in lista2:
            nueva.append( str(n) + str(j) )

    return nueva
lista1=[1,4,3]
lista2=['a', 'b', 'c']
       
print(combinada( lista1, lista2 ))
"""""


# Ejercicio
# Realice una función que inserte un elemento dado ANTES de cada elemento de una lista
# Ejemplo: lista=['j', 'q'] elem=[1] , resultado = ['1j', '1q']

"""
def inserta(lista):
    comb=[]
    elem=1
    for n in lista:
        comb.append( str(elem)+ str(n)  )
    return comb
    
lista=['j','q']
print(inserta (lista) )
"""


# Ejercicio
# Realice una función que corte una lista cada x elementos dados, generando
# una nueva lista, donde cada elemento es una lista del corte.
# Ejemplo lista=['1','2','3','4','5','6','7','8','9','0'] corte=3
# resultado = [ ['1','2','3'] , ['4','5','6'] , ['7','8','9'] , ['0']]
"""
def cortada(listado,corte):
    nueva=[]
    inicio=0
    fin=0
    for n in range( (len(listado) // corte ) + 1):
        fin=inicio + corte
        nueva.append(listado[inicio:fin])
        inicio=fin    
    return nueva    
    
lista=[99,85,37,54,27,6,105,45,9,0]
cortar=3

print(cortada(lista,cortar))


"""

# Ejercicio
# Realice una función, que busque en una lista todos los números mayores de
# un número dado por el usuario (input). 
# Devolverá con un print, cuales son esos elementos, cuantos y 
# cuanto suman entre ellos.
# Ejemplo: lista=[1,2,3,4,5,6,7,8,9,10] numero = 4
# resultado 5, 6, 7, 8, 9, 10 - total: 6 - suma total: 45
"""
def mayores(lista,numero):
    superiores=[]
    
    for n in lista:
        if n> numero:
            superiores.append(n)
                       
    #return superiores,total
    print(superiores,len(superiores),'total:', sum(superiores))
    
        
numero=int(input("Introduce un número entre el 1 y el 10"))
lista=[1,2,3,4,5,6,7,8,9,10]

mayores(lista,numero)

"""
#Ejercicio máquina bitcoin


importe=float( input( "Introduce el importe a cambiar") )


billetes={500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 0.5:0,0.2:0,0.1:0,00.5:0,0.01:0}

for n in billetes:
    cambiar=importe//n
    billetes[n] =cambiar
    importe=importe - (cambiar * n) 
    
print(billetes)
    
    
    
    
    


    
        

    
        








