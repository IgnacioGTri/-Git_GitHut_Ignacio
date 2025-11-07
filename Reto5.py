#tabla de multiplicar

# Pide al usuario que ingrese un número
numero = int(input("Ingresa un número para generar la tabla: "))

# Itera del 1 al 10
for i in range(1, 11):
    # Calcula y muestra el resultado
    print(f"{numero} x {i} = {numero * i}")