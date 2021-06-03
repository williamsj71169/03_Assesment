# functions go here


def demo_thing(teeth, claws):

    print("Teeth: {} ".format(teeth))
    print("Claws: {} ".format(claws))




# Main routine

animal = input("animal? ")

if animal == "dog":
    teeth = "sharp"
    claws = "non-retractable"

elif animal == "cat":
    teeth = "pointy"
    claws = "retractable"

statement = demo_thing(teeth, claws)
