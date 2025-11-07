
while True:
    a = float(input("Número 1: ")) 
    b = float(input("Número 2: ")) 
    op = input("Operación (+, -, *, /): ") 
    if op == "+": 
        resultado = a + b 
    elif op == "-": 
        resultado = a - b 
    elif op == "*": 
        resultado = a * b 
    elif op == "/":    
        resultado = a / b 
    else: 
        resultado = "Operación no válida" 
    print(f"Resultado: {resultado}")

    #Commit: "Versión inicial de la calculadora"
    with open("historial.txt", "a") as f: 
        f.write(f"{a} {op} {b} = {resultado}\n") 
    #Commit: "Añadido guardado en historial.txt"



    # (todo el código anterior) 
        continuar = input("¿Quieres hacer otra operación? (s/n): ") 
        if continuar.lower() != "s": 
            break 
    #Commit: "Añadido bucle para múltiples operaciones" 


    with open("historial.txt", "r") as f: 
        print(f.read()) 
    #Commit: "Muestra historial al finalizar"

