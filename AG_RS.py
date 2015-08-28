#!/usr/bin/env python

import random
import math
import geometricbasics
import time
""" funcion de temperatura"""
def kirkpatrick_cooling(start_temp,alpha):
    T=start_temp
    while True:
        yield T
        T=alpha*T


def rand_move(p,t=1000000):
    """Moves point randomly to a new location"""
    l=1.0/float(t)
    tx=random.expovariate(l)
    l=1.0/float(t)
    ty=random.expovariate(l)
    tx=int(tx)
    ty=int(ty)
    if random.randint(0,1)==0:
        tx=-tx
    if random.randint(0,1)==0:
        ty=-ty
    p[0]=p[0]+tx
    p[1]=p[1]+ty
        
        

def P(vcurrent,vnew,T):
    """Computes the probability of accepting the new value.
       It also runs the corresponding probabilitic trial.
       Returns True if the solution should be accepted
       false otherwise."""
       
    df=vcurrent-vnew
    if df>=0:
        return True
    
    df=float(df)
    p=math.exp(df/float(T))
    print(p)
    if random.random()<=p:
        return True
    return False
    
"""programa principal RS"""
def simmulated_annealing(n=10,pts=[],intentos=10000,run_time=10,k=10000000,k_f=kirkpatrick_cooling(10000000,0.99),
                         f=geometricbasics.countCrossings,
                         T=kirkpatrick_cooling(100,0.99),min_val=0):
    """Implementation of a simulated annealing algorithm to search for good point sets."""

    for i in range(len(pts),n):
        pts.append([random.randint(-k,k),random.randint(-k,k)])
        
    n=len(pts)
    start_time=time.time()
    vcurrent=f(pts)
    t=0
    """Condiciones de paro del algoritmo RS"""
    
    """t<intentos while """
    while min_val<vcurrent:
        archi=open('datosSM.txt','a')
        idxp=random.randint(0,n-1)
        p=pts[idxp]
        q=p[:]
        rand_move(p,int(k_f.next()))
        vnew=f(pts)
        if P(vcurrent,vnew,T.next()):
            if vnew!=vcurrent:
                min_cruces=str(vnew)
                crossing=str(vcurrent)
                iteracion=str(t)
                print (vnew), T.next()
                archi.write(min_cruces +'\t'+ crossing +'\t'+iteracion+'\n')
            vcurrent=vnew
           
        else:
            min_cruces=str(vnew)
            crossing=str(vcurrent)
            iteracion=str(t)
            p[0]=q[0]
            p[1]=q[1]
            archi.write(crossing +'\t'+ crossing +'\t'+iteracion+'\n\n')
        t=t+1
    return n,vcurrent


"""Programa principal AG"""
def greedy(n,intentos=10000,k_f=kirkpatrick_cooling(10000000,0.99),pts=[],k=10000000,f=geometricbasics.countCrossings,min_val=229):
   
    for i in range(n-len(pts)):
        pts.append([random.randint(-k,k),random.randint(-k,k)])
    
    min=f(pts)
    t=0
    
    
    """ Condicuiones de paro del algoritmo AG"""
    """while t<intentos:"""
    """while min_val<min:"""
    
    while min_val<min:
        archi=open('datosGREEDY.txt','a')
        min_cruces=str(min)
        idxp=random.randint(0,n-1)
        p=pts[idxp]
        q=p[:]
        s=rand_move(p,k_f.next())
        r=f(pts)
        crossing=str(r)
        iteracion=str(t)
        if r <= min:
            archi.write(min_cruces +'\t'+ crossing +'\t'+iteracion+'\n')
            min=r
            q=p[:]
        p[0]=q[0]
        p[1]=q[1]
        t=t+1
        print t, min, k_f.next(), s
        #print adaptarray[idxp]
    return min , n