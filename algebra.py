import sympy as sp

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir entre cero"
    return suma, resta, multiplicacion, division

def operaciones_intermedias(a, b):
    potencia = a ** b
    raiz_cuadrada_a = sp.sqrt(a)
    raiz_cuadrada_b = sp.sqrt(b)
    return potencia, raiz_cuadrada_a, raiz_cuadrada_b

def operaciones_avanzadas(expresion):
    expresion_factorizada = sp.factor(expresion)
    expresion_simplificada = sp.simplify(expresion)
    return expresion_factorizada, expresion_simplificada

# Ejemplos de uso
a = 5
b = 2
expresion = sp.sin(sp.Symbol('x'))**2 + sp.cos(sp.Symbol('x'))**2

# Operaciones básicas
resultado_basicas = operaciones_basicas(a, b)
print("Operaciones básicas:")
print("Suma:", resultado_basicas[0])
print("Resta:", resultado_basicas[1])
print("Multiplicación:", resultado_basicas[2])
print("División:", resultado_basicas[3])

# Operaciones intermedias
resultado_intermedias = operaciones_intermedias(a, b)
print("\nOperaciones intermedias:")
print("Potencia:", resultado_intermedias[0])
print("Raíz cuadrada de", a, ":", resultado_intermedias[1])
print("Raíz cuadrada de", b, ":", resultado_intermedias[2])

# Operaciones avanzadas
resultado_avanzadas = operaciones_avanzadas(expresion)
print("\nOperaciones avanzadas:")
print("Factorización de la expresión:", resultado_avanzadas[0])
print("Simplificación de la expresión:", resultado_avanzadas[1])
