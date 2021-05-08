# 10. NINJA BONUS: Modularize your code into 3 separate files
from store2 import Store

# 7. Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
krogers = Store("Krogers")
print("--add_product--")
krogers.add_product("carrot", 0.25, "vegetable")
krogers.add_product("lettuce", 1, "vegetable")
krogers.add_product("celery", 1, "vegetable")
for i in range(len(krogers.products)):
    krogers.products[i].print_info()
# for i in range(len(krogers.products)):
#     print(krogers.products[i].name)

# print("\n\n--sell_product--")
# krogers.sell_product("carrot")            #for use with store.py
# for i in range(len(krogers.products)):
#     krogers.products[i].print_info()

print("\n\n--sensei sell_product--")            #for use with store2.py
krogers.sell_product()

print("\n\n--inflation--")
krogers.inflation(0.10)
for i in range(len(krogers.products)):
    krogers.products[i].print_info()

print("\n\n--set_clearance--")
krogers.set_clearance("vegetable", 0.10)
for i in range(len(krogers.products)):
    krogers.products[i].print_info()


# 11. SENSEI BONUS: Update the product class to give each product a unique id. 
# Update the sell_product method to accept the unique id.
