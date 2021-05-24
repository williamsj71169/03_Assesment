

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


age = num_check("Age: ", "Please enter a number more than 0", int)

t_side_1 = num_check("How long is side 1? ", "Please enter a number more than 0", float)

if type(t_side_1) == int:
    print("Is {}".format(t_side_1))
else:
    print("Not {}".format(t_side_1))
