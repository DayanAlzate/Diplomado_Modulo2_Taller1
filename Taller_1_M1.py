# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:30:14 2022
@author: dayan alzate hernandez
Id:000502226
"""

    
# creamos 6 lista que contengan los datos de cada variable a, b,c,d,e,f
        
a=[1]
b=[2]
c=[3]
d=[4]
e=[5] 
f=[6]
#creamos 1 lista que contendra los valores de las listas ya creadas 
lista=[a,b,c,d,e,f]
           
           
#ecuacion 1
           
ecu1 = (lista[0][0]+(lista[1][0]/lista[2][0]))/(lista[3][0]+(lista[4][0]/lista[5][0]))
           
#ecuacion 2 
Ecu2 = lista[0][0]-(lista[1][0]/(lista[2][0]-lista[3][0]))
            
         
# variables actuales
ec1=ecu1
ec2=Ecu2 
print ("valores originales ")
print(ec1)
print(ec2)
           
#variables intercambiadas 
ecu1=ec2
Ecu2=ec1
          
print("valores actualizados")
print(ecu1)
print(Ecu2)
          
        
           
            
           
    
    
