alumnos = ["Arnold", "Alfredo", "Anthony"]
print (f"inicio: {alumnos}")
# append -> agregar un valor a una lista
alumnos.append("diego")
print(f"append: {alumnos}")

alumnos.insert(1,"elvia")
print(f"insert: {alumnos}")

# index devuelve la posicion de un valor

posicion_anthony = alumnos.index ("Anthony")
print(f"la posicion (indice) de Anthony es: {posicion_anthony}")

# remove -> remover un valor de la lista
# count -> retorna las veces que exitse un valor
# pop remueve un valor de un alista, segun su indice
# extent -> junta dos listas
print(f"Total de alumnos: {len(alumnos)} ")

print ("################################################")

persona = {
    "nombres":"Nixon Guevara",
    "edad": 20,
    "hobbies": ["futbol", "Nadar", "Jugar"]
}

print(f"Nombre de la persona: {persona ['nombres']}")
print(f"Segundo Hobby: {persona ['hobbies'] [1]}")
# get -> busca el valor con la clave 
print(persona.get("cursos") )

