import uuid

# 2. Create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation
class Product:
    # 11. SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4().hex[:8]

    # 3. Add the print_info method to the Product class
    def print_info(self):
        print(f"The {self.name} is in the {self.category} category and costs ${self.price}. The id# is {self.id}")

    # 4. Add the update_price method to the Product class
    def update_price(self, percent_change, is_increased):           #updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
        if is_increased:
            self.price = round((self.price +(percent_change * self.price)),2)
        else:
            self.price = round((self.price - (percent_change * self.price)), 2)
        return self