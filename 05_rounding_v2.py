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

selling_price = num_check("num:", "not valid", float)

if type(selling_price) == int:
    print("it works?")

recommended_price = round_up(selling_price, round_to)

print(selling_price)
print(recommended_price)


# for item in snack_order:
#     if len(item) > 0:
#         to_find = (item[1])
#         amount = (item[0])
#         add_list = movie_data_dict[to_find]
#         add_list[-1] = amount
