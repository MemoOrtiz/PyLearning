animal = "    leoPArdo leo   "
print(animal.upper()) #hace mayusculas toda la string
print(animal.lower())#hace minusculas toda la string
print(animal.capitalize())
"""
El método capitalize hace que el primer caracter del String
se haga mayuscula, pero si es un espacio en blanco no hay
ninguna diferencia
"""
print(animal.title())
"""
El método title hace que con cada espacio el primer
caracter sea mayuscula
"""
print(animal.strip())
"""
El método strip remueve todos los espacios en blanco a la 
izquierda y derecha de la cadena en cuestión
"""
print(animal.lstrip())#quita los espacios en blanco de la izquierda
print(animal.rstrip())#quita los espacios en blanco de la derecha
print(animal.strip().capitalize())
print(animal.find("PA"))
"""
el método find devuelve el índice de la cadena a encontrar
 y si no se encuentra devuelve un -1
"""
print(animal.replace("PA", "Pa"))
print("PA" in animal)
"""
la diferencia es que devuelve un boolean cuando encuentra
o no la cadena
"""
print("PA" not in animal)
