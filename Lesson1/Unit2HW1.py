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
    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}\nType: {self.cuisine_type}")
    def open_restaurant():
        print("The restaurant is open")
class User:
    def __init__(self,first_name,last_name,gender,birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nBirthday: {self.birthday}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you are a {self.gender}")

def main():
    restaurant1 = Restaurant("restaurant","food")
    restaurant1.__init__("restaurant","food")
    restaurant1.describe_restaurant()
    Restaurant.open_restaurant()
    sushi = Restaurant("Bing's Sushi","sushi")
    burgers = Restaurant("Robby's Burgers","burgers")
    pizza = Restaurant("Pete's Pizza","pizza")
    sushi.__init__("Bing's Sushi","sushi")
    burgers.__init__("Robby's Burgers","burgers")
    pizza.__init__("Pete's Pizza","pizza")
    sushi.describe_restaurant()
    burgers.describe_restaurant()
    pizza.describe_restaurant()
    todd = User("Todd","Dewey","male","10/12/1985")
    james = User("James","White","male","3/5/1990")
    sarah = User("Sarah","Smith","female","5/6/1995")
    todd.__init__("Todd","Dewey","male","10/12/1985")
    james.__init__("James","White","male","3/5/1990")
    sarah.__init__("Sarah","Smith","female","5/6/1995")
    todd.describe_user()
    todd.greet_user()
    james.describe_user()
    james.greet_user()
    sarah.describe_user()
    sarah.greet_user()
if __name__ == '__main__':
    main()