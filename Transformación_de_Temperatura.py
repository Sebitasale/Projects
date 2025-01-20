def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)
    else:
        return None


def main():
    print("Este es un convertidor de temperatura.")
    from_unit = input("¿Desde qué unidad de temperatura quiere convertir? (C, F, K): ").strip().upper()
    to_unit = input("¿A qué unidad desea convertir? (C, F, K): ").strip().upper()

    if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
        print("Unidad no válidas. Por favor, intente de nuevo.")
        return

    try:
        value = float(input("Ingrese el valor de la temperatura que desea convertir: "))
        converted_value = convert_temperature(value, from_unit, to_unit)
        print(f"La temperatura convertida de {from_unit} a {to_unit} es: {converted_value:.2f}")
    except ValueError:
        print("Por favor, ingrese un número válido para la temperatura.")


if __name__ == "__main__":
    main()

