def read_input_from_file(file_location):
    with open(file_location, "r") as file:
        lines = file.readlines()
        number_of_slices_max = int(lines[0].split()[0])
        number_of_pizzas = int(lines[0].split()[1])
        pizzas = lines[1].split()
        pizzas = list(map(int, pizzas))
        return number_of_slices_max, number_of_pizzas, pizzas


def write_results_to_file(output_file_location, number_of_different_pizza_types, list_with_numbers_of_pizzas_ordered):
    with open(output_file_location, 'w') as f:
        f.writelines(str(number_of_different_pizza_types) + "\n")
        f.write(" ".join(str(number_of_pizza) for number_of_pizza in list_with_numbers_of_pizzas_ordered))


def get_file_locations(input_file_name):
    output_file_name = input_file_name[:-3] + ".out"
    input_file_location = "../resources/in/" + input_file_name
    output_file_location = "../resources/out/" + output_file_name
    return input_file_location, output_file_location
