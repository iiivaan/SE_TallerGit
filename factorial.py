def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pide al usuario que ingrese un número
n = int(input("Ingrese un número: "))

# Calcula el factorial del número ingresado
fact = factorial(n)

# Imprime el resultado
print("El factorial de", n, "es", fact)
