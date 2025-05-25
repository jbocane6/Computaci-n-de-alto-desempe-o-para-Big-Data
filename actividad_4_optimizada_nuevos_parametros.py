# Juan Camilo Bocanegra Osorio - Computación de alto desempeño para Big Data (YESID DIAZ 21042025_C2_202541)
def get_input_data(): # Función para ingresar los datos
    N = int(input()) # Solicita ingresar un número entero y lo almacena en la variable N.
    db = [N] # Crea una lista llamada db y almacena el valor de N como su primer elemento.
    for _ in range(N): # Itera N veces, donde N es el número ingresado, ignorando el valor iterado (_).
        c = input() # Solicita ingresar una cadena de texto.
        db.append(list(map(int, c.split()))) # Divide la cadena de texto en una lista de enteros y la agrega a db, mapeando los valores como enteros y luego recreando la lista.
    return db

def check_availability(db, parametros): # Función que analiza los datos y valida disponibilidad.
    disponibilidad = False # Inicializa la variable disponibilidad como False.
    exito = [] # Crea una lista vacía llamada exito.
    for i in range(db[0]): # Itera db[0] veces, donde db[0] es el valor de N.
        if all([ # Devuelve True si todas las validaciones son correctas, de lo contrario, False.
            db[i+1][0] >= parametros[0], #verifica si el primer valor de la lista dentro de la iteración es mayor o igual al primer valor de perametros.
            parametros[2] <= db[i+1][1] <= parametros[3], # Verifica si el segundo valor de la lista dentro de la iteración está entre los valores 3 y 4 de parámetros.
            parametros[4] <= db[i+1][2] <= parametros[5] # Verifica si el tercer valor de la lista dentro de la iteración está entre los valores 5 y 6 de parámetros.
        ]):
            exito.append(db[i+1][3]) # Agrega el cuarto valor de db[i+1] a la lista exito.
            disponibilidad = True # Establece disponibilidad como True.
    return disponibilidad, exito # Devuelve los 2 valores para que la función principal actúe.

def main():
    parametros = [100, 120, 70, 80, 90, 110] # Define los parámetros
    db = get_input_data() # Obtiene los datos de entrada
    disponibilidad, exito = check_availability(db, parametros) # Verifica la disponibilidad y obtiene los éxitos

    if not disponibilidad: # Valida si disponibilidad es False.
        print("NO DISPONIBLE") # Imprime "NO DISPONIBLE".
    else: # Si por el contrario disponibilidad es True.
        for i in exito: # Itera sobre cada elemento en exito.
            print(i) # Imprime el elemento.
        print()

if __name__ == "__main__": # Valida si se está ejecutando directamente o es importado.
    main() # Ejecuta la función principal.
