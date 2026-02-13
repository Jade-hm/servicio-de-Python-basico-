#Tuplas
mi_tupla = (2,4)
print("Mi tupla: ", mi_tupla)

#Lista
mi_lista = [1, 3.1416, "Jade", mi_tupla]
print("El primer elemento de mi lista: ", mi_lista[0])
print("El segundo elemento de mi lista: ", mi_lista[3])
print("El tercer elemento de mi lista: ", mi_lista[2])

#Diccionarios 
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "jade",
    "pi": 3.1416,
    "Tel": "664-2783537"
}
print("Llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("Llave para accesar a mi diccionario pi", mi_diccionario["pi"])
print("Llave para accesar a mi diccionario tel", mi_diccionario["Tel"])
