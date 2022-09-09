# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:10:14 2020

@author: EFE
"""
abeced=["a","b","c","d","e","f","g","h","i",
        "j","k","l","m","n","o","p","q","r","s",
        "t","u","v","w","x","y","z"]
ingreso="Ingrese cuantos numeros aleatorios desea obtener = "
a=[1,3,2]
b=[4,5,6]
def abecedario(lista):
    i=0
    while i<len(lista):
        if i%3==0:
            del lista[i]
        
        i=i+1   
    return lista

def producto_escalar(vector1,vector2):
    i=0
    s=0
    while i<len(vector1):
        s=s+vector1[i]*vector2[i]
        i=i+1
    return s
print (abecedario(abeced))
print (producto_escalar(a,b))

import numpy as np
arre = np.array([[1,2,3],
                [4,5,6]
                ])
arre2 = np.array([
                 [-1,0],
                 [0,1],
                 [1,1]])
print(np.dot(arre,arre2))
import random
aleatorios = []
def solicita():
    n=int(input("Ingrese cuantos numeros aleatorios desea obtener = ".upper()))
    for x in range(0,n):
       aleatorios.append(random.randint(0,1001))
    print (aleatorios)
solicita()
def par_estadisticos(lista):
    s=sum(lista)/len(lista)
    p=0
    for i in range(len(lista)):
        p=p+pow(lista[i]-s,2)
    p=p/(len(lista)-1)
    p=(p**1/2)
    return round(s,2),round(p,2)            
print (par_estadisticos(aleatorios))
print(ingreso.split())

#cambio de lina = '\n'
#tabulador = '\t'

    
