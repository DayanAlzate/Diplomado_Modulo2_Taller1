# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:30:14 2022
@author: user
"""
class ecuacion():
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    def ecuacion1(self):
        
        ecu1 = (self.a+(self.b/self.c))/(self.d+(self.e/self.f))
        return ecu1
    
    def ecuacion2(self):
        
        ecu2 = self.a-(self.b/(self.c-self.d))
        return ecu2
    
    
    
    
 

     
objeto= ecuacion()
print(objeto.ecuacion1())
print (objeto.ecuacion2())


