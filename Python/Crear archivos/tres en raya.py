def tictoe():
    almacen=[
        ["_","_","_"],
        ["_","_","_"],
        [" "," "," "],        
    ]
    
    
    return " A B C \n" + \
            "1" + almacen[0][0] + "|" + almacen[0][1] + "|" + almacen[0][2]+"\n" + \
            "2" + almacen[1][0] + "|" + almacen [1][1] + "|" + almacen [1][2] + "\n" + \
            "3" + almacen[2][0] + "|" + almacen [2][1] + "|" +almacen [2][2]
            
        
jugada=input("Dime la posicion en la que quieres jugar")
resultado= tictoe()
print(resultado)
