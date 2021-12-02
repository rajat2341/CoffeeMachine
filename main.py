import sys
from coffeemachine import CoffeeMachine
import json


def start_machine(cm, filename):
    try:
        # reading inputs given to coffee machine
        with open(filename) as file:
            data = json.load(file)

            # processing drinks
            cm.process_drinks(data)

        # checking whether user needs to refill
        print("Enter 'Y' to Refill Ingredients, press any other Button to Exit: ")
        refill = input()
        if refill == 'Y' or refill == 'y':
            # adding more ingredients
            cm.add_ingredients(refill)
        print("Thank you")

    # catching all the exceptions
    except Exception as e:
        raise e


def main():
    if len(sys.argv) > 1:

        # initialising the singleton class instance
        cm = CoffeeMachine()

        # starting the machine and providing inputs
        start_machine(cm, sys.argv[1])
    else:
        print("Specify the file")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()