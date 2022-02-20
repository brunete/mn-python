def solicitar_int(mensaje):
    while True:
        n = input(mensaje)
        try:
            return int(n)
        except :
            print("Ingrese un numero entero...")

def solicitar_float(mensaje):
    while True:
        n = input(mensaje)
        try:
            return float(n)
        except :
            print("Ingrese un numero...")

def solicitar_bool(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.upper() == "S":
            return True
        if entrada.upper() == "N":
            return False
        print("Ingrese S(Si) o N(No)...")