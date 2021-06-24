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
        print("1- Choose your shape from the options provided (circle, square, rectangle, triangle or parallelogram)")
        print("2- Input your units")
        print("3- Input how many dp(decimal points) you would like the final answers to be rounded to")
        print("4- Add in the lengths of the shapes sides, or its base and height (for parallelogram and triangle only)")
        print("5- Watch as the program outputs the perimeter and area of the shape, as well as working out!")
        print("6- When you have finished, just input 'no', into the shape question spot.")
        print("7- Input 'y' to have the data (shape, area, perimeter and units) to be writen into a file")
        print("8- Name the file")
        print("9- Read the basics presented in a table at the bottom of the program")

    return ""


y_n = [
    ["yes", "y"],
    ["no", "n"]
]

instructions(y_n)
