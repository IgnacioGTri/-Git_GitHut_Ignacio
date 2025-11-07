#pedir el nombre la edad y el año que nacio

from datetime import date

nombre=input("¿Cuál es tu nombre?")
edad=int(input("¿Cuál es tu edad?"))

fecha=date.today().year - edad
print(f"Hola, tu nombre es {nombre}. Nacieste en {fecha} y tienes {edad}")