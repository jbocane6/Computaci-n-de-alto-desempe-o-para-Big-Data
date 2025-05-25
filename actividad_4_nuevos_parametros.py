# Juan Camilo Bocanegra Osorio - Computación de alto desempeño para Big Data (YESID DIAZ 21042025_C2_202541)
N = int(input()) # Solicita ingresar un número entero y lo almacena en la variable N.
db = [N] # Crea una lista llamada db y almacena el valor de N como su primer elemento.
for i in range(N): # Itera N veces, donde N es el número ingresado.
    c = input() # Solicita ingresar una cadena de texto.
    db.append(c.split(' ')) # Divide la cadena de texto en una lista de palabras y la agrega a db.
P1 = 100 # Inicializa P1 con el valor 100.
P2 = 120 # Inicializa P2 con el valor 120.
P3 = 70 # Inicializa P3 con el valor 70.
P4 = 80 # Inicializa P4 con el valor 80.
P5 = 90 # Inicializa P5 con el valor 90.
P6 = 110 # Inicializa P6 con el valor 110.
parametros = [P1, P2, P3, P4, P5, P6] # Crea una lista llamada parámetros que contiene los valores de P1 a P7.
disponibilidad = False # Inicializa la variable disponibilidad como False.
exito = [] # Crea una lista vacía llamada exito.
for i in range(db[0]): # Itera db[0] veces, donde db[0] es el valor de N.
   # int(db[i+1][0]) >= parametros[0] verifica si el primer valor de la lista dentro de la iteración es mayor o igual a P1.
   # int(db[i+1][1]) >= parametros[2] verifica si el segundo valor de la lista dentro de la iteración es mayor o igual a P3.
   # int(db[i+1][1]) <= parametros[3] verifica si el segundo valor de la lista dentro de la iteración es menor o igual a P4.
   # int(db[i+1][2]) >= parametros[4] verifica si el tercer valor de la lista dentro de la iteración es mayor o igual a P5.
   # int(db[i+1][2]) <= parametros[5] verifica si el tercer valor de la lista dentro de la iteración es menor o igual a P6.
    if (int(db[i+1][0]) >= parametros[0]) and \
    (int(db[i+1][1]) >= parametros[2]) and \
    (int(db[i+1][1]) <= parametros[3]) and \
    (int(db[i+1][2]) >= parametros[4]) and \
    (int(db[i+1][2]) <= parametros[5]):
        exito.append(int(db[i+1][3])) # Agrega el cuarto valor de db[i+1] a la lista exito.
        disponibilidad = True # Establece disponibilidad como True.
if not disponibilidad: # Valida si disponibilidad es False.
    print("NO DISPONIBLE") # Imprime "NO DISPONIBLE".
else: # Si por el contrario disponibilidad es True.
    for i in exito: # Itera sobre cada elemento en exito.
        print(i) # Imprime el elemento.
        print() # Imprime una línea en blanco.
