
"""
! En Python tenemos los siguientes tipos de objetos: 

Números, cadenas, listas, diccionarios, tuplas, conjuntos. 

"""

#? Numeros: Intergers, float, boolean.


# numeros del tipo int, float. Variables del tipo string y bool.
1 + 1 # es una expresion (dos enteros y un operador).
b = 3 + 1 # es una sentecia formada por una expresion y un operador(=).
"""
Se llama expresion de asignacion o simplemente asignacion. b se convierte en un objeto del
universo de python. En Python no hay declaracion de variables
codigo con sentido.
"""
print(b) # sentencia funcion interna print.
print(type(b)) #La función internet "type" retorna el tipo de objeto que se le entregue a la función
#Variable a, b.
#&este = 5
in_d = 2
#print(_ind)

b = b*2.0 # ahora b es float y * es un operador
print(b)

str1 = 'Press return to exit'  #cadenas de caracteres
str2 = "the program"
print("concatenando los dos string:", str1+' '+str2) # concatenation de cadenas de texto
print("Haciendo slicing al primer string:", str1[0:11+1]) # slicing 
#la cadena es un objeto del tipo iterable inmutable.
print('yo "no estoy" aqui') #apantallamiento
print("yo \"no estoy\" aqui")
print('viene bien \n dormir') # separar en nuevo renglon

s = '3 9 81'
print(s.split()) # funcion como atributo de una varible con el operador punto.
"""
Este método toma una cadena y la divide en una lista de subcadenas utilizando un 
separador (por defecto, el separador es el espacio en blanco). Dado que no se proporciona ningún 
argumento al método split(), se utiliza el separador predeterminado (el espacio en blanco).
"""

#? lista es iterable, obj de dif. naturaleza, es mutable.

#Lista, las definimos con corchetes  "[]" 
a = [1, 2.0, 3.0, True, 'ab'] # crear una lista
a.append(4.0) # agregar 4.0 a la lista (se agrega en la última posición)
print(a)
a.insert(0, 10) # inserte 10 en la posicion 0 (sobre escribe el valor qeu haya en esa posición)
print(a)
print(len(a))
a[2:4] = [1.0, 1.0, 1.0] #agregar elementos
print(a)


for _ in a:   #Como mencionamos anteriormente, las listas son iterables y las iteramos asi:
    print(a)
    
#? tupla. objetos iterables, inmutable. [], (), {}

#La tupla se asemeja a la listas pero, la principal diferencia es que son Inalterables. No se puede cambiar sus valores 
#Las Tuplas se definen con parentesis "()"
x = (2,)
rec = ('Smith', 'John',  (6, 23, 68))
lastname, firstname, birthdate = rec #asignacion multiple.
print(firstname)
birthYear = birthdate[2]
birthday = birthdate[1]
print(birthYear)
print(birthday)
name = rec[1]+' '+rec[0]
print(name)
print(rec[0:2])

#? Diccionarios se definen con llaves "{}"

pop_dict = {'Calif': 38332521, 'Texas' : 26448193, 'New York' : 19651127}
print(pop_dict)
