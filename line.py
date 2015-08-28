#!/usr/bin/env python
from fractions import *
import geometricbasics

def dual_point_to_line(point):
    l=Line(p=[0,point[1]],q=[1,point[0]+point[1]])
    return l

class Line:
    
    def __init__(self,p=[0,0],q=[1,1],color="grey"):
        """constructs a line with passing
           through p and q"""
        delta_x=p[0]-q[0]
        delta_y=p[1]-q[1]
        if delta_x!= 0:
            if (delta_x.__class__==Fraction or
                delta_y.__class__==Fraction):
                self.m=delta_y/delta_x
            else:
                self.m=Fraction(delta_y,delta_x)
            self.b=p[1]-self.m*p[0]
        else:
            self.m=None
            self.b=p[0]
            
        self.color=color
        
    
    def line_intersection(self,l):
        """Computes the intersection
           of this line with l. Returns
           None if the lines are parallel"""
        
        if self.m == l.m:
            return None
    
         #If one of them is vertical
        if self.m==None or l.m==None:
            if self.m==None:
                x=self.b
                y=l.m*x+l.b
                return [x,y]
            if l.m==None:
                x=l.b
                y=self.m*x+self.b
                return [x,y]
        
        #General case
        x=(l.b-self.b)/(self.m-l.m)
        y=self.m*x+self.b
        
        return [x,y]
        
    def point_in_line(self,point):
        """Test wheter a point is: above, below
            or in the line. returns -1,1 and 0
            respectively"""
        
        if self.m!=None:
            p=[0,self.b]
            q=[1,self.m+self.b]
        else:
            p=[self.b,0]
            q=[self.b,1]
        
        inline=geometricbasics.turn(p,q,point)
        return inline
    
    def __str__(self):
        return "m="+self.m.__str__()+",b="+self.b.__str__()
    
        
            