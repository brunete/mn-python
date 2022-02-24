def reglaSimpson(f, a, b, n):
    resultado = 0
    sumatoria = 0
    delta = ((b-a)/n)

    for i in range(n+1):
        xi = (a + (i * delta))
        
        if xi == a or xi == b:
            sumatoria += f(xi)
        elif i % 2 != 0:
            sumatoria += 4 * f(xi)
        elif i % 2 == 0:
            sumatoria += 2 * f(xi)
        
    resultado = (delta/3) * sumatoria

    return resultado