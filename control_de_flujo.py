
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
naturales = []
a=1

while a < 101:
  #print(a)
  naturales.append(a)
  a += 1
#print (naturales)


"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""

acumulado = []
b = 2
x = '1'

acumulado.append(x)

while b < 51:

  if b == 2:
    x = x + ' ' + str( b )
    acumulado.append(x)
    b += 1
    continue  

  x = x + ' ' + str( b )
  #print(x)
  acumulado.append(x)
  b += 1

#print(acumulado)


"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""

s = 1
suma100 = 0

while s < 101:
  suma100 = suma100 + s
  #print(suma100)
  s += 1


"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""

#tabla100

tabla100 = '134'

for i in range(2, 11):
  tabla100 = tabla100 + ',' + str(134 * i)

#print(tabla100)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

multiplos3_1 = []

for x in lista1:

  if( int(x) < 300 ):
    if ( int(x)%3 == 0):
      multiplos3_1.append(x)

multiplos3 = len(multiplos3_1)
#print(multiplos3)





"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""

regresivo50 = []
l = len(acumulado) -1
s = 0


for i in reversed ( range (1, 52) ):
  x = ''
  for j in reversed ( range (1, i) ):
    if( j == i ):
      x = j
    else:
      x = x + ' ' + str(j)
  if ( x.lstrip() == ''):
    print('')
  else:          
    regresivo50.append(x.lstrip())

#print(regresivo50)



"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
#print(lista2)
invertido =[]
l = len(lista2) -1

for f in range(0, len(lista2)):
  invertido.append(lista2[l-f])
#print (invertido)



"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""

primos = []
nmax = 300
for x in range(3, nmax):
    for i in range(2, x):
        if x%i != 0:
            #i no es divisor de x, x puede ser primo
            continue
        else:
            #i es divisor de x, x no es primo
            break #No es necesario buscar más divisores
    else:
        #El bucle for ha terminado con normalidad
        #El número que estábamos comprobando es primo
        #print ('%d es primo'%x)
        if ( x >= 37):
          primos.append(x)

#print(primos)

"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""

num=58
fibonacci = [0,1]
a=0
b=1

for y in range(num):
  c=a+b
  fibonacci.append(c)
  a=b
  b=c

#print(fibonacci)

"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""

factorial_1 = []
aa = 1

for o in range(1, 31):
  aa = aa * o
  factorial_1.append(aa)

factorial = factorial_1[len(factorial_1)-1]
#print(factorial)




"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]


pares = []

for i in range(81):
  if ( i%2 == 0):
    pares.append(lista3[i])

#print (pares)
"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""

cubos = []

for i in range(1, 101):
  cubos.append(i**3)
#print(cubos)



"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""

x='2'
list_x = []
suma_2s = 0

for i in range(1, 11):
  if (i == 1):
    list_x.append(x)
  else:
    x = x + '2'  
    list_x.append(x)

for j in range(len(list_x)):
  suma_2s = suma_2s + int(list_x[j])
  #print (list_x[j])

#print (suma_2s)

"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""

x='*'
patron='*'

for i in range(2, 31):
  patron = patron + '\n' + ( x * i )

for i in reversed( range(1, 30) ):
  patron = patron + '\n' + ( x * i )

print(patron)

