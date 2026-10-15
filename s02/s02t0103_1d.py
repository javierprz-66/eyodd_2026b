from array import array as arr





# Archivo
from s02t0102_1d import print_array
 
my_array = arr("i",[2,10,15,20])

print("--- ANTES DE LA INSERCION ---")
print_array(my_array)

# Insercion
my_array.insert(1,90)
print("--- DESPUES DE LA INSERCION ---")
print_array(my_array)

print("--- DEPUES DE UN APPEND--")
my_array.append(1000)
print_array(my_array)

print("--- SIMILAR UN APPEND CON UN INSERT")
my_array.insert(len(my_array), 90000)
print_array(my_array)