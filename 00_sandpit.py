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


round_outputs = num_check("Round to how many dp for the final outputs??",
                          "Must be a whole number more than or equal to 0", int)

# round_calc = num_check("Round to how many dp for the calculations??", 
#                        "Must be a whole number more than or equal to 0", int)
