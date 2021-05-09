# inputs

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


# not blank?
# get shape
# circle
# square
# rectangle
# triangle
# calcutations
# instructions
# export

# main stuff

get_int = num_check("How long is side 1?", "Please enter an number more than 0\n", float)

get_cost = num_check("How long is side 2?", "Please enter an number more than 0\n", float)

# 'dictionaries'

# valid options for yes/no questions
y_n = [
    ["yes", "y"],
    ["no", "n"]
]

# instructions(y_n)

# printing

# write to file
