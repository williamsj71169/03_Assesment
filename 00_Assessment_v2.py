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

    # Square and Rectangle:

    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")

    all_units.append(unit)

    round_to = num_check("Round to how many dp??", "Can't be zero", int)

    side_12 = num_check("How long is it? ", "Please enter an number more than 0\n", float)
    if shape == "Rectangle":
        side_34 = num_check("How wide is it? ", "Please enter an number more than 0\n", float)
    else:
        side_34 = 0

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
    all_perimeters.append(perimeter)

    v1_area = r_side_12 * r_side_34
    area = round(v1_area, round_to)
    print("area is {} {} squared".format(area, unit))
    all_areas.append(area)

    return()


def shape_circle():

    # Circle:

    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")
        else:
            all_units.append(unit)

    round_to = num_check("Round to how many dp??(>1)", "Can't be zero", int)

    c_radius = num_check("What is the radius (half of diameter)? ", "Please enter an number more than 0\n", float)

    c_radius_2 = round(c_radius, round_to)
    print("the radius is {} {}".format(c_radius_2, unit))

    perimeter = 2 * 3.1415926 * c_radius
    c_perimeter = round(perimeter, round_to)
    print("perimeter is {} {}".format(c_perimeter, unit))
    all_perimeters.append(c_perimeter)

    area = c_radius ** 2 * 3.1415926
    c_area = round(area, round_to)
    print("area is {} {} squared".format(c_area, unit))
    all_areas.append(c_area)

    return()


def shape_tripar(shape2):

    # Triangle and Parallelogram:

    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")

    all_units.append(unit)

    round_to = num_check("Round to how many dp??", "Can't be zero", int)

    bh_or_sides = [
        ["base and height", "b&h", "b & h", "bh", "b", "base", "height", "h"],
        ["sides", "s", "side"]
    ]

    desired_loop = ""
    while desired_loop != "xxx" or desired_loop != "no":

        desired_enter = input("Do You have the base and height (bh), or the sides (s)?").lower()

        enter_choice = string_check(desired_enter, bh_or_sides)
        print("Your Choice: ", enter_choice)

        if enter_choice == "Sides":

            t_side_1 = num_check("How long is side 1? ", "Please enter an number more than 0\n", float)
            t_side_2 = num_check("How long is side 2? ", "Please enter an number more than 0\n", float)
            if shape2 == "Triangle":
                t_side_3 = num_check("How long is side 3? ", "Please enter an number more than 0\n", float)
            else:
                t_side_3 = 0

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
            all_perimeters.append(pt_perimeter)

            if shape2 == "Triangle":
                semi_perimeter = perimeter / 2
                part_a = semi_perimeter - t_side_1
                part_b = semi_perimeter - t_side_2
                part_c = semi_perimeter - t_side_3
            else:
                semi_perimeter = 0
                part_a = 0
                part_b = 0
                part_c = 0
                print()

            if shape2 == "Triangle":
                pt_area = math.sqrt(semi_perimeter * part_a * part_b * part_c)
                area = round(pt_area, round_to)
            else:
                area = "n/a"
            print("area is {} {} squared".format(area, unit))
            all_areas.append(area)

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
            all_perimeters.append(perimeter)

            if shape2 == "Triangle":
                area = base / 2 * height
            else:
                area = base * height
            pt_area = round(area, round_to)
            print("area is {} {} squared".format(pt_area, unit))
            all_areas.append(pt_area)

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

    desired_shape = ""
    while desired_shape != "xxx" or desired_shape != "no":

        # ask user for desired snack and put in lowercase
        print()
        print("Shape Options: circle, square, rectangle, triangle or parallelogram")
        desired_shape = input("Your Shape: ").lower()

        # check that string is valid
        shape_choice = string_check(desired_shape, valid_shapes)

        if desired_shape == "xxx" or desired_shape == "no":
            print()
            return()

        if shape_choice != "invalid choice":
            all_shapes.append(shape_choice)

        if shape_choice == "Triangle" or shape_choice == "Parallelogram":
            tripar = shape_tripar(shape_choice)

        elif shape_choice == "Circle":
            circle = shape_circle()

        elif shape_choice == "Square" or shape_choice == "Rectangle":
            squrec = shape_squrec(shape_choice)

        else:
            print("Sorry, That is not a valid shape.")

        # add snack and amount to list...
        # return()


# function to show instructions if necessary
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = yes_no("*** Would you like to read the instructions? (y/n) *** ")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("*** Instructions ***")
        print()
        print("* Choose your shape and add in its sides lengths, or its base and height"
              "(for parallelogram and triangle only), and you will receive the area and perimeter in the units that"
              "you provided. *")

    return ""

# valid options for payment method
units_options = [
    ["mm"],
    ["cm"],
    ["m"]
]

# valid options for yes/no questions
y_n = [
    ["yes", "y"],
    ["no", "n"]
]

# initialize lists (to make data-frames in due course)
all_shapes = []
all_areas = []
all_perimeters = []
all_units = []

# lists to store summary data...
summary_headings = ["Shape"]
summary_data = []


# data frame dictionary
shape_data_dict = {
    'Shape': all_shapes,
    'Area': all_areas,
    'Perimeter': all_perimeters,
    'Unit': all_units
}


instructions(y_n)


shape_order = get_shape()


# create data frame and set index to name column
shape_frame = pandas.DataFrame(shape_data_dict)
shape_frame = shape_frame.set_index('Shape')


# write data to file
write_to_file = yes_no("Would you like the data writen to file? (y/n) ")
if write_to_file == "yes":

    # write to file...
    # create file to hold data (add .txt extension)
    file_name_choice = input("What would you lke your file named?")
    file_name = "{}.txt".format(file_name_choice)
    text_file = open(file_name, "w+")
    print("Your File was called: {}.txt ".format(file_name_choice))

    # heading
    text_file.write("*** {} ***\n\n".format(file_name_choice))

    text_file.write("{}".format(shape_frame))

    # close file
    text_file.close()


# *** Printing area ***

print()
print("*** Maths!! ***")
print()

print()
print(shape_frame)
print()
