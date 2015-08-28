#!/usr/bin/env python
import time
import random
import funciones
import geometricbasics

def turn(p0,p1,p2):
   t=((p2[0]-p0[0])*(p1[1]-p0[1]))-((p1[0]-p0[0])*(p2[1]-p0[1]))
   if t >0:
      return 1
   else:
      if t < 0:
         return -1


"""Definicion del algoritmo BT por recursion"""
def tries_lt2(n,pts=[],run_time=10,c=0,iterador=10000,k=100000000,f=geometricbasics.countCrossings,intentos=100,min_val=4430):
    
    for i in range(len(pts),n):
        pts.append([random.randint(-k,k),random.randint(-k,k)])
    """Esta funcion inicializa la primer solucion"""
    def Add_LT():
      idxp=random.randrange(0,n)
      p=funciones.get_punto(k)
      z2=actualizar_llave(current_key[0],pts,p,idxp)
      q=pts[idxp]
      pts[idxp]=p
      crossing=f(pts)
      archi=open('datosTS.txt','a')
      if min_crossing>=crossing:
        if min_crossing>crossing:
            empty_dict[0]=True
            dicc[z2]=crossing
            crucesn=str(min_crossing)
            crucesv=str(crossing)
            iteracion=str(l)
            archi.write(crucesn +'\t'+crucesv +'\t'+iteracion+'\n')
           # archi.write( + '\n\n\t')
            #archi.write( + '\n\n\t')
            print "llaves"
            #print current_key[0]
            print z2,
            current_key[0]=z2
            archi.close()
        else:
            crucesn=str(min_crossing)
            crucesv=str(crossing)
            iteracion=str(l)
            if dicc.has_key(z2)==False:
               print "point set NOT in list"
               dicc[z2]=crossing
               archi.write(crucesn +'\t'+crucesv +'\t'+iteracion+'\n')
               current_key[0]=z2
            else:
               print "point set in list"
               archi.write(crucesn +'\t'+crucesv +'\t'+iteracion+'\n')
               pts[idxp]=q
            archi.close()       
      else:
        crucesn=str(min_crossing)
        crucesv=str(crossing)
        iteracion=str(l)
        archi.write(crucesn +'\t'+ crucesn +'\t'+ iteracion+'\n' )
        archi.close()
        print min_crossing, crossing, iteracion,k,r
        pts[idxp]=q
      

    #pts=lista(n,k)
    min_crossing=f(pts)
    current_key=[llave(pts)]
    start_time=time.time()
    dicc={current_key[0]:min_crossing}
    empty_dict=[False]
    contador=0
    l=0
    r=1
    
    """Condicion de paro del algoritmo BT
    en esta ocacion termina si encuentra el numero de cruces o si realiza las iteraciones solicitadas"""
    """l<=iterador::"""
    while min_val<min_crossing and l<=iterador:
       Add_LT()
       if empty_dict[0]:
          min_crossing=dicc[current_key[0]]
          dicc={current_key[0]:min_crossing}
          empty_dict[0]=False
          contador=0
       else:
          contador=contador+1
          if contador>intentos:
            if k<1000000:
                contador=0
                k=1000000000
                r=r+1 
            else:
                contador=0
                k=k/2
       l=l+1        
    return min_crossing,n,k


""" pruebas para la actualizacion de la llave"""
"""def test_actualizar_llave(n,tries=1000,k=100000000):
   for i in range(1000):
      pts=lista(n,k=k)
      idxp=random.randrange(0,n)
      p=funciones.get_punto(k)
      llave_init=llave(pts)
      llave_1=actualizar_llave(llave_init,pts,p,idxp)
      q=pts[idxp]
      pts[idxp]=p
      llave_2=llave(pts)
      if llave_1!=llave_2:
         print "ERROR"
         return (q,p,idxp,pts)
      else:
         print "test "+str(i)+", llave:"+str(llave_1)"""

"""Funcion que calcula el valor de la llave de la nueva configuracion
al momento del mover solo un vertice, se ejecuta en tiempo O(n^2)"""

def actualizar_llave(llave,pts,p,idxp):
   """Actualiza la llave dada la llave anterior, el nuevo
   conjunto de puntos el indice del punto que se movio
   y su ubicacion anterior """
   llave1=0
   n=len(pts)
   idx_p=pts[idxp]
   for j in range(idxp+1,n):
      for k in range(j+1,n):
         s=funciones.get_s(idxp,j,k,n)
         l1=turn(p,pts[j],pts[k])
         l2=turn(idx_p,pts[j],pts[k])
         if l1==l2:
            llave1=llave
         elif (l1!=l2 and l2==1):
            llave1=llave-l2*2**s           
         elif (l1!=l2 and l2==-1):
            llave1=llave+l1*2**s
         llave=llave1
   
   for i in range(idxp):
      for k in range(idxp+1,n):
         s=funciones.get_s(i,idxp,k,n)
         l1=turn(pts[i],p,pts[k])
         l2=turn(pts[i],idx_p,pts[k])
         if l1==l2:
            llave1=llave
         elif (l1!=l2 and l2==1):
            llave1=llave-l2*2**s
         elif  (l1!=l2 and l2==-1):
            llave1=llave+l1*2**s
         llave=llave1   
   
   for i in range(idxp):
      for j in range(i+1,idxp):
         s=funciones.get_s(i,j,idxp,n)
         l1=turn(pts[i],pts[j],p)
         l2=turn(pts[i],pts[j],idx_p)
         if l1==l2:
            llave1=llave
         elif (l1!=l2 and l2==1):
            llave1=llave-l2*2**s
         elif  (l1!=l2 and l2==-1):
            llave1=llave+l1*2**s
         llave=llave1   
   return llave1

"""Calcula el valor de la llave del conjunto inicial
apartir de su configuracion inicial, se ejecuta en O(n^3)"""
def llave(pts):
   key=0
   n=len(pts)
   l=0
   for i in range (0,n):
       for j in range (i+1,n):
           for k in range (j+1,n):
               s=turn(pts[i],pts[j],pts[k])
               if s==-1:
                   s=0
               key=key+s*2**l
               l=l+1
   return key   
