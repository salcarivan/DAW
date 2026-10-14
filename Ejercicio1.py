""" Los médicos forenses utilizan la longitud de los huesos para determinar la altura de una
persona, cuando la persona estaba viva.
Por ejemplo, para los varones:
altura (en cm) = 69.089 + 2.232 × longitud de la tibia
Para las mujeres, el valor es el siguiente:
altura (en cm) = 61.412 + 2.317 × longitud de la tibia
A partir de los 30 años (inclusive), la altura de una persona decrece a una tasa de 0.06
cm por año.
Escribir un programa que, dados los valores de la longitud de la tibia, el sexo y la edad
del paciente, nos calcule la altura aproximada.
"""
def validar_longitud_tibia():
    """Valida que la longitud de la tibia sea un número positivo razonable"""
    while True:
        try:
            longitud = float(input("Por favor ingresa la longitud de tu tibia en cm: "))
            if longitud <= 0:
                print("Error: La longitud debe ser un número positivo.")
            elif longitud > 60:  # Una tibia humana no suele superar los 60 cm
                print("Error: La longitud ingresada parece demasiado grande. Intenta de nuevo.")
            else:
                return longitud
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def validar_sexo():
    """Valida que el sexo sea 'M' (masculino) o 'F' (femenino)"""
    while True:
        sexo = input("Ingresa tu sexo (M para masculino, F para femenino): ").strip().upper()
        if sexo in ['M', 'F']:
            return sexo
        else:
            print("Error: Debes ingresar 'M' o 'F'.")

def validar_edad():
    """Valida que la edad sea un número entero positivo razonable"""
    while True:
        try:
            edad = int(input("Ingresa tu edad en años: "))
            if edad <= 0:
                print("Error: La edad debe ser un número positivo.")
            elif edad > 120:
                print("Error: La edad ingresada no es realista.")
            else:
                return edad
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def calcular_altura(longitud_tibia, sexo, edad):
    """Calcula la altura aproximada según la longitud de la tibia, sexo y edad"""
    if sexo == 'M':
        altura = 69.089 + 2.232 * longitud_tibia
    else:  # sexo == 'F'
        altura = 61.412 + 2.317 * longitud_tibia
    
    # A partir de los 30 años, la altura decrece 0.06 cm por año
    if edad >= 30:
        años_pasados = edad - 30
        altura -= 0.06 * años_pasados

    return altura

# Programa principal
print("=== CÁLCULO DE ALTURA APROXIMADA A PARTIR DE LA TIBIA ===\n")

long_tibia = validar_longitud_tibia()
sexo = validar_sexo()
edad = validar_edad()

altura_estimada = calcular_altura(long_tibia, sexo, edad)

print(f"\n--- RESULTADOS ---")
print(f"Longitud de la tibia: {long_tibia} cm")
print(f"Sexo: {'Masculino' if sexo == 'M' else 'Femenino'}")
print(f"Edad: {edad} años")
print(f"Altura aproximada: {altura_estimada:.2f} cm")