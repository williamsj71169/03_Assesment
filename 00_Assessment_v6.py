# imports go here
import math
import pandas


# ***** Functions Go Here *****


# string checker
def string_check(choice, options, ):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the shape is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of shape and put it
            # in title case so it locks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen shape is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# checks that input is either a float or an integer that is more than or equal to zero
# takes in custom error messages.
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if question == "Round to how many dp??":
                if response >= -1:
                    return response

            elif response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# checks that user has entered yes / no to a question
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

        # error message
        print("Please enter either yes or no...\n")


# sets up the frame for the calculation outputs
def calc_print(heading, letter, number, unit, equation, step_1, ur_answer, r_answer, rounded, letter2, number2,
               letter3, number3, choice, t_s_p):
    print()
    # allows for multiple letter-number transitions
    if heading == "Rectangle Perimeter" or heading == "Rectangle Area" or heading == "Parallelogram Perimeter"\
            or heading == "Parallelogram Area":
        others = ", ({} = {}{})".format(letter2, number2, unit)
    elif heading == "Triangle Area" or heading == "Triangle Perimeter":
        if choice == "bh":
            others = ", ({} = {}{})".format(letter2, number2, unit)
        else:
            others = ", ({} = {}{}), ({} = {}{})".format(letter2, number2, unit, letter3, number3, unit)
    else:
        others = ""
    print("* {} ({} = {}{}){}: *".format(heading, letter, number, unit, others))
    print()
    if heading == "Triangle Area" and choice == "":
        print("p = perimeter / 2")
        print("p = {}".format(t_s_p))
        print()
    print("{}".format(equation))
    print("= {}".format(step_1))
    print("= {} (unrounded)".format(ur_answer))
    print("= {} ({} dp)".format(r_answer, rounded))
    print()
    if heading == "Triangle Area" or heading == "Rectangle Area" or heading == "Circle Area" \
            or heading == "Parallelogram Area" or heading == "Square Area":
        units = "{}²".format(unit)
    else:
        units = unit
    print("* {} = {} {} *".format(heading, r_answer, units))
    print()

    return ""


# function for Square and Rectangle
def shape_squrec(shape):

    # Square and Rectangle:

    # asks for units
    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")

    # asks how many dp to round the answer to
    round_to = num_check("Round to how many dp??", "Must be a whole number more than or equal to 0", int)

    side_12 = num_check("How long is it? ", "Please enter an number more than 0\n", float)
    if shape == "Rectangle":
        side_34 = num_check("How wide is it? ", "Please enter an number more than 0\n", float)
    else:
        side_34 = 0

    print(side_12)
    print("side 1/2 is {} {}".format(side_12, unit))

    if shape == "Rectangle":

        print("side 3/4 is {} {}".format(side_34, unit))
    else:
        side_34 = side_12

    v1_perimeter = side_12 + side_12 + side_34 + side_34

    if round_to == 0:
        perimeter = ("{:.0f}".format(v1_perimeter))
    else:
        perimeter = round(v1_perimeter, round_to)

    if shape == "Rectangle":
        equation = "s1 + s1 + s2 + s2"
        step_1 = "{} + {} + {} + {}".format(side_12, side_12, side_34, side_34)
    else:
        equation = "s x 4"
        step_1 = "{} x 4".format(side_12)

    calc_print("{} Perimeter".format(shape), "s1", side_12, unit, equation, step_1, v1_perimeter, perimeter, round_to,
               "s2", side_34, "", "", "", "")

    perimeter_u = "{} {}".format(perimeter, unit)

    all_perimeters.append(perimeter_u)

    v1_area = side_12 * side_34

    if round_to == 0:
        area = ("{:.0f}".format(v1_area))
    else:
        area = round(v1_area, round_to)

    if shape == "Rectangle":
        num = "s2"
        extra = "1"
    else:
        num = "s"
        extra = ""

    calc_print("{} Area".format(shape), "s", side_12, unit, "s{} x {}".format(extra, num),
               "{} x {}".format(side_12, side_34), v1_area, area, round_to, "s2", side_34, "", "", "", "")

    area_u = "{} {}²".format(area, unit)

    all_areas.append(area_u)

    return()


# function for Circle
def shape_circle():

    # Circle:

    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")

    round_to = num_check("Round to how many dp??", "Must be a whole number more than or equal to 0", int)

    c_radius = num_check("What is the radius (half of diameter)? ", "Please enter an number more than 0\n", float)

    print("The radius is {} {}".format(c_radius, unit))

    circumference = 2 * 3.1415926 * c_radius

    if round_to == 0:
        c_circumference = ("{:.0f}".format(circumference))
    else:
        c_circumference = round(circumference, round_to)

    calc_print("Circle Circumference", "r", c_radius, unit, "2 x pi x r",
               "2 x pi x {}".format(c_radius), circumference, c_circumference, round_to, "", "", "", "", "", "")

    c_circumference_u = "{} {}".format(circumference, unit)

    all_perimeters.append(c_circumference_u)

    area = c_radius ** 2 * 3.1415926

    if round_to == 0:
        c_area = ("{:.0f}".format(area))
    else:
        c_area = round(area, round_to)

    calc_print("Circle Area", "r", c_radius, unit, "(r x r) x pi",
               "({} x {}) x pi".format(c_radius, c_radius), area, c_area, round_to, "", "", "", "", "", "")

    c_area_u = "{} {}²".format(c_area, unit)

    all_areas.append(c_area_u)

    return()


