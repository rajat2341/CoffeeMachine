# CoffeeMachine

The Driver file is main.py

INPUT JSON : The Coffee Machine expects a json input with keys same as : https://www.npoint.io/docs/77e0bf528e4af43cdc10 Enter the input json file location in the console when running the program.

Example -> python main.py {File Location}

REFILL INGREDIENTS : The initial ingredients are added based on the input. After all beverages are processed (N at a time), the machine asks whether any of the present ingredients need to be refilled. To refill any of the ingredients, input has to be provided in the console as asked by the machine. Note : The ingredient to be refilled must be present in the machine.

ALERT MESSAGES : After processing each drink the ingredient quantity is checked and an alert message is shown if the quantity has fallen below 10.

ASSUMPTIONS : Json input is not valid if it has duplicate keys. Such a json input will still be parsed considering the first value as the only valid one.
