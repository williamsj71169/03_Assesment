

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

original = 45.5324565

num = round(original, round_to)

print("Original:{}".format(original))
print("Rounded:{}".format(num))
