import math
import pandas


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


def shape_squrec(shape):

    shape_list = []
    area_list = []
    perimeter_list = []

    shape_list.append(shape)

    # ***** Reeeectannnn / squarring *****

    print("squarring")
    print("Reeeectannnn")

    round_to = num_check("Round to nearest...? ", "Can't be zero", int)

    side_12 = num_check("How long is it? ", "Please enter an number more than 0\n", float)
    if shape == "Rectangle":
        side_34 = num_check("How wide is it? ", "Please enter an number more than 0\n", float)

    r_side_12 = round(side_12, round_to)
    print("side 1/2 is {} {}".format(r_side_12, unit))

    if shape == "Rectangle":
        r_side_34 = round(side_34, round_to)
        print("side 3/4 is {} {}".format(r_side_34, unit))
    else:
        r_side_34 = r_side_12

    v1_perimeter = r_side_12 + r_side_12 + r_side_34 + r_side_34
    perimeter = round(v1_perimeter, round_to)
    print("perimeter is {} {}".format(perimeter, unit))

    v1_area = r_side_12 * r_side_34
    area = round(v1_area, round_to)
    print("area is {} {} squared".format(area, unit))

    area_list.append(area)
    perimeter_list.append(perimeter)

    return()


def shape_circle():

    # ***** cirrical *****

    print("cirrical")

    round_to = num_check("Round to nearest...? ", "Can't be zero", int)

    c_radius = num_check("What is the radius (half of diameter)? ", "Please enter an number more than 0\n", float)

    c_radius_2 = round(c_radius, round_to)
    print("the radius is {} {}".format(c_radius_2, unit))

    perimeter = 2 * 3.1415926 * c_radius
    c_perimeter = round(perimeter, round_to)
    print("perimeter is {} {}".format(c_perimeter, unit))

    area = c_radius ** 2 * 3.1415926
    c_area = round(area, round_to)
    print("area - {}".format(area))
    print("area is {} {} squared".format(c_area, unit))
    return()


def shape_tripar(shape2):

    # ***** Triiiang ****

    round_to = num_check("Round to nearest...? ", "Can't be zero", int)

    print("Triiiang")
    print("parrrooolll")

    bh_or_sides = [
        ["base and height", "b&h", "b & h", "bh", "b"],
        ["sides", "s", "side"]
    ]

    desired_loop = ""
    while desired_loop != "xxx" or desired_loop != "no":

        desired_enter = input("Do You have the base and height, or the sides?").lower()

        enter_choice = string_check(desired_enter, bh_or_sides)
        print("Your Choice: ", enter_choice)

        if enter_choice == "Sides":

            t_side_1 = num_check("How long is side 1? ", "Please enter an number more than 0\n", float)
            t_side_2 = num_check("How long is side 2? ", "Please enter an number more than 0\n", float)
            if shape2 == "Triangle":
                t_side_3 = num_check("How long is side 3? ", "Please enter an number more than 0\n", float)

            t_side_12 = round(t_side_1, round_to)
            t_side_22 = round(t_side_2, round_to)
            print("side 1 is {} {}".format(t_side_12, unit))
            print("side 2 is {} {}".format(t_side_22, unit))
            if shape2 == "Triangle":
                t_side_32 = round(t_side_3, round_to)
                print("side 3 is {} {}".format(t_side_32, unit))

            if shape2 == "Triangle":
                perimeter = t_side_1 + t_side_2 + t_side_3
            else:
                perimeter = t_side_1 + t_side_1 + t_side_2 + t_side_2
            pt_perimeter = round(perimeter, round_to)
            print("perimeter is {} {}".format(pt_perimeter, unit))

            if shape2 == "Triangle":
                semi_perimeter = perimeter / 2
                part_a = semi_perimeter - t_side_1
                part_b = semi_perimeter - t_side_2
                part_c = semi_perimeter - t_side_3
            else:
                print()

            if shape2 == "Triangle":
                pt_area = math.sqrt(semi_perimeter * part_a * part_b * part_c)
                area = round(pt_area, round_to)
            else:
                area = "n/a"
            print("area is {} {} squared".format(area, unit))
            break

        elif enter_choice == "Base And Height":

            base = num_check("What is the base?", "Please enter an number more than 0\n", float)
            height = num_check("What is the height?", "Please enter an number more than 0\n", float)

            base_2 = round(base, round_to)
            height_2 = round(height, round_to)
            print("the base is {} {} squared".format(base_2, unit))
            print("the height is {} {} squared".format(height_2, unit))

            if shape2 == "Triangle":
                perimeter = "n/a"
            else:
                perimeter_1 = base + height
                pt_perimeter = perimeter_1 * 2
                perimeter = round(pt_perimeter, round_to)
            print("perimeter is {} {}".format(perimeter, unit))

            if shape2 == "Triangle":
                area = base / 2 * height
            else:
                area = base * height
            pt_area = round(area, round_to)
            print("area is {} {} squared".format(pt_area, unit))

        else:
            print("Sorry, That is not a valid input.")

        return ()


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

        if shape_choice == "Triangle" or shape_choice == "Parallelogram":
            tripar = shape_tripar(shape_choice)

        elif shape_choice == "Circle":
            circle = shape_circle()

        elif shape_choice == "Square" or shape_choice == "Rectangle":
            squrec = shape_squrec(shape_choice)

        else:
            print("Sorry, That is not a valid shape.")

        # check snack amount it valid (less than 5)

        # add snack and amount to list...

        shape_row.append(shape_choice)

        # check that snack is not the exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice" and shape_choice != "no":
            shape_info_list.append(shape_row)

        return[shape_choice]


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("*** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


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

# write data to file
write_to_file = yes_no("Would you like the data writen to file? (y/n) ")
if write_to_file == "yes":

    # variable_txt = pandas.DataFrame.to_string(variable_frame)
    # fixed_txt = pandas.DataFrame.to_string()

    # write to file...
    # create file to hold data (add .txt extension)
    file_name = "maths.txt"
    text_file = open(file_name, "w+")

    # heading
    text_file.write("*** Maths ***\n\n")

    # list holding stuff to print / write to file
    # to_write = [variable_txt, fixed_txt]

    # heading
    # for item in to_write:
    #     text_file.write(str(item))
    #     text_file.write("\n\n")

    # shape
    shape_write = "Shape: {} \n ".format(get_shape())
    text_file.write(shape_write)

    # close file
    text_file.close()

else:
    print()


# *** Printing area ***

print()
print("*** Maths!! ***")
print()
# expense_print("Variable", variable_frame, variable_sub)


print()
print("*** Shape 1: $ ***")
print()

print()
print("*** Pricing ***")
print("Minimum Price: $")
print("Recommended Price: $")
