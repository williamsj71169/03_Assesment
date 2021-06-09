

# functions go here
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


round_to = num_check("Round to nearest...? ", "Can't be zero", int)

num = round(45.5324565, round_to)

print(num)
