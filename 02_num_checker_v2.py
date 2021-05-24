

# checks for an integer more than 0
def int_check(question):

    error = "Please enter a number more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer in not entered, display an error
        except ValueError:
            print(error)


age = int_check("Age: ")

t_side_1 = int_check("How long is side 1? ")

if type(t_side_1) == int:
    print("Is {}".format(t_side_1))
else:
    print("Not {}".format(t_side_1))
