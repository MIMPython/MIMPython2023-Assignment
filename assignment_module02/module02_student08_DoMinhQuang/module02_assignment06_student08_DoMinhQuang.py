from ast import List
from math import sqrt

a=int(input())

b=int(input())

c=int(input())

def solution(a,b,c):
    delta=(b*b-4*a*c)
    
    if(delta>0):
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        if(x1<x2):
          return [x1,x2]            
        elif(x1>x2):
           return [x2,x1]
    elif(delta==0):
        x=(-b+sqrt(delta))/(2*a)
        return [x]
    else:
       return []

list = solution(a,b,c)
tuple=tuple(list)
print(tuple)






    
        