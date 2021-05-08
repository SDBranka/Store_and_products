 1. Create a Store class with 2 attributes that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    # 5. Add the add_product method to the Store class
    def add_product(self, name, price, category):
        self.products.append(Product(name, price, category))
        return len(self.products)-1
    
    # 6. Add the sell_product method to the Store class
    def sell_product(self, name):
        for i in range(len(self.products)):
            if self.products[i].name == name:
                x = i
        self.products.pop(x)
        return self

    # 8. NINJA BONUS: Add the inflation method to the Store class
    def inflation(self, percent_increase):          #increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
        return self

    
    # 9. NINJA BONUS: Add the set_clearance method to the Store class
    def set_clearance(self, category, percent_discount):            #updates all the products matching the given category by   reducing the price by the percent_discount given (use the method you wrote in the Product class!)
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
        return self
