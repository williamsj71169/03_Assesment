# functions go here


def demo_thing(animal):

    response = input("Are you a fluffy {}? ".format(animal))
    return response

# Main routine

animal = input("animal? ")

if animal == "dog" or animal == "cat":
    fur = demo_thing(animal)
