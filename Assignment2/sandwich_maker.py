
class SandwichMaker:
    def __init__(self):
        pass

    def check_resources(self, size, resources, recipes):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for key, amount in resources.items():
                if resources.get(key, 0) < recipes[size]["ingredients"].get(key, 0):
                     print(f"Sorry, not enough {key} to fulfill the order.\n")
                     return False
        return True

    def make_sandwich(self, size, resources, recipes):
        ########
        ingredients = recipes[size]["ingredients"]
        for ingredient, amount in ingredients.items():
                resources[ingredient] -= amount
        print(f"One {size} sandwich made! Resources updated and ready for next order.")