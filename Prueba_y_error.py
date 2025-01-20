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
