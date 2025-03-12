class Costco:
    def __init__(self, name, price, quantity=0, total=0, food_list=["Hotdog","Pizza","Chicken Bake","Chicken Salad","Roast Beef Sandwich","Ice Cream","Smoothie","Soda"], price_list=[1.50,1.99,3.99,6.99,9.99,1.99,2.99,0.69], buy_list=[]) -> None:
        """Initializes the Costco self service kiosk

        Args:
            name (_type_): the name of the food item
            price (_type_): the price of the food item
            quantity (_type_): the amount of the food item. Defaults to 0. 
            total (int, optional): the total money. Defaults to 0.
            food_list (list, optional): the list of food items. Defaults to ["Hotdog","Pizza","Chicken Bake","Chicken Salad","Roast Beef Sandwich","Ice Cream","Smoothie","Soda"].
            price_list (list, optional): the list of prices. Defaults to [1.50,1.99,3.99,6.99,9.99,1.99,2.99,0.69].
            buy_list (list, optional): the list of items the user buys. Defaults to [].
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = total
        self.food_list = food_list
        self.price_list = price_list
    def get_info(self,food_num) -> None:
        """gets the name of the food item corresponding to the number

        Args:
            food_num (_type_): the number corresponding to the food item
        """
        for i in range(len(self.food_list)):
            print("test")
            if int(food_num) == i+1:
                print("test")
                self.name = self.food_list[i]
                self.price = self.price_list[i]
                self.get_quantity()
                break
    def get_quantity(self) -> None:
        self.quantity = int(input(f"Enter the quantity for {self.name}: "))
        for i in range(self.quantity):
            self.buy_list.append(self.name)
        self.get_price()
    def get_price(self) -> None:
        pass
def main():
    print("Welcome to Costco")
    print("Here is the menu:\n1. Hotdog $1.50\n2. Pizza $1.99"
        "\n3. Chicken Bake $3.99\n4. Chicken Salad $6.99\n5. Roast Beef Sandwich $9.99"
        "\n6. Ice Cream $1.99\n7. Smoothie $2.99\n8. Soda $0.69\n9. Exit")
    food = Costco("","",0,0,[])
    while True:
        food_num = input("Enter the food item number: ")
        if food_num not in "123456789":
            print("Invalid food item")
            continue
        else:
            food.get_info(food_num)
    
if __name__ == "__main__":
    main()