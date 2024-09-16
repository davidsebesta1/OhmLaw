def calculate_resistance(current, voltage):
    if current == 0:
        print("Proud nesmi byt nula při vypoctu odporu.")
        return None
    return voltage / current

def calculate_voltage(current, resistance):
    raise NotImplementedError

def calculate_current(voltage, resistance):
    raise NotImplementedError

def get_valid_number_input(request):
    res = 0.0
    is_valid = False
    while not is_valid:
        try:
            res = float(input(request))
        except ValueError:
            print("Zadany vstup neni cislo")
        else:
            is_valid = True

    return res

letter_to_calculation_function = {"I": calculate_current, "U": calculate_voltage, "R": calculate_resistance}

user_input = ""
while user_input not in letter_to_calculation_function:
    user_input = input("Zadejte, co chcete vypocitat (R,U,I) podle ohmova zakona: ")

calculation_params = []
for key in letter_to_calculation_function:
    if user_input == key:
        continue
    number = get_valid_number_input(f"Zadejte hodnotu pro {key}: ")
    calculation_params.append(number)

result = letter_to_calculation_function[user_input](calculation_params[0], calculation_params[1])
if result is not None:
    print(f"{user_input} = {result}")