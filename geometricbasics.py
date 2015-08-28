#!/usr/bin/env python

from math import sqrt
from combinatorics import *
from datastructures import *

#funcion para decidir si
#la vuelta es al a izq (-1) o der (1)
#se usa para definir el tipo de orden de un conjunto de puntos dado.
def turn(p0,p1,p2):
   t=((p2[0]-p0[0])*(p1[1]-p0[1]))-((p1[0]-p0[0])*(p2[1]-p0[1]))
   if t >0:
      return 1
   else:
      if t < 0:
         return -1
   return 0


#verifica si dos puntos son iguales
def pointEqual(p,q):
 return (p[0]==q[0]) and (p[1]==q[1])


#regresa  la distnacia entre dos puntos
def distance(p,q):
   return sqrt((p[0]-q[0])*(p[0]-q[0])+
               (p[1]-q[1])*(p[1]-q[1]))

#regresa un arreglo de punto escalado en r
def scale(p,r):
   q=[]
   for v in p:
      q.append([int(round(v[0]*r)),
                int(round(v[1]*r))])
   return q
               


def sort_around_point(p,points,join=True):
   """Sorts a set of points by angle around
      a point p.***5 March 2012, found a mistake, it
      had however not affected other functions using
      it. Check here for problems in the future.
      When computing the visibility graph of a point
      set, the starting point does matter. It now makes
      sure it starts at the right point. It did not
      before.***Remove when everything is ok
      Also refactor, it seems to take time O(n^2)!"""
   l=0
   r=0
   p1=[p[0],p[1]+1]
   for x in points:
      if turn(p,p1,x) > 0:
         r=r+1
      else:
         if turn(p,p1,x) <  0:
            l=l+1
         else:
            if p[1] >= x[1]:
               l=l+1
            else:
               r=r+1
   r=[[0,0] for i in range(r)]
   l=[[0,0] for i in range(l)]
   ir=0
   il=0
   for x in points:
      if turn(p,p1,x) > 0:
         r[ir]=x[:]
         ir=ir+1
      else:
         if turn(p,p1,x) <  0:
            l[il]=x[:]
            il=il+1
         else:
            if p[1] >= x[1]:
               l[il]=x[:]
               il=il+1
            else:
               r[ir]=x[:]
               ir=ir+1
                     
   l.sort(lambda v1,v2:turn(p,v1,v2))
   r.sort(lambda v1,v2:turn(p,v1,v2))
   
   if join:
      tpts=[[0,0] for i in range(len(points))]
      for i in range(len(r)):
         tpts[i]=r[i][:]
      for j in range(len(l)):
         tpts[len(r)+j]=l[j][:]
      concave=False
      for i in range(len(tpts)):
         if turn(tpts[i],p,tpts[(i+1)%len(tpts)])<0:
            concave=True
            break
      if concave:
         start=(i+1)%len(tpts)
         tpts=[tpts[(start+i)%len(tpts)][:] for i in range(len(tpts))]
      
      
      return tpts
   else:
      return (r,l)

#regresa un arreglo de los puntos ordenados por angulo alrededor de x
# en dos listas
def orderandsplit(points):
   
   orderedpoints = []
   for p in points:
      l=[]
      r=[]
      p1=[p[0],p[1]+1]
      
      for x in points:
         if not p is x:
            if turn(p,p1,x) > 0:
               r.append(x)
            else:
               if turn(p,p1,x) <  0:
                  l.append(x)
               else:
                  if p[1] >= x[1]:
                     l.append(x)
                  else:
                     r.append(x)
                     
      l.sort(lambda v1,v2:turn(p,v1,v2))
      r.sort(lambda v1,v2:turn(p,v1,v2))
      orderedpoints.append([p,r,l])
      
   return orderedpoints

def sortpoints(pts):
   ptsordsplit=orderandsplit(pts)
   for p in ptsordsplit:
      p[1].extend(p[2])
      p.pop()
   return ptsordsplit

def countCrossings(pts):
   """Cuenta el numero de cruces rectilineo de un
      conjunto de puntos, corre en tiempo O(n^2logn). No
      es correcta si los puntos No estan en posicion general"""
   ordpts=sortpoints(pts)
   cr=0
   n=len(pts)
   for lp in ordpts:
      po=lp[0]
      j=0
      for i in range(len(lp[1])):
         pi=lp[1][i]
        
         while turn(po,pi,lp[1][(j+1)%len(lp[1])]) <=0 and (j+1)%len(lp[1])!=i:
            j=j+1
            
         cr=cr+binomial((j-i)%len(lp[1]),2)
 
   total=n*(n-3)*binomial(n-1,2)
   
   #Voodoo magic!
   return cr-(total/4)
      


#funcion de tiempo O(n^3) para verificiar si un conjunto
#de puntos esta o no en posicion convexa regresa 0 si lo esta
#y en caso contrario el numero de tercias collineales
#imprime tambien las ternas colineales de momento
def slow_generalposition(pts):
   col=0
   for i in range(len(pts)):
      for j in range(i+1,len(pts)):
         for k in range(j+1,len(pts)):
            if turn(pts[i],pts[j],pts[k])==0:
               col=col+1
   return col

def general_position(points,return_tuples=False):
   """Checks in time O(n^2logn) wheter
      the point set is in general position"""
   ord_points=orderandsplit(points)
   col=0
   if return_tuples:
      tuples=[]
   for p in ord_points:
      point=p[0] #point p
      rpoints=p[1] #points to the right of p
      for i in range(len(rpoints)-1):
         if slow_generalposition([point,rpoints[i],rpoints[i+1]])>0:
            col=col+1
            if return_tuples:
               tuples.append([point,rpoints[i],rpoints[i+1]])
   if return_tuples:
      return tuples
   return col

