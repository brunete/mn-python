import numpy as np
import time as t

def jacobi(f1,f2,f3,x0,y0,z0,max_iter) :
    tabla = np.empty([max_iter, 4])

    # Encabezados
    print("{:} {: >10} {: >10} {: >10}".format("i","x","y","z"))

    # Iteración
    inicio = t.perf_counter()
    for i in range(max_iter):
        x1 = f1(y0,z0)
        y1 = f2(x0,z0)
        z1 = f3(x0,y0)

        x0 = x1
        y0 = y1
        z0 = z1

        tabla[i] = [i+1,x1,y1,z1]
    fin = t.perf_counter()
    
    for iteracion in tabla:
        print("{: .0f} {: >10.4f} {: >10.4f} {: >10.4f}".format(*iteracion))

    print(f'\nSolucion: x={x1:.3f}, y={y1:.3f}, z={z1:.3f}')
    print(f"Tiempo de ejecucion: {fin - inicio:0.4f} segundos\n")