
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

            if response <= -1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


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

    round_outputs = num_check("Round to how many dp??",
                              "Must be a whole number more than or equal to 0", int)

    c_radius = num_check("What is the radius (half of diameter)? ", "Please enter an number more than 0\n", float)

    if round_outputs == 0:
        c_radius_2 = ("{:.0f}".format(c_radius))
    else:
        c_radius_2 = round(c_radius, round_outputs)

    print("the radius is {} {}".format(c_radius_2, unit))

    circumference = 2 * 3.1415926 * c_radius

    print("Circumference: 2 * 3.1415926 * {} = {}".format(c_radius, circumference))

    if round_outputs == 0:
        c_circumference = ("{:.0f}".format(circumference))
    else:
        c_circumference = round(circumference, round_outputs)

    print("Circumference is {} {} ".format(c_circumference, unit))
    all_perimeters.append(c_circumference)

    area = c_radius ** 2 * 3.1415926

    print("Area: {} ** 2 * 3.1415926 = {}".format(c_radius, area))

    if round_outputs == 0:
        c_area = ("{:.0f}".format(area))
    else:
        c_area = round(area, round_outputs)

    print("Area is {} {} squared".format(c_area, unit))
    all_areas.append(c_area)

    return()


units_options = [
    ["mm"],
    ["cm"],
    ["m"]
]

all_shapes = []
all_areas = []
all_perimeters = []
all_units = []

output = shape_circle()
