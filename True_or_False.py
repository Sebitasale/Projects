from email.header import SPACE
from itertools import combinations

x = 1
y = 2

a = (x == 1) and (y == 3)
b = (x < y) or (x > 1)
c = not ((x == 1) and (y == 2))

print("a = (x == 1) and (y == 3):", a)
print("b = (x < y) or (x > 1):", b)
print("c = not ((x == 1) and (y == 2)):", c)

valores = [ (True, True, True), (True, True, False),
            (True, False, True), (False, True, True),
           (True, False, False), (False, True, False),
           (False, False, True), (False, False, False)]
print("A\tB\tC\t ((Not A) AND B) OR C")
print("-" * 30)

for A, B, C in valores:
    resultado = ((not A) and B) or C
    print(f"{A}\t {B}\t {C}\t{resultado}")

x = 5
y = 10
z = 15
resultado = (x == 5 and y == 11) or ([x + y] == z)
print(f"Resultado Ejercicio N.3: {resultado} ")

x = 69
y = 13
resultado = (0 <= x <= 100 and 0 <= y <= 100 and x != y)
print(f"Resultado Ejercicio N.4: {resultado} ")

score = 150
resultado = not (200 <= score <= 800)
print(f"Resultado Ejercicio N.5: {resultado} ")

valores = (True, True), (True, False), (False, True), (False, False)

print(f"A\tB\tResultado")
for A, B in valores:
    print(f"{A}\t{B}\t: {resultado}")

combinaciones = [ (True, True), (True, False), (False,True), (False, False)]
print("Figura 4.22 - Resultados para todas las combinaciones de a y b:")
print(" a| b | c | d ")
print("--|---|---|--")
for a, b in combinaciones:
    c = a or b
    d = not (a and not b)
    print(f"{int(a)} | {int(b)} | {int (c)} | {int (d)}")

from prettytable import PrettyTable

tabla = PrettyTable()
tabla.field_names = ["a", "b", "c", "d"]

combinaciones = [ (0,0), (0, 1), (1,0), (1, 1)]

for a, b in combinaciones:
    c = a or b
    d = not (a and not b)

    tabla.add_row([a, b, int(c), int(d)])

print(tabla.get_string(border=False, header=True, padding_width=1))

print("Figura 4.23 - Resultados con a=1 y b=0:")
print("Salida c:", int(c))
print("Salida d:", int(d))

from prettytable import PrettyTable

tabla = PrettyTable()
tabla.field_names = ["a", "b", "c", "Output-1"]
for a in [0,1]:
    for b in [0, 1]:
        for c in [0, 1]:

            term1 = int((not a) and b and (not c))
            term2 = int(a and b and (not c))
            output_1 = int(term1 or term2)

            tabla.add_row([a, b, c, output_1])

print(tabla.get_string(border=False, header=True, padding_width=1))

def xor(a, b):
    term1 = (a and not b)
    term2 = (not a and b)
    output = term1 or term2
    return int(output)

print("a | b | Output (XOR)")
print("---------------------")
for a in [0, 1]:
    for b in [0, 1]:
        result = xor(a, b)
        print(f"{a} | {b} |    {result}")

def full_on_full_off(a, b, c):
    term1 = (not a and not b and not c)
    term2 = (a and b and c)
    output = term1 or term2
    return int(output)

print("a | b | c | Output (Full-ON/Full-OFF)")
print("--------------------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            result = full_on_full_off(a, b, c)
            print(f"{a} | {b} | {c} |           {result}")
