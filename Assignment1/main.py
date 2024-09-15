### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

currency = {
    "largeBills": 0,
    "halfBills": 0,
    "quarters" : 0,
    "nickels" : 0
}

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    #@param: dictionary(resources)
    #@return: boolean
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for key in ingredients:
            print(key)

    #return: float
    def process_coins(self):
        totalPaid = 0
        for key in currency:
            count = float(input(f"How many {key} will you be using?\n"))
            if key == "largeBills":
                currency[key] = count * 1
            elif key == "halfBills":
                currency[key] = count * .5
            elif key == "quarters":
                currency[key] = count * .25
            else:
                currency[key] = count * .5
            totalPaid += currency[key]
        print(totalPaid)

    #param: float, float
    #return: boolean
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        
    #@param: string, dictionary
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if sandwich_size in recipes:
            recipe = recipes[sandwich_size]
        else:
            print("Sorry, we do not offer this sandwich size.\n")     
        for ingredient, amount in order_ingredients.items():
            if ingredient in resources:
                if resources[ingredient] >= amount:
                    resources[ingredient] -= amount
                else:
                    print("Not enough ingredients.\n")
            
                


### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine5000 = SandwichMachine(resources)
sandwichMachine5000.check_resources(resources)


print("\nHello! Welcome to the sandwichMachine5000 virtual sandwich maker.")
size = input("To start, tell us what size sandwich you would like today.\n").lower()
print(recipes[size])
print(f"One {size} sandwich coming right up!\n")
sandwichMachine5000.make_sandwich(size, recipes)


print("In the mean time, let's get the payment over with! You can do so in dollars, half dollars, quarters, and nickels.")
sandwichMachine5000.process_coins()


