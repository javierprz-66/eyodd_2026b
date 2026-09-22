"""""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por Ejemplo su n = 100, el programa
calculara la suma del 1 al 100
"""

 # Importar biblioteca time
import time 

#Tomnado el tiempo inicial
timestamp_01 = time.time()

# Programa que calcula la suma 
# de los "n" numeros naturales
n = 1500
total_sum = 0

# Ciclo for
for number in range(1,n+1):
    #print(number, end= ",")
    total_sum = total_sum + number
    # 1: sum - 0 + 1
    # sum = 1
    # 2: sum - 1 +2
    #sum



print(f"La suma de 1 hasta {n} es: {total_sum}")

# Tomando el tiempo final
timestamp_02 = time.time()

# Impresion del tiempo de ejecucion 
print(f"Tiempo de ejcucion: {(timestamp_02-timestamp_01) * 1e6:.2f} μs")