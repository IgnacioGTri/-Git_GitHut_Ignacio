
num1=float(input("Inserta número 1: "))
num2=float(input("Inserta número 2: "))
resultado=float("0")
operacion =(input("¿Qué operación quieres realizar? + , - , * o / : "))
if operacion == "+":
    resultado= num1 + num2
    print(f"El resultado es {resultado}")
elif operacion == "-":
    resultado= num1 - num2
    print(f"El resultado es {resultado}")
elif operacion == "*":
    resultado= num1*num2
    print(f"El resultado es {resultado}")
elif operacion== "/":
    if num2==0 :
        print("no puedes dividir entre 0")
    else: 
        resultado= num1 / num2
        print(f"El resultado es {resultado}")

else: print("Operacion Invalida.")


 