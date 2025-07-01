customer_age = int(input("What is your age? "))
ticket_price = 10.00
DISCOUNT = 0.10

if customer_age < 65:
    print("You do not get a discount")
else:
    print("You do get a discount")
    ticket_price = ticket_price - (DISCOUNT * ticket_price)

print("Your ticket price is", ticket_price)