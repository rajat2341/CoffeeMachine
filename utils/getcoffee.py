from utils.checkinventory import CheckInventory


class GetCoffee:

    @staticmethod
    def get_coffee(beverage, inventory):
        beverage_ingredients = beverage.get_ingredients()

        for ingredient in beverage_ingredients:
            if ingredient.get_name() in inventory:
                inventory_ingredient = inventory[ingredient.get_name()]
                if ingredient.get_quantity() > inventory_ingredient.get_quantity():
                    print(f'{beverage.get_name()} cannot be prepared as {ingredient.get_name()} is not sufficient')
                    return
            else:
                print(f'{beverage.get_name()} cannot be prepared as {ingredient.get_name()} is not available')
                return

        for ingredient in beverage_ingredients:
            if ingredient.get_name() in inventory:
                inventory_ingredient = inventory[ingredient.get_name()]
                balance_quantity_in_inventory = inventory_ingredient.get_quantity() - ingredient.get_quantity()
                inventory_ingredient.set_quantity(balance_quantity_in_inventory)
        print(f'{beverage.get_name()} prepared')

        # Check Inventory if low then raise alert
        ci = CheckInventory()
        ci.check_inventory(inventory)
