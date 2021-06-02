# functions go here


def demo_thing(question):

    response = input(question)
    return response


def thing_two():
    example = demo_thing("Greeting? ")
    return example

# Main routine

greeting = thing_two()

print(greeting)
