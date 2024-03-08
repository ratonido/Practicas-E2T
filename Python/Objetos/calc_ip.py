
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
        #self.octetos=[]
        #self.octetos.insert(self.octr1,self.octr2,self.octr3,self.octr4)
        #octetos de la máscara introducida
        self.octm1=int(self.octetos_masc[0])
        self.octm2=int(self.octetos_masc[1])
        self.octm3=int(self.octetos_masc[2])
        self.octm4=int(self.octetos_masc[3])
        #self.msc=[]
        #self.msc.append(self.octr1,self.octr2,self.octr3,self.octr4)
        self.dir_red=[]
        self.dir_broad=[]
    def red(self):
        for i in range(4):
            self.dir_red.append(str(int(self.octr1[1]))) & str(int(self.octm1[1]))
            print(self.dir_red)
            
        
        
        
        

net=input("Introduce la dirección IP""")
mask=input("Introduce la máscara de red""")
direccion=network(net,mask) 
direccion.red()



   


