import numpy as np
import lagrange as l
import util

if __name__ == "__main__":
    xi = None; fi = None

    if util.solicitar_bool("Cargar automaticamente el ejercicio 18.7 de Chapra? S/N: "):
        xi = np.array([1.0,3.0,5.0,7.0,13.0])
        fi = np.array([800.0,2310.0,3090.0,3940.0,4755.0])
        print(f"x = {xi}")
        print(f"f(x) = {fi}")
    else:
        num_puntos = util.solicitar_int("Cuantos puntos iniciales?: ")
        print()

        xi = np.empty(num_puntos)
        fi = np.empty(num_puntos)

        for i in range(num_puntos):
            xi[i]= float(input(f"x[{i}] = "))
            fi[i]= float(input(f"y[{i}] = "))
            print()

    l.lagrange(xi,fi)