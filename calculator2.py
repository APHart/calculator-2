"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

operators = ["+", "-", "*", "/", "square",
             "cube", "pow", "mod", "x+",
             "cubes+", "q"]


while True:
    user_input = raw_input('> ')
    input_tokens = user_input.split(' ')
    num_tokens = input_tokens[1:]

    if input_tokens[0] in operators:

        try:
            for item in num_tokens:
                float(item)

        except ValueError:
            print "Invalid input, numbers must be entered for calculations."
            continue

        if input_tokens[0] == '+':

            add_list = []

            for num in num_tokens:
                num = float(num)
                add_list.append(num)

            add_result = add(add_list)
            print add_result

        elif input_tokens[0] == '-':

            sub_list = []

            for num in num_tokens:
                num = float(num)
                sub_list.append(num)

            sub_result = subtract(sub_list)
            print sub_result

        elif input_tokens[0] == '*':
            mult_result = multiply(float(input_tokens[1]),
                                   float(input_tokens[2]))
            print mult_result

        elif input_tokens[0] == '/':
            div_result = divide(float(input_tokens[1]),
                                float(input_tokens[2]))
            print div_result

        elif input_tokens[0] == 'square':
            sq_result = square(float(input_tokens[1]))
            print sq_result

        elif input_tokens[0] == 'cube':
            cube_result = cube(float(input_tokens[1]))
            print cube_result

        elif input_tokens[0] == 'pow':
            pow_result = power(float(input_tokens[1]),
                               float(input_tokens[2]))
            print pow_result

        elif input_tokens[0] == 'mod':
            mod_result = mod(float(input_tokens[1]),
                             float(input_tokens[2]))
            print mod_result

        elif input_tokens[0] == 'x+':
            add_mult_result = add_mult(float(input_tokens[1]),
                                       float(input_tokens[2]),
                                       float(input_tokens[3]))
            print add_mult_result

        elif input_tokens[0] == 'cubes+':
            add_cubes_result = add_cubes(float(input_tokens[1]),
                                         float(input_tokens[2]))
            print add_cubes_result

        elif user_input == "q":
            print "You will exit."
            break

    else:
        print "Invalid input, please enter an operator or q to quit."
