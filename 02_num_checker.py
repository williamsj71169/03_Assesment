

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

# main stuff
get_side_1 = num_check("How long is side 1?", "Please enter an number more than 0\n", float)

get_side_2 = num_check("How long is side 2?", "Please enter an number more than 0\n", float)
