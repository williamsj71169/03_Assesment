

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


valid_shapes = [
    ["triangle", "t", "tri"],
    ["square", "s", "squ"],
    ["rectangle", "rect", "r"],
    ["circle", "circ", "c"]
]

shape = "invalid choice"
while shape == "invalid choice":
    shape = input("What shape would you like?").lower()
    shape = string_check(shape, valid_shapes)

print(shape)
