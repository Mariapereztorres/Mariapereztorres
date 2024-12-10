"""
Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
La empresa Netflix desea saber cuál es el género favorito de
streaming entre 5 personas. Para esto, le ha solicitado su ayuda
para desarrollar un programa para saber cuál es el género con
más votos entre: acción y ciencia ficción. El programa debe
capturar la preferencia de las 5 personas y mostrar cuál de los
géneros es el favorito.
"""


accion = 0
ciencia_ficcion = 0


for i in range(1, 6):  
    print(f"Persona {i}: ¿Cuál es tu género favorito? (acción/ciencia ficción)")  
    preferencia = input().lower() 


     if preferencia == "acción":
        votos_accion += 1
    elif preferencia == "ciencia ficción":
        votos_ciencia_ficcion += 1
    else:
        print("Opción no válida, el voto no será contado.")


if accion > ciencia_ficcion: 
    print("\nEl género favorito es: Acción.")  
else: 
    if ciencia_ficcion > accion: 
        print("\nEl género favorito es: Ciencia ficción.") 
    else: 
        print("\nHay empate entre acción y ciencia ficción.")  
