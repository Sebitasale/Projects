
def a_base_10(numero, base_origen):
    numero_en_base_10 = 0
    potencia = 0
    for digito in reversed(numero):
        numero_en_base_10 += int(digito) * (base_origen ** potencia)
        potencia += 1
    return numero_en_base_10

def de_base_10_a_otra_base(numero, base_destino):
    resultado = ''
    while numero > 0:
        resultado = str(numero % base_destino) + resultado
        numero //= base_destino
    return resultado

numero = input("ingrese un número: ")
base_origen=int(input("ingrese la base de origen 2,3,4,5,6,7,8,9,10 o 16: "))
base_destino=int(input("ingrese la base de destino 2,3,4,5,6,7,8,9,10 o 16: "))

if base_origen != 10:
    numero_en_base_10 = a_base_10(numero, base_origen)
else:
    numero_en_base_10 = int(numero)

if base_destino != 10:
    resultado = de_base_10_a_otra_base(numero_en_base_10, base_destino)
else:
    resultado = str(numero_en_base_10)

print(f"El número {numero} en base {base_origen} convertido a base {base_destino} es {resultado}")
