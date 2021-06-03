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


def yes_no(question):

    # the 2 end available answers
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


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
        ["circle", "circ", "c"],
        ["parallelogram", "paro", "p"]
    ]

    bh_or_sides = [
        ["base and height", "b&h", "b & h", "bh", "b"],
        ["sides", "s", "side"]
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
            print()
            return shape_info_list

        # ***** Triiiang *****

        if shape_choice == "Triangle" or shape_choice == "Parallelogram":
            print("Triiiang")
            print("parrrooolll")

            desired_loop = ""
            while desired_loop != "xxx" or desired_loop != "no":

                desired_enter = input("Do You have the base and height, or the sides?").lower()

                enter_choice = string_check(desired_enter, bh_or_sides)
                print("Your Choice: ", enter_choice)

                if enter_choice == "Sides":

                    print()
                    int_float = yes_no("Does it have any .'s ?")
                    if int_float == "Yes":
                        num_type = float
                    else:
                        num_type = int
                    print()

                    t_side_1 = num_check("How long is side 1? ", "Please enter an number more than 0\n", num_type)
                    t_side_2 = num_check("How long is side 2? ", "Please enter an number more than 0\n", num_type)
                    if shape_choice == "Triangle":
                        t_side_3 = num_check("How long is side 3? ", "Please enter an number more than 0\n", num_type)

                    print("side 1 is {} {}".format(t_side_1, unit))
                    print("side 2 is {} {}".format(t_side_2, unit))
                    if shape_choice == "Triangle":
                        print("side 3 is {} {}".format(t_side_3, unit))

                    if shape_choice == "Triangle":
                        perimeter = t_side_1 + t_side_2 + t_side_3
                    else:
                        perimeter = t_side_1 + t_side_1 + t_side_2 + t_side_2
                    print("perimeter is {} {}".format(perimeter, unit))

                    semi_perimeter = perimeter / 2
                    part_a = semi_perimeter - t_side_1
                    part_b = semi_perimeter - t_side_2
                    part_c = semi_perimeter - t_side_3

                    if shape_choice == "Triangle":
                        area = math.sqrt(semi_perimeter * part_a * part_b * part_c)
                    else:
                        area = ("n/a")
                    print("area is {} {} squared".format(area, unit))
                    break

                elif enter_choice == "Base And Height":

                    print()
                    int_float = yes_no("Does it have any .'s ?")
                    if int_float == "No":
                        num_type = int
                    else:
                        num_type = float
                    print()

                    base = num_check("What is the base?", "Please enter an number more than 0\n", num_type)
                    height = num_check("What is the height?", "Please enter an number more than 0\n", num_type)

                    if shape_choice == "Triangle":
                        perimeter = ("n/a")
                    else:
                        perimeter_1 = base + height
                        perimeter = perimeter_1 * 2
                    print("perimeter is {} {}".format(perimeter, unit))

                    if shape_choice == "Triangle":
                        area = base/2 * height
                    else:
                        area = base * height
                    print("area is {} {} squared".format(area, unit))

                else:
                    print("Sorry, That is not a valid input.")

        elif shape_choice == "Circle":
            circle = shape_circle()

        # ***** Reeeectannnn / squarring *****

        elif shape_choice == "Square" or shape_choice == "Rectangle":
            squrec = shape_squrec()

        else:
            print("Sorry, That is not a valid shape.")

        # check snack amount it valid (less than 5)

        # add snack and amount to list...

        shape_row.append(shape_choice)

        # check that snack is not the exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice" and shape_choice != "no":
            shape_info_list.append(shape_row)

        # return(shape_choice)


def shape_circle():

    # ***** cirrical *****

    print("cirrical")

    print()
    int_float = yes_no("Does it have any .'s ?")
    if int_float == "No":
        num_type = int
    else:
        num_type = float
    print()

    c_radius = num_check("What is the radius (half of diameter)? ",
                         "Please enter an number more than 0\n", num_type)

    print("the radius is {} {}".format(c_radius, unit))

    perimeter = 2 * 3.1415926 * c_radius
    print("perimeter is {} {}".format(perimeter, unit))

    area = c_radius ** 2 * 3.1415926
    print("area is {} {} squared".format(area, unit))
    return()


def shape_squrec():
    print("squarring")
    print("Reeeectannnn")

    print()
    int_float = yes_no("Does it have any .'s ?")
    if int_float == "No":
        num_type = int
    else:
        num_type = float
    print()

    r_side_12 = num_check("How long is it? ", "Please enter an number more than 0\n", num_type)
    if get_shape == "Rectangle":
        r_side_34 = num_check("How wide is it? ", "Please enter an number more than 0\n", num_type)

    print("side 1/2 is {} {}".format(r_side_12, unit))

    if get_shape == "Rectangle":
        print("side 3/4 is {} {}".format(r_side_34, unit))
    else:
        r_side_34 = r_side_12

    perimeter = r_side_12 + r_side_12 + r_side_34 + r_side_34
    print("perimeter is {} {}".format(perimeter, unit))

    area = r_side_12 * r_side_34
    print("area is {} {} squared".format(area, unit))

    return()


# valid options for payment method
units_options = [
    ["mm"],
    ["cm"],
    ["m"]
]

unit = "invalid choice"
while unit == "invalid choice":
    unit = input("Please choose your units (mm / cm / m)?").lower()
    unit = string_check(unit, units_options).lower()
    if unit == "invalid choice":
        print("This is not a valid unit.")


shape_order = get_shape()
