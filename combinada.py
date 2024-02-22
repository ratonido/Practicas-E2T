    

def combi( lista1,lista2):
    nueva=[]
    for n in lista1:
        for j in lista2:
            nueva.append( str(n) + str(j) )

    return nueva
lista1=[1,4,3]
lista2=['a', 'b', 'c']

if __name__=='__main__':
    
       print(combi( lista1, lista2 ))
