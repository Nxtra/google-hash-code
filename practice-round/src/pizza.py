from file_util import get_file_locations, write_results_to_file, read_input_from_file


def just_do_it(input_file_location, output_file_location):
    number_of_slices_max, number_of_pizzas, pizzas = read_input_from_file(input_file_location)
    number_of_different_pizza_types, list_with_numbers_of_pizzas_ordered = calculate(number_of_slices_max, pizzas)
    write_results_to_file(output_file_location, number_of_different_pizza_types, list_with_numbers_of_pizzas_ordered)


def calculate(number_of_slices_max, pizzas):
    list_with_numbers_of_pizzas_ordered = []
    number_of_different_pizza_types = 0
    number_of_slices_left_to_fill = number_of_slices_max
    for i, e in reversed(list(enumerate(pizzas))):
        if e <= number_of_slices_left_to_fill:
            list_with_numbers_of_pizzas_ordered.append(i)
            number_of_different_pizza_types += 1
            number_of_slices_left_to_fill -= e

    return number_of_different_pizza_types, list_with_numbers_of_pizzas_ordered[::-1]


if __name__ == "__main__":
    file_names = [
        "a_example.in",
        "b_small.in",
        "c_medium.in",
        "d_quite_big.in",
        "e_also_big.in"
    ]
    for file_name in file_names:
        input_file_location, output_file_location = get_file_locations(file_name)
        just_do_it(input_file_location, output_file_location)
