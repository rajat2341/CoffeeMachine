from ingredient import Ingredient
from beverages import Beverages
from utils.getcoffee import GetCoffee


class CoffeeMachine:
    inventory = {}
    beverages = {}

    def add_ingredients_to_inventory(self, machine_data):
        all_ingredients = machine_data['total_items_quantity']
        for name, quantity in all_ingredients.items():
            if int(quantity) > 0:
                if name in self.inventory:
                    ingredient = self.inventory[name]
                    ingredient.update_quantity(int(quantity))
                else:
                    ingredient = Ingredient(name, int(quantity))
                    self.inventory[name] = ingredient
                print("Ingredients in Inventory added")
            else:
                print("Inappropriate Quantity")

    def process_coffee(self, beverages):
        print(f'processing {len(beverages)} order')
        for b1 in beverages:
            gc = GetCoffee()
            gc.get_coffee(b1, self.inventory)

    def add_beverages_to_coffee_machine(self, machine_data, outlets):
        beverages = []
        all_beverages = machine_data['beverages']
        for beverage_name, ingredients in all_beverages.items():
            beverage_ingredients = []
            for name, quantity in ingredients.items():
                if int(quantity) > 0:
                    ingredient = Ingredient(name, int(quantity))
                    beverage_ingredients.append(ingredient)
                else:
                    print("Inappropriate quantity")
            beverage = Beverages(beverage_name, beverage_ingredients)
            beverages.append(beverage)

            if len(beverages) == outlets:
                self.process_coffee(beverages)
                beverages = []
        if len(beverages) > 0:
            self.process_coffee(beverages)
            beverages = []

    def process_drinks(self, data):
        machine_data = data['machine']

        # reading outlets
        outlets = machine_data['outlets']['count_n']

        # adding ingredients to inventory
        self.add_ingredients_to_inventory(machine_data)

        # Adding beverages requested by user
        self.add_beverages_to_coffee_machine(machine_data, int(outlets))

    def add_ingredients(self, x):
        while x == 'Y' or x == 'y':
            print("Enter Ingredient Name to refill : ")
            name = input()
            print("Enter Ingredient Quantity to refill : ")
            quantity = int(input())
            if quantity < 0:
                print("Refill Quantity is Negative")
                return
            if name in self.inventory:
                ingredient = self.inventory[name]
                ingredient.update_quantity(quantity)
                print(f'Successfully Refilled {name}')
                print(f'Updated Quantity {ingredient.get_quantity()}')
            else:
                print(f'{name} does not exist in inventory')
            print("Do you want to Refill another item? Press 'Y' to continue or any other button to exit")
            x = input()