# function for Triangle and Parallelogram
def shape_tripar(shape2):
    # Triangle and Parallelogram:

    unit = "invalid choice"
    while unit == "invalid choice":
        unit = input("Please choose your units (mm / cm / m)?").lower()
        unit = string_check(unit, units_options).lower()
        if unit == "invalid choice":
            print("This is not a valid unit.")

    round_to = num_check("Round to how many dp??", "Can't be zero", int)

    bh_or_sides = [
        ["base and height", "b&h", "b & h", "bh", "b", "base", "height", "h"],
        ["sides", "s", "side"],
        ["base, height, side", "base, height and 1 side", "bhs"]
    ]

    desired_loop = ""
    while desired_loop != "xxx" or desired_loop != "no":

        if shape2 == "Triangle":
            desired_enter = input("Do you have the base and height (bh), or the sides (s)?").lower()
        else:
            desired_enter = input("Do you have: base and height(bh), 2 sides(s) or the base, height and 1 side(bhs)? ")

        enter_choice = string_check(desired_enter, bh_or_sides)

        if enter_choice == "Sides":

            t_side_1 = num_check("How long is side 1? ", "Please enter an number more than 0\n", float)
            t_side_2 = num_check("How long is side 2? ", "Please enter an number more than 0\n", float)
            if shape2 == "Triangle":
                t_side_3 = num_check("How long is side 3? ", "Please enter an number more than 0\n", float)
            else:
                t_side_3 = 0

            print("side 1 is {} {}".format(t_side_1, unit))
            print("side 2 is {} {}".format(t_side_2, unit))
            if shape2 == "Triangle":
                print("side 3 is {} {}".format(t_side_3, unit))

            perimeter = t_side_1 + t_side_2 + t_side_3

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
                try:
                    pt_area = math.sqrt(semi_perimeter * part_a * part_b * part_c)
                except ValueError:
                    print("A triangle with these measurements can not exist.")
                    break
                if round_to == 0:
                    area = ("{:.0f}".format(pt_area))
                else:
                    area = round(pt_area, round_to)

                calc_print("Triangle Area", "s1", t_side_1, unit, "√ p(p − a)(p − b)(p − c)",
                           "√ {}({} - {})({} − {})({} − {})".format(semi_perimeter, semi_perimeter, t_side_1,
                                                                    semi_perimeter, t_side_2, semi_perimeter, t_side_3),
                           pt_area, area, round_to, "s2", t_side_2, "s3", t_side_3, "", semi_perimeter)

            else:
                area = "n/a"
                print()
                print("* The area is n/a *")
                print()

            all_areas.append(area)

            if shape2 == "Triangle":
                perimeter = t_side_1 + t_side_2 + t_side_3
                equation = "s1 + s2 + s3"
                step1 = "{} + {} + {}".format(t_side_1, t_side_2, t_side_3)
                l3 = "s3"
                n3 = t_side_3
            else:
                perimeter = t_side_1 + t_side_1 + t_side_2 + t_side_2
                equation = "s1 + s1 + s2 + s2"
                step1 = "{} + {} + {} + {}".format(t_side_1, t_side_1, t_side_2, t_side_2)
                l3 = ""
                n3 = ""

            if round_to == 0:
                pt_perimeter = ("{:.0f}".format(perimeter))
            else:
                pt_perimeter = round(perimeter, round_to)

            calc_print("{} Perimeter".format(shape2), "s1", t_side_1, unit, equation, step1, perimeter, pt_perimeter,
                       round_to, "s2", t_side_2, l3, n3, "", "")

            pt_perimeter_u = "{} {}".format(pt_perimeter, unit)

            all_perimeters.append(pt_perimeter_u)

            break

        elif enter_choice == "Base And Height":

            base = num_check("What is the base?", "Please enter an number more than 0\n", float)
            height = num_check("What is the height?", "Please enter an number more than 0\n", float)

            print("The base is {} {}".format(base, unit))
            print("The height is {} {}".format(height, unit))

            perimeter = "n/a"
            print()
            print("* The perimeter is n/a *")
            print()

            perimeter_u = "{} {}".format(perimeter, unit)

            all_perimeters.append(perimeter_u)

            if shape2 == "Triangle":
                area = base / 2 * height
                equation = "b x h / 2"
                step1 = "{} x {} / 2".format(base, height)
            else:
                area = base * height
                equation = "b x h"
                step1 = "{} x {}".format(base, height)

            if round_to == 0:
                pt_area = ("{:.0f}".format(area))
            else:
                pt_area = round(area, round_to)

            calc_print("{} Area".format(shape2), "b", base, unit, equation, step1, area, pt_area, round_to, "h", height,
                       "", "", "bh", "")

            pt_area_u = "{} {}²".format(pt_area, unit)

            all_areas.append(pt_area_u)

        elif enter_choice == "Base, Height, Side":

            base = num_check("What is the base?", "Please enter an number more than 0\n", float)
            height = num_check("What is the height?", "Please enter an number more than 0\n", float)
            side = num_check("What is the side? ", "Please enter an number more than 0\n", float)

            print("The base is {} {}".format(base, unit))
            print("The height is {} {}".format(height, unit))
            print("The side is {} {}".format(side, unit))

            perimeter = base + base + side + side

            if round_to == 0:
                p_perimeter = ("{:.0f}".format(perimeter))
            else:
                p_perimeter = round(perimeter, round_to)

            calc_print("Parallelogram Perimeter", "b", base, unit, "b + b + s + s",
                       "{} + {} + {} + {}".format(base, base, side, side), perimeter, p_perimeter, round_to,
                       "s", side, "", "", "", "")

            p_perimeter_u = "{} {}".format(p_perimeter, unit)

            all_perimeters.append(p_perimeter_u)

            area = base * height

            if round_to == 0:
                p_area = ("{:.0f}".format(area))
            else:
                p_area = round(area, round_to)

            calc_print("Parallelogram Area", "b", base, unit, "b * h",
                       "{} * {}".format(base, height), area, p_area, round_to, "h", height, "", "", "", "")

        else:
            print("Sorry, That is not a valid input.")

        return ()


