class Costco:
    def __init__(self, name, price, quantity=0, total=0, food_list=[], price_list=[], food_dictionary={}, buy_list=[]) -> None:
        """Initializes the Costco self service kiosk

        Args:
            name (_type_): the name of the food item
            price (_type_): the price of the food item
            quantity (_type_): the amount of the food item. Defaults to 0. 
            total (int, optional): the total money. Defaults to 0.
            food_list (list, optional): the list of food items. Defaults to [].
            price_list (list, optional): the list of prices. Defaults to [].
            food_dictionary (dict, optional): the dictionary of food items and prices. Defaults to {}.
            buy_list (list, optional): the list of items the user buys. Defaults to [].
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = total
        food_list = ["Hotdog","Pizza","Chicken Bake","Chicken Salad","Roast Beef Sandwich","Ice Cream","Smoothie","Soda"]
        self.food_list = food_list
        price_list = [1.50,1.99,3.99,6.99,9.99,1.99,2.99,0.69]
        self.price_list = price_list
        for i in range(len(food_list)):
            food_dictionary[food_list[i]] = price_list[i]
        self.food_dictionary = food_dictionary
        self.buy_list = buy_list
    def menu(self) -> None:
        print("Here is the menu:\n1. Hotdog $1.50\n2. Pizza $1.99"
        "\n3. Chicken Bake $3.99\n4. Chicken Salad $6.99\n5. Roast Beef Sandwich $9.99"
        "\n6. Ice Cream $1.99\n7. Smoothie $2.99\n8. Soda $0.69\n9. Finish and pay")
        return
    def food_name(self) -> None:
        while True:
            food_num = input("Enter the food number or type menu: ")
            if food_num == "menu":
                self.menu()
                continue
            elif food_num == "9":
                self.get_receipt()
                break
            elif food_num not in "12345678":
                print("Invalid food number")
                continue
            else:
                self.get_info(food_num)
    def get_info(self,food_num) -> None:
        """gets the name of the food item corresponding to the number

        Args:
            food_num (_type_): the number corresponding to the food item
        """
        for i in range(len(self.food_list)):
            if int(food_num) == i+1:
                self.name = self.food_list[i]
                self.price = self.price_list[i]
                self.get_quantity()
                break
    def get_quantity(self) -> None:
        """
        adds the food item to the list for each quantity the user wants
        """
        self.quantity = int(input(f"Enter the quantity for {self.name}: "))
        for i in range(self.quantity):
            self.buy_list.append(self.name)
        self.get_price()
    def get_price(self) -> None:
        for i in range(len(self.buy_list)):
            self.total += self.food_dictionary[self.buy_list[i]]
        print(f"Your total is ${self.total:.2f}")
    def get_receipt(self):
        print()
        print("Thank you for shopping at Costco\n--------------------------------")
        print("Items:                   Price:")
        for i in range(len(self.buy_list)):
            space = " "*(25-len(self.buy_list[i]))
            print(f"{self.buy_list[i]}{space}${self.food_dictionary[self.buy_list[i]]:.2f}")
        print("--------------------------------")
        print(f"Total:                   ${self.total:.2f}")
def main():
    print("Welcome to Costco self serve kiosk")
    food = Costco("","",0,0,[])
    food.menu()
    food.food_name()
if __name__ == "__main__":
    main()