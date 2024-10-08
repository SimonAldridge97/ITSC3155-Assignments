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

#added a dictionary to hold currency
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

    #check the resource dict and verify that theres enough of each
    #@param: dictionary(resources)
    #@return: boolean
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for key, amount in ingredients.items():
            if self.machine_resources.get(key, 0) < amount:
                print(f"Sorry, not enough {key}!")
                return False
        return True

    #method to take integers and turn it into the appropriate denomination
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
        return totalPaid

    #method that checks the processed amount from the method above and checks it against the cost
    #param: float, float
    #return: boolean
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            if coins > cost:
                change = coins - cost
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        
    #make the sandiwch and deduct the resources from the resource dictionary
    #@param: string, dictionary
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
            
                


### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine5000 = SandwichMachine(resources)

print("\nHello! Welcome to the sandwichMachine5000 virtual sandwich maker.")
exit = False
while not exit:
    
    print("Current resources: ")
    for key, value in resources.items():
        print(f"{key} : {value}")
    size = input("To start, tell us what size sandwich you would like today. Or, press 'z' to exit.\n").lower()

    if size == "z":
        print("Powering off!")
        exit = True
        continue  

    if size not in recipes:
        print("Invalid size. Please choose 'small', 'medium', or 'large'.")
        continue  

    #print("Checking resources...\n")
    if sandwichMachine5000.check_resources(recipes[size]["ingredients"]):
        #print("Sufficient resources!")
        print(f"One {size} sandwich coming right up!\n")
        
        

        print("In the meantime, let's get the payment over with! You can do so in dollars, half dollars, quarters, and nickels.")
        print(f"Your total is {recipes[size]["cost"]}")
        total_paid = sandwichMachine5000.process_coins()
        
        if sandwichMachine5000.transaction_result(total_paid, recipes[size]["cost"]):
            sandwichMachine5000.make_sandwich(size, recipes[size]["ingredients"])
            print("Thanks for choosing sandwichMachine5000, here's your sandwich!\n")
    else:
        print("Unable to complete the order due to insufficient resources.\n")
