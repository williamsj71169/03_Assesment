import math


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


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# ask user for rounding
round_to = num_check("Round to nearest... ", "Can't be zero", int)

selling_price = num_check("num 1:", "not valid", float)

recommended_price = round_up(selling_price, round_to)

print(selling_price)
print(recommended_price)
