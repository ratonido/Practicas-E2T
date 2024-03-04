class network():
    def __init__ (self,net,mask):
        self.net=net
        self.mask=mask
    
    def masc_ip(self):
        self.oct1=self.net[0:3]
        self.oct2=self.net[5:7]
        self.oct3=self.net[9:11]
        self.oct4=self.net[13:15]
        print()
        
            
            
            
            
        
            
                   
            
    

    
  
net=str(input("Introduce la dicrección IP"))
mask=str(input("Introduce la máscara de red"))
direccion=network(net,mask) 
direccion.masc_ip()

    
    
    
    
    