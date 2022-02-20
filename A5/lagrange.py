import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import util

def lagrange(xi,fi):
    x = sym.Symbol('x')
    
    pol = calcular_polinomio(xi,fi,x)
    pol_simple = pol.expand()
    pol_lambda = sym.lambdify(x,pol_simple)
    
    print(f'Polinomio: {pol_simple}')
    
    if util.solicitar_bool("Desea graficar el polinomio? S/N: "):
        graficar_polinomio(xi,fi,pol_lambda)

    if util.solicitar_bool("Desea calcular un estimado? S/N: "):
        calcular_estimado(pol_lambda)
    
def calcular_polinomio(xi,fi,x):
    pol = 0
    for i in range(0,len(xi),1):
        num = 1
        den = 1
        for j  in range(0,len(xi),1):
            if (j!=i):
                num = num*(x-xi[j])
                den = den*(xi[i]-xi[j])

        pol = pol + (fi[i]*num/den)
    return pol

def graficar_polinomio(xi,fi,pol_lambda):
    x = np.linspace(np.min(xi),np.max(xi),100)
    y = pol_lambda(x)
    
    plt.plot(x,y,label='Polinomio de Lagrange')
    plt.plot(xi,fi,'o',label='Puntos iniciales')
    
    plt.title('Interpolacion de Lagrange')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    plt.show()

def calcular_estimado(px):
    val_x = util.solicitar_float("Ingrese el valor de x a estimar: ")
    print(f"f({val_x}) = {px(val_x)}")