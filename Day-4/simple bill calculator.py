# Write a function named calculate_bill(price, quantity).

#Requirements:
# 1. Ask the user for the product price.
# 2. Ask how many items they purchased.
# 3. Calculate the total bill.
# 4. If the total bill is greater than ₹1000,₹5000, ₹10000 apply a 10%, 20%, 30% discount.
# 5. Return the final bill amount.

def calculate_bill(x,y):

        total=(x*y)

        if (total>1000):
            discount=total*(10/100) # Applying the discount
            total=total-discount
            return total
        elif (total>5000):
            discount=total*(20/100) # Applying the discount
            total=total-discount
            return total
        elif (total>10000):
            discount=total*(30/100) # Applying the discount
            total=total-discount
            return total
        else:
            return total

price=int(input("Enter the price: "))
print("Price is: ",price)
quantitiy=int(input("Enter the quantity: "))
print("Quantity is: ",quantitiy)

discounted_total=calculate_bill(price,quantitiy)
print("Your total is: ",discounted_total)