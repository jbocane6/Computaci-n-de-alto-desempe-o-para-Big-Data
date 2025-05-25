# Solicitar al usuario la cantidad de diseños de ruedas que desea evaluar
print("Ingrese la cantidad de diseños de ruedas que desea evaluar:")
N = int(input())  # int convierte la entrada a entero
db = []  # Inicializa una lista vacía para almacenar los registros

# Informa a el usuario sobre el formato de entrada
print(f"Ingrese los {N} registros, uno por línea con el formato:")
print("DIÁMETRO(mm) GROSOR(mm) ANCHO(mm) PRECIO")

# Se genera un bucle para recibir los registros de diseño de ruedas
for i in range(N):
    c = input(f"Ingrese diseño #{i+1}: ")  # Solicita al usuario ingresar los datos
    db.append(c.split(' '))  # Divide las entradas usando el espacio como referencia y los agraga a una lista

# Parámetros de validación para los diseños de ruedas
P1 = 100   # Diámetro mínimo permitido
P2 = 120   # Diámetro máximo permitido
P3 = 70    # Grosor mínimo permitido
P4 = 80    # Grosor máximo permitido
P5 = 90    # Ancho mínimo permitido
P6 = 110   # Ancho máximo permitido

disponibilidad = False  # Inicializa la variable como falsa
exito = []  # Lista para almacenar los precios cuando cumpla las condiciones

# Bucle para evaluar cada diseño ingresado
for i in range(N):
    diametro = int(db[i][0])  # Asigna el valor en la lista a la variable diametro como entero
    grosor = int(db[i][1])    # Asigna el valor en la lista a la variable grosor como entero
    ancho = int(db[i][2])     # Asigna el valor en la lista a la variable ancho como entero
    precio = int(db[i][3])    # Asigna el valor en la lista a la variable precio como entero

    # Verifica si el diseño cumple con los parámetros establecidos
    if (P1 <= diametro <= P2) and (P3 <= grosor <= P4) and (P5 <= ancho <= P6):
        exito.append(precio)  # Agrega el precio a la lista de éxitos
        disponibilidad = True  # Cambia la disponibilidad a verdadero

# Muestra el resultado según el valor de disponibilidad
if not disponibilidad:
    print("NO DISPONIBLE")  # Mensaje si no hay diseños válidos
else:
    print("Precios de diseños que cumplen con el reglamento:")
    for precio in exito:
        print(precio)  # Imprime los precios de los diseños válidos
