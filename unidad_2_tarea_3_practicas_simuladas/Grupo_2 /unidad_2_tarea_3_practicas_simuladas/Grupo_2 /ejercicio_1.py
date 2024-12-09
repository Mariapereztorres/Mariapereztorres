Realizar el siguiente ejercicio con la instrucción if..else
La escuela ECAPMA de la UNAD está desarrollando un estudio
para verificar el cambio climático en su ciudad. Para esto, le ha
pedido su ayuda en la construcción de un programa que solicite
las temperaturas de los últimos 5 días y muestre el promedio de
temperaturas si el promedio es mayor o igual a 22 grados,
debe informar que el clima es cálido si es menor que es frio.
"""


print("Bienvenido al programa de análisis climático de la escuela ECAPMA.")
print("Este programa calcula el promedio de las temperaturas de los últimos 5 días.")
print("Dependiendo del promedio, indicará si el clima es cálido o frío.\n")


print("Por favor, ingrese las temperaturas de los últimos 5 días:")
temperaturas = []


for i in range(1, 6):
  temp = float(input(f"Temperatura día {i}: "))
      temperaturas.append(temperatura)


promedio = sum(temperaturas) / len(temperaturas)


if promedio >= 22:
    print(f"El promedio de temperaturas es {promedio:.2f} grados. El clima es cálido.")
else:
    print(f"El promedio de temperaturas es {promedio:.2f} grados. El clima es frío.")

  print("\nGracias por usar este programa. 🌞❄️")
