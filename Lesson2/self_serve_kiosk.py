class Kiosk:
    def __init__(self,item_name,item_price,transaction_total=0,item_dictionary={},item_list=[],price_list=[]):
        '''
        This method will initialize the Kiosk object
        '''
        self.item_name = item_name
        self.item_price = item_price
        self.item_dictionary = item_dictionary
        self.transaction_total = transaction_total
        self.item_list = item_list
        self.price_list = price_list
    def getTotal(self):
        '''
        This method will calculate the total of the transaction
        '''
        self.transaction_total = sum(self.price_list)
    def addItem(self,item_name,item_price):
        '''
        This method will add an item to the item dictionary, item list, and price list
        '''
        self.item_dictionary[item_name] = item_price
        self.item_list.append(item_name)
        self.price_list.append(item_price)
    def takePayment(self):
        '''
        This method will take the payment from the user
        '''
        self.payment = int(input("Enter the amount you want to pay: "))
    def giveChange(self):
        '''
        This method will give the user their change
        '''
        if self.payment >= self.transaction_total:
            self.change = self.payment - self.transaction_total
            print(f"Your change is ${self.change}")
        else:
            print("You did not pay enough")
    def finalizeTransaction(self):
        '''
        This method will finalize the transaction
        '''
        print(f"Your total is ${self.transaction_total}")
    def print_receipt(self):
        '''
        This method will print the receipt
        '''
        print("Thank you for shopping with us:")
        print(f"Your total was ${self.transaction_total}")
        print(f"You paid ${self.payment}")
        print(f"Your change is ${self.change}")
    def reset_transaction(self):
        '''
        This method will reset the transaction
        '''
        self.item_name = ""
        self.item_price = 0
        self.item_dictionary = {}
        self.transaction_total = 0
        self.item_list = []
        self.price_list = []
shopping = True
kiosk = Kiosk("","",0,{},[],[])
while shopping:
    item_name = input("Enter the item you want to add: ")
    item_price = int(input("Enter the price of the item: "))
    kiosk.addItem(item_name,item_price)
    kiosk.getTotal()
    kiosk.finalizeTransaction()
    continue_shopping = input("Do you want to continue shopping? (yes/no): ")
    if continue_shopping == "no":
        while True:
            kiosk.takePayment()
            kiosk.giveChange()
            if kiosk.payment >= kiosk.transaction_total:
                break
        kiosk.print_receipt()
        continue_shopping = input("Go shopping again? (yes/no): ")
        if continue_shopping == "no":
            shopping = False
        else:
            kiosk.reset_transaction()
