#!/usr/bin/env python

from random import randrange
import random


"""algoritmo que proporciona la posicion del vertice a cambiar"""
"""en las ternas que se utilizan para el calculo de la nueva llave"""
def get_s(i,j,k,n):
    i=i+1
    j=j+1
    k=k+1
    return g(i,n)+f(i,j,n)+h(j,k)-1

 
def f_1(i,n):
    return ((n**2*i)/2)-((n*(i**2))/2)-n*i+(i**3)/6+(i**2)/2+i/3

def tuplas(n):
    """Numero de tuplas para en un conjunto de n numeros"""
    return (n)*(n-1)/2 

def g(i,n):
    """Numero de ternas antes de la tupla que empieza con i en un
        en un conjunto de n numeros"""
    if i<=1:
        return 0
    return ((i-1)*(3*n*n-3*n*(i+1)+i*(i+1)))/6

"""funcion para probar la funcion g"""
def g_slow(i,n):
    if i<=1:
        return 0
    s=0
    for j in range(1,i):
      s=s+tuplas(n-j)
    return s

def f(i,j,n):
    """Numero de ternas antes de las ternas entre
     (i,i+1,i+2) y (i,j,j+1) """
    return ((i-j+1)*(i+j-(2*n)))/2

"""funcion que proprociona el numero de ternas
en donde la posicion del vertice en las ternas fue la tercera"""
def h(j,k):
    return k-j
    
def hubicacion_idx_p(pts):
    """esta funcion me da la posicion a cambiar y yo pongo en la consola idxp=funciones.hubicacion_idx_p
    asi yo obtengo la posicion y despues observo que posicion me da para definir idx_p=pts[idxp]"""
    n=len(pts)
    p=randrange(0,n)    
    return p

def get_punto(j):
    """esta funcion solo nos da el nuevo punto a cambiar en un rango
    aleatorio el cual esta dado por el usuario, para mi este es el punto p y pongo p=funciones.get_punto(k) """
    a=[random.randint(-j,j),random.randint(-j,j)]
    return a


def get_punto1(k,i=1000):
    """esta funcion solo nos da el nuevo punto a cambiar en un rango
    aleatorio el cual esta dado por el usuario, para mi este es el punto p y pongo p=funciones.get_punto(k) """
    while k!=i:
        a=[random.randint(-k,k),random.randint(-k,k)]
        print a
        k=k-i
    #return a
