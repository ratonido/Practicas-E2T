"""
class network():
    def __init__ (self,net,mask):
        self.net=net
        self.mask=mask
    
    def red_ip(self):
        self.oct1=bin(int(net[0:3]))
        self.oct2=bin(int(net[4:7]))
        self.oct3=bin(int(net[8:11]))
        self.oct4=bin(int(net[12:15]))
        self.mask1=bin(int(mask[0:3]))
        self.mask2=bin(int(mask[4:7]))
        self.mask3=bin(int(mask[8:11]))
        self.mask4=bin(int(mask[12:15]))         
        
            
               
            
    

    
  
net=str(input("Introduce la dirección IP con octetos completos"))
mask=str(input("Introduce la máscara de red"))
direccion=network(net,mask) 
direccion.red_ip()
"""

   
 
    
    




net=input("Introduce la dirección de red")
red=net.split(".")
mask=input("Introduce la máscara de red")
mascara=mask.split(".")

def ipsub(r,m):
    
    
    

#mask=input("Introduce la máscara")

#ipred(red)