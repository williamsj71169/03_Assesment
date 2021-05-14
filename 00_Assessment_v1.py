# imports
# import pandas

# functions:


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

        print("Please enter either yes or no...\n")


# checks that input is either a float or an integer that is more that zero.
# takes in custom error messages.
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


# string checker
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


# get shape
# circle
# square
# rectangle
# triangle
# calculations

# function to show instructions if necessary
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = yes_no("*** Would you like to read the instructions? (y/n) ")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("*** Instructions ***")
        print()
        print("* Answer all the questions asked in the way you will be asked to. *")

    return ""

# export

# *********main stuff*********

# 'dictionaries'

# valid options for yes/no questions
y_n = [
    ["yes", "y"],
    ["no", "n"]
]

# valid shapes
valid_shapes = [
    ["triangle", "t", "tri"],
    ["square", "s", "squ"],
    ["rectangle", "rect", "r"],
    ["circle", "circ", "c"]
]

instructions(y_n)

# play_again loop start
play_again = ""
while play_again == "":

    shape = "invalid choice"
    while shape == "invalid choice":
        shape = input("What shape would you like?").lower()
        shape = string_check(shape, valid_shapes)

    print(shape)

    get_side_1 = num_check("How long is side 1?", "Please enter an number more than 0\n", float)

    get_side_2 = num_check("How long is side 2?", "Please enter an number more than 0\n", float)

    # printing

    # write to file

    print()
    play_again = (input("Push <enter> for more questions or any other key to quit"))
    print()

# end
