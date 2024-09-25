import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker()
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    exit = False
    while not exit:
        print("Hello, welcome to virtual sandwich machine, modular style")
        size = input("To start, tell us what size sandwich you want. We offer small, medium, and large. Or, press 'z' to exit.\n").lower()

        if size == "z":
            exit = True
        elif size not in recipes:
            print("Sorry, we do not offer that size sandwich.\n")
        else:
            if sandwich_maker_instance.check_resources(size, resources, recipes):
                print("Great! While we make it, lets get your payment settled up.")
                print(f"A {size} sandwich costs {recipes[size]["cost"]}.")
                total_paid = cashier_instance.process_coins()
                cashier_instance.transaction_result(total_paid, recipes[size]["cost"])
                sandwich_maker_instance.make_sandwich(size, resources, recipes)
                print("Thanks for coming!")

    # 
if __name__=="__main__":
    main()
    


    
