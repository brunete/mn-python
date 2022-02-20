import jacobi as j
import gauss_seidel as gs
import util

f1 = lambda y,z: (960-3*y-2*z)/4
f2 = lambda x,z: (510-x-z)/3
f3 = lambda x,y: (610-2*x-y)/3

print('Sistema de funciones:')
print('4x + 3y + 2z = 960')
print('x + 3y + z = 510')
print('2x + y + 3z = 610\n')

est_x = 100
est_y = 100
est_z = 100

quiere_estimar = util.solicitar_bool('Desea definir las estimaciones iniciales? S/N: ')
if quiere_estimar:
    est_x = util.solicitar_float('Estimacion para x: ')
    est_y = util.solicitar_float('Estimacion para y: ')
    est_z = util.solicitar_float('Estimacion para z: ')
print()

print('- - - - Jacobi - - - -')
max_iter = util.solicitar_int('Ingrese numero de iteraciones de Jacobi: ')
print()
j.jacobi(f1,f2,f3,est_x,est_y,est_z,max_iter)

print('- - - - Gauss-Seidel - - - -')
max_iter = util.solicitar_int('Ingrese numero de iteraciones de Gauss-Seidel: ')
print()
gs.gauss_seidel(f1,f2,f3,est_y,est_z,max_iter)