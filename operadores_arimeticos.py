n_uno = 10
n_dos = 20

suma = n_uno + n_dos
print (f"La suma de {n_uno} y {n_dos} es igual a: {suma}")

resta = n_dos - n_uno
print (f"La resta de {n_dos} y {n_uno} es igual a: {resta}") 

division = n_dos / n_uno
print (f"La dividion de {n_dos} y {n_uno} es igual a: {division}")

division_exacta, residuo = divmod (n_dos, n_uno)
print(f"la division exacta de {n_dos} y {n_uno} es igual a: {division_exacta}")
print(f"El residuo de {n_dos} entre {n_uno} es igual a: {residuo}")

potencia = n_uno ** n_dos
print (f"La potencia de {n_uno} y {n_dos} es igual a: {potencia}")