# Operaciones Algebraicas en Python

Este proyecto proporciona funciones para realizar operaciones algebraicas básicas, intermedias y avanzadas en Python. Utiliza la librería `sympy` para llevar a cabo las operaciones algebraicas.

## Funcionalidades

El proyecto actualmente ofrece las siguientes funcionalidades:

- **Operaciones Básicas**: Suma, resta, multiplicación y división de números.
- **Operaciones Intermedias**: Potenciación y cálculo de raíces cuadradas.
- **Operaciones Avanzadas**: Factorización y simplificación de expresiones algebraicas.

## Requisitos

- Python 3.x
- Librería `sympy` (se puede instalar utilizando `pip install sympy`)

## Uso

1. Clona el repositorio o descarga el archivo ZIP.
2. Instala las dependencias usando `pip install -r requirements.txt` o manualmente instalando `sympy`.
3. Ejecuta el script `operaciones_algebraicas.py`.
4. Modifica los valores de entrada según sea necesario para realizar las operaciones deseadas.

## Ejemplos de Uso

```python
# Operaciones básicas
resultado_basicas = operaciones_basicas(5, 2)
print("Suma:", resultado_basicas[0]) # Salida: 7
print("Resta:", resultado_basicas[1]) # Salida: 3
print("Multiplicación:", resultado_basicas[2]) # Salida: 10
print("División:", resultado_basicas[3]) # Salida: 2.5

# Operaciones intermedias
resultado_intermedias = operaciones_intermedias(5, 2)
print("Potencia:", resultado_intermedias[0]) # Salida: 25
print("Raíz cuadrada de 5:", resultado_intermedias[1]) # Salida: sqrt(5)
print("Raíz cuadrada de 2:", resultado_intermedias[2]) # Salida: sqrt(2)

# Operaciones avanzadas
resultado_avanzadas = operaciones_avanzadas(sin(x)**2 + cos(x)**2)
print("Factorización de la expresión:", resultado_avanzadas[0]) # Salida: 1
print("Simplificación de la expresión:", resultado_avanzadas[1]) # Salida: 1
```
