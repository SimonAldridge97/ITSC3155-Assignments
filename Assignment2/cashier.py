class Cashier:
    def __init__(self):
        self.currency = {
           "largeBills" : 0,
           "halfBills" : 0,
           "quarters" : 0, 
           "nickels" : 0,
        }

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        totalPaid = 0
        for key in self.currency:
            count = float(input(f"How many {key} will you be using?\n"))
            if key == "largeBills":
                self.currency[key] = count * 1
            elif key == "halfBills":
                self.currency[key] = count * .5
            elif key == "quarters":
                self.currency[key] = count * .25
            else:
                self.currency[key] = count * .05
            totalPaid += self.currency[key]
        return totalPaid

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins >= cost:
            if coins > cost:
                change = coins - cost
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
