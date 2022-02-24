import numpy as n

def trapecio(f,a,b,tramos):
    h = (b-a)/tramos
    xi = a
    suma = f(xi)
    
    for i in range(1,tramos):
        xi = xi + h
        suma = suma + 2*f(xi)
    
    suma = suma + f(b)
    area = h*(suma/2)
    return area