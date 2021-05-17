import math


def string_check(choice, options, ):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it locks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Gets list of shapes
def get_shape():

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # ,and possible abbreviations ect>

    valid_shapes = [
        ["triangle", "t", "tri"],
        ["square", "s", "squ"],
        ["rectangle", "rect", "r"],
        ["circle", "circ", "c"]
    ]

    # holds snack order for a single user
    shape_info_list = []

    desired_shape = ""
    while desired_shape != "xxx" or desired_shape != "no":

        shape_row = []

        # ask user for desired snack and put in lowercase
        desired_shape = input("Shape: ").lower()

        # check that string is valid
        shape_choice = string_check(desired_shape, valid_shapes)
        print("Shape Choice: ", shape_choice)

        if desired_shape == "xxx" or desired_shape == "no":
            return shape_info_list

        # ***** Triiiang *****

        if desired_shape == "t" or desired_shape == "tri" or desired_shape == "triangle":
            print("Triiiang")

            t_side_1 = num_check("How long is side 1? ", "Please enter an number more than 0\n", float)
            t_side_2 = num_check("How long is side 2? ", "Please enter an number more than 0\n", float)
            t_side_3 = num_check("How long is side 3? ", "Please enter an number more than 0\n", float)

            print("side 1 is {} {}".format(t_side_1, unit))
            print("side 2 is {} {}".format(t_side_2, unit))
            print("side 3 is {} {}".format(t_side_3, unit))
            
            perimeter = t_side_1 + t_side_2 + t_side_3
            print("perimeter is {} {}".format(perimeter, unit))

            semi_perimeter = perimeter / 2
            part_a = semi_perimeter - t_side_1
            part_b = semi_perimeter - t_side_2
            part_c = semi_perimeter - t_side_3

            area = math.sqrt(semi_perimeter * part_a * part_b * part_c)
            print("area is {:.3f} {}".format(area, unit))

        # ***** squarring *****

        elif desired_shape == "s" or desired_shape == "squ" or desired_shape == "square":
            print("squarring")

            s_side = num_check("How long is one side? ", "Please enter an number more than 0\n", float)

            print("side 1 is {} {}".format(s_side, unit))

            area = s_side * s_side
            print("area is {} {} squared".format(area, unit))

            perimeter = s_side * 4
            print("perimeter is {} {}".format(perimeter, unit))

        # ***** Reeeectannnn *****

        elif desired_shape == "r" or desired_shape == "rect" or desired_shape == "rectangle":
            print("Reeeectannnn")

            r_side_12 = num_check("How long is the length? ", "Please enter an number more than 0\n", float)
            r_side_34 = num_check("How wide is the width? ", "Please enter an number more than 0\n", float)

            print("side 1/2 is {} {}".format(r_side_12, unit))
            print("side 3/4 is {} {}".format(r_side_34, unit))

            area = r_side_12 * r_side_34
            print("area is {} {} squared".format(area, unit))

            perimeter = r_side_12 + r_side_12 + r_side_34 + r_side_34
            print("perimeter is {} {}".format(perimeter, unit))

        # ***** cirrical *****

        elif desired_shape == "c" or desired_shape == "circ" or desired_shape == "circle":
            print("cirrical")

            c_radius = num_check("What is the radius (half of diameter)? ",
                                 "Please enter an number more than 0\n", float)

            print("the radius is {} {}".format(c_radius, unit))

            area = 3.1415926 * c_radius / 2
            print("area is {} {} squared".format(area, unit))

            perimeter = 2 * 3.1415926 * c_radius
            print("perimeter is {} {}".format(perimeter, unit))

        else:
            print("Sorry, That is not a valid shape.")

        # check snack amount it valid (less than 5)

        # add snack and amount to list...

        shape_row.append(shape_choice)

        # check that snack is not the exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice" and shape_choice != "no":
            shape_info_list.append(shape_row)


# valid options for payment method
units_options = [
    ["mm"],
    ["cm"],
    ["m"]
]

unit = "invalid choice"
while unit == "invalid choice":
    unit = input("Please choose your units (mm / cm / m)?").lower()
    unit = string_check(unit, units_options)
    if unit == "invalid choice":
        print("This is not a valid unit.")


shape_order = get_shape()