# Gets shapes then sends user to that shapes function
def get_shape():

    # valid shapes holds list of all shapes
    # each item in valid shapes is a list with
    # valid options for each shape <full name, letter code (a - e)
    # ,and possible abbreviations ect>

    valid_shapes = [
        ["triangle", "t", "tri"],
        ["square", "s", "squ"],
        ["rectangle", "rec", "r"],
        ["circle", "cir", "c"],
        ["parallelogram", "par", "p"]
    ]

    desired_shape = ""
    while desired_shape != "xxx" or desired_shape != "no":

        # ask user for desired shape and put in lowercase
        print()
        print("Shape Options: circle, square, rectangle, triangle or parallelogram.(or 'no' to exit)")
        desired_shape = input("Your Shape: ").lower()

        # check that string is valid
        shape_choice = string_check(desired_shape, valid_shapes)

        if desired_shape == "xxx" or desired_shape == "no":
            print()
            return()

        if shape_choice != "invalid choice":
            all_shapes.append(shape_choice)

        if shape_choice == "Triangle" or shape_choice == "Parallelogram":
            shape_tripar(shape_choice)

        elif shape_choice == "Circle":
            shape_circle()

        elif shape_choice == "Square" or shape_choice == "Rectangle":
            shape_squrec(shape_choice)

        else:
            print("Sorry, That is not a valid shape.")

        # add shape and amount to list...
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
        print("1- Choose your shape from the options provided (circle, square, rectangle, triangle or parallelogram)")
        print("    (You can type out the full name, the first letter, of the first 3 letters.)")
        print("2- Input your units (cm, mm or m)")
        print("3- Input how many dp(decimal points) you would like the final answers to be rounded to")
        print("4- Add in the lengths of the shapes sides, or its base and height (for parallelogram and triangle only)")
        print("5- Watch as the program outputs the perimeter and area of the shape, as well as working out!")
        print("6- When you have finished, just input 'no', into the shape question spot.")
        print("7- Input 'y' to have the data (shape, area, perimeter and units) writen into a file")
        print("8- Name the file")
        print("9- Read all the basic info, presented in a table at the bottom of the program")

    return ""


# ***** Main Routine *****


# valid options for units
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
# lists for final outputs
all_shapes = []
all_areas = []
all_perimeters = []

# data frame dictionary
shape_data_dict = {
    'Shape': all_shapes,
    'Area': all_areas,
    'Perimeter': all_perimeters,
}

# instruction question
instructions(y_n)

# Routines link to get_shape function
get_shape()


# create data frame and set index to name column
shape_frame = pandas.DataFrame(shape_data_dict)
shape_frame = shape_frame.set_index('Shape')


# write data to file
write_to_file = yes_no("Would you like the data writen to file? (y/n) ")
if write_to_file == "yes":

    # write to file...
    # create file to hold data (add .txt extension)
    file_name_choice1 = input("What would you lke your file named?")
    if file_name_choice1 == "" or file_name_choice1 == " ":
        file_name_choice = "Math Homework"
    else:
        file_name_choice = file_name_choice1
    file_name = "{}.txt".format(file_name_choice)
    text_file = open(file_name, "w+")
    print("Your File was called: {}.txt ".format(file_name_choice))

    # heading
    text_file.write("*** {} ***\n\n".format(file_name_choice))

    # frame
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
