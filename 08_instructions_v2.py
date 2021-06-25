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


def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = yes_no("*** Would you like to read the instructions? (y/n) *** ")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("*** Instructions ***")
        print()
        print("* Choose your shape from the options, then input your units and to how many dp(decimal points)")
        print(" you would like the final answers to be rounded to. Add in the lengths of the shapes sides, or")
        print(" its base and height for parallelogram and triangle only) and you will receive the area and ")
        print(" perimeter in the units that you provided as well as the working out that lead to that answer. ")
        print(" When you have finished, just input 'no', into the shape question spot. You will be asked if you")
        print(" would like for the data (just the basic shape, area, perimeter and units) to be writen into a file")
        print(" that you will be prompted to name. Even if you choose not to write it to a file, there will be an")
        print(" output at the very end with the basics. *")

    return ""


y_n = [
    ["yes", "y"],
    ["no", "n"]
]

instructions(y_n)
