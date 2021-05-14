

def string_check(choice, options):

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

        if desired_shape == "xxx" or desired_shape == "no":
            return shape_info_list

        elif desired_shape == "t" or desired_shape == "tri" or desired_shape == "triangle":
            print("Triiiang")

            side_1 = num_check("How long is side 1?", "Please enter an number more than 0\n", float)
            side_2 = num_check("How long is side 2?", "Please enter an number more than 0\n", float)
            side_3 = num_check("How long is side 1?", "Please enter an number more than 0\n", float)

            print("side 1 is {} {}".format(side_1, unit_choice))
            print("side 2 is {} {}".format(side_2, unit_choice))
            print("side 3 is {} {}".format(side_3, unit_choice))
            
            area = ("n/a")
            print(area)
            
            perimeter = side_1 + side_2 + side_3
            print("perimeter is {} {}".format(perimeter, unit_choice))

        else:
            print("Sorry, That is not a valid shape.")

        # remove white space around snack
        desired_shape = desired_shape.strip()

        # check that string is valid
        shape_choice = string_check(desired_shape, valid_shapes)
        print("Shape Choice: ", shape_choice)

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

unit_choice = "invalid choice"
while unit_choice == "invalid choice":
    unit_choice = input("Please choose your units (mm / cm / m)?").lower()
    unit_choice = string_check(unit_choice, units_options)

shape_order = get_shape()
