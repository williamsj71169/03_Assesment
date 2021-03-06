

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


# loops to make testing faster...
for item in range(0, 6):
    want_help = yes_no("Question? ")
    print("You said '{}'\n".format(want_help))
