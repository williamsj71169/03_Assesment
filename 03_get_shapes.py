

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


# Gets list of shapes
def get_shape():

    # valid_shapes holds list of all shapes
    # each item in valid shapes is a list with
    # valid options for each shape <full name, letter code (a - e)
    # ,and possible abbreviations ect>

    valid_shapes = [
        ["triangle", "t", "tri"],
        ["square", "s", "squ"],
        ["rectangle", "rect", "r"],
        ["circle", "circ", "c"]
    ]

    # holds shape order for a single user
    shape_order = []

    desired_shape = ""
    while desired_shape != "xxx" or desired_shape != "no":

        # ask user for desired shape and put in lowercase
        desired_shape = input("shape: ").lower()

        if desired_shape == "xxx" or desired_shape == "no":
            return shape_order

        # remove white space around shape
        desired_shape = desired_shape.strip()

        # check that string is valid
        shape_choice = (desired_shape)
        print("Shape Choice: ", shape_choice)


shape_order = get_shape()
