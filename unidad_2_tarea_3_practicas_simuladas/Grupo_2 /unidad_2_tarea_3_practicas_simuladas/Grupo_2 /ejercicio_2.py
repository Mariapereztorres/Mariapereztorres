"""
Realizar el siguiente ejercicio con la instrucción if..else
Construir un programa que permita verificar si una persona es
mayor de edad. Para esto debe solicitar el año de nacimiento,
calcular la edad y si la edad es mayor o igual a 18 mostrar un
mensaje por consola que indique que la persona es mayor de
edad, de lo contrario que muestre un mensaje indicando que es
menor de edad
"""


print("Bienvenido al programa de verificación de mayoría de edad.")
print("Este programa te dirá si eres mayor o menor de edad basándose en tu año de nacimiento.\n")


anio_nacimiento = int(input("Ingrese su año de nacimiento: 2008"))


from datetime import date
anio_actual = date.today(2024).year 
edad = anio_actual - anio_nacimiento  


if edad >= 18:
    print(f"Tienes {edad} años. Eres mayor de edad.")
else:
    print(f"Tienes {edad} años. Eres menor de edad.")


print("\nGracias por usar este programa. ¡Hasta luego!")
