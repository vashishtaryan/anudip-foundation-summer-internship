# calculate the total revenue genreated by the two product categories in a store
import numpy as np
cat1 = np.array([500, 600, 700, 550])
cat2 = np.array([450, 700, 800, 600])

total_revenue = cat1 + cat2
print("Total Revenue:",total_revenue)


print("<-------------------------------------------------------->")


#calculate the profit made by the company
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500 ,4800])

profit = revenue - expenses
print("profit is:",profit)


print("<-------------------------------------------------------->")


#determine which products is a store are out stocks (quantity is 0)
inventory = np.array([10, 0, 5, 0, 20, 0])
print("out of stock:-")
print(inventory[inventory == 0])

print("<-------------------------------------------------------->")

#calculate the total cost of items in a shopping cart, considering the quantity and price per item
quantity = np.array([2, 3, 4, 1])
price = np.array([10.0, 5.0, 8.0, 12.0])
print("total cost :",quantity*price)