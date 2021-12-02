import sys
from coffeemachine import CoffeeMachine
import json


def start_machine(cm, filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            cm.process_drinks(data)
        print("Enter 'Y' to Refill Ingredients, press any other Button to Exit: ")
        refill = input()
        if refill == 'Y' or refill == 'y':
            cm.add_ingredients(refill)
        print("Thank you")
    except Exception as e:
        raise e


def main():
    if len(sys.argv) > 1:
        cm = CoffeeMachine()
        start_machine(cm, sys.argv[1])
    else:
        print("Specify the file")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()