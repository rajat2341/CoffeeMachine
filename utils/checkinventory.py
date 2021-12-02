

class CheckInventory:

    @staticmethod
    def check_ingredients(inventory):
        all_ingredients = inventory.values()
        for ingredient in all_ingredients:
            if ingredient.get_quantity() < 10:
                print(f'Alert {ingredient.get_name()} is low')

    def check_inventory(self, inventory):
        self.check_ingredients(inventory)
