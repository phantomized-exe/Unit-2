"""
Name: Phann Boon
Date: 3/6/2025
Description: Unit 2 HW 1
"""

# Classes go here
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    def set_number_served(self,number_served):
        self.number_served = number_served
        print(number_served)
    def restaurant(self):
        print(self.number_served)
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")
    def greet_user(self):
        print(f"Welcome {self.first_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0

def main():
    restaurant1 = Restaurant("restaurant","food")
    restaurant1.__init__("restaurant","food")
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    sushi = Restaurant("Bing's Sushi","sushi")
    burgers = Restaurant("Robby's Burgers","burgers")
    pizza = Restaurant("Pete's Pizza","pizza")
    sushi.__init__("Bing's Sushi","sushi")
    burgers.__init__("Robby's Burgers","burgers")
    pizza.__init__("Pete's Pizza","pizza")
    sushi.describe_restaurant()
    burgers.describe_restaurant()
    pizza.describe_restaurant()
    todd = User("Todd","Dewey")
    james = User("James","White")
    sarah = User("Sarah","Smith")
    todd.__init__("Todd","Dewey")
    james.__init__("James","White")
    sarah.__init__("Sarah","Smith")
    todd.describe_user()
    todd.greet_user()
    james.describe_user()
    james.greet_user()
    sarah.describe_user()
    sarah.greet_user()
    restaurant1.restaurant()
    restaurant1.set_number_served(10)
    todd.increment_login_attempts()
    todd.increment_login_attempts()
    todd.reset_login_attempts()

if __name__ == '__main__':
    main()