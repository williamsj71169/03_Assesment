import math


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


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= -1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def calc_print(heading, letter, number, unit, equation, step_1, ur_answer, r_answer, rounded, letter2, number2,
               letter3, number3, choice, t_s_p):
    print()
    # allows for multiple letter-number transitions
    if heading == "Rectangle Perimeter" or heading == "Rectangle Area" or heading == "Parallelogram Perimeter" \
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

# valid options for units
units_options = [
    ["mm"],
    ["cm"],
    ["m"]
]

all_areas = []
all_perimeters = []

shape_choice = input("shape?")
shape_tripar(shape_choice)
