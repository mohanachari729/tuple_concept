# #Create a Tuple
# my_self = ('mohan',22,'white')
# print(my_self)

# #Access Tuple Elements:
# week_days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
# print(week_days[2])

# #Tuple Concatenation
# tuple1 = (1,3,5)
# tuple2 = (2,4,6)
# print(tuple1 +tuple2)

# #Tuple Unpacking
# rec_dimensions = (3,4)
# lenght , width = rec_dimensions
# area = lenght*width
# print(f"area of rectangle is {area}")


##a Python program to generate a bill for a supermarket purchase
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("      welcome to the super market         ")
print('-'*50)
total_price = 0
for item ,price in items  :
    print(f"{item:<10}:{price:>5}.00")
    total_price += price
else :
    print('-'*50)
    print(f"total cost : {total_price}.00")
