
class network():
    def __init__ (self,net,mask):
        self.net=net
        self.mask=mask
        self.octetos_red=net.split(".")
        self.octetos_masc=mask.split(".")
        #Octetos de la dirección Ip introducida
        self.octr1=int(self.octetos_red[0])
        self.octr2=int(self.octetos_red[1])
        self.octr3=int(self.octetos_red[2])
        self.octr4=int(self.octetos_red[3])
      
        #octetos de la máscara introducida
        self.octm1=int(self.octetos_masc[0])
        self.octm2=int(self.octetos_masc[1])
        self.octm3=int(self.octetos_masc[2])
        self.octm4=int(self.octetos_masc[3])
        #self.msc.append(self.octr1,self.octr2,self.octr3,self.octr4)
        self.red=[self.octr1,self.octr2,self.octr3,self.octr4]
        self.broad=[self.octm1,self.octm2,self.octm3,self.octm4]
        
        #Calculo de la dir de red con suma binaria
        self.dir_red=[]
        for x in range(4):
            suma_red=(self.red[x]) & (self.broad[x])
            self.dir_red.append(suma_red)
               
        #Calculo de la direccion de broadcast con or    
        self.dir_broad=[]    
        for j in range(4):   
            suma_broad=self.red[j] | (~self.broad[j]&255)  
            self.dir_broad.append(suma_broad) 
    
        #Calculo del número de host para la red
        
        self.hosts=self.dir_broad[3]-self.dir_red[3]-2
            
        print("Para la dirección:",self.net,"la dirección de red es:",".".join(map(str,self.dir_red)))
        print("La dirección de broadcast es:",".".join(map(str,self.dir_broad)))
        print("El número de host para esta red es:",self.hosts)   
           
            
            
                   
                 

net=input("Introduce la dirección IP:")
mask=input("Introduce la máscara de red:")
direccion=network(net,mask) 





   


