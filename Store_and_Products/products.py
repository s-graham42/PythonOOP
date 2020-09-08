masterNumber = 1001     # Global variable for use in making unique product idNums

def make_idNum():
    global masterNumber # Apparently need this statement to tell the function to use the global rather than
    temp = masterNumber # making it's own masterNumber variable
    masterNumber += 10  # increments masterNumber by 10 for no real reason, could easily be += 1
    return temp

class Product:
    def __init__(self, name, price, category):
        self.prod_name = name
        self.price = price
        self.category = category
        self.idNum = make_idNum()   # calls function to get the unique number

    def update_price(self, percent_change, is_increased = True):
        if is_increased == True:
            print(f"{self.prod_name}'s price has been increased by {percent_change * 100}%")
            self.price += (self.price * percent_change)
        else:
            print(f"{self.prod_name}'s price has been decreased by {percent_change * 100}%")
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"{self.prod_name} - Id no. {self.idNum}:\n\tCategory: {self.category}\t||\tPrice: ${format(self.price, '.2f')}")
        return self                                                               # format() constrains price output to 2 decimal places
