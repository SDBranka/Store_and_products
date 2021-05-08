
# Let's give some methods to our Product class:

#     update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
#     print_info(self) - print the name of the product, its category, and its price.

# Let's also give some methods to our Store class:

#     add_product(self, new_product) - takes a product and adds it to the store
#     sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
#     inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
#     set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)

# 1. Create a Store class with 2 attributes that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.

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


# 2. Create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # 3. Add the print_info method to the Product class
    def print_info(self):
        print(f"The {self.name} is in the {self.category} category and costs ${self.price}")

    # 4. Add the update_price method to the Product class
    def update_price(self, percent_change, is_increased):           #updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
        if is_increased:
            self.price = round((self.price +(percent_change * self.price)),2)
        else:
            self.price = round((self.price - (percent_change * self.price)), 2)
        return self
    



# 7. Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
krogers = Store("Krogers")
krogers.add_product("carrot", 0.25, "vegetable")
krogers.add_product("lettuce", 1, "vegetable")
krogers.add_product("celery", 1, "vegetable")
for i in range(len(krogers.products)):
    krogers.products[i].print_info()

# for i in range(len(krogers.products)):
#     print(krogers.products[i].name)

krogers.sell_product("carrot")
# for i in range(len(krogers.products)):
#     krogers.products[i].print_info()

krogers.inflation(0.10)
# for i in range(len(krogers.products)):
#     krogers.products[i].print_info()

krogers.set_clearance("vegetable", 0.10)
for i in range(len(krogers.products)):
    krogers.products[i].print_info()











# 10. NINJA BONUS: Modularize your code into 3 separate files

# 11. SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.