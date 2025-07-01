customer_age = int(input("What is your age? "))
ticket_price = 10.00
DISCOUNT = 0.10

#if customer is older or is 65..they get a discount
if customer_age >= 65:
    print("You get a discount")
    ticket_price = ticket_price - (DISCOUNT * ticket_price)

else:
    print("You do not get a discount")

print("Your ticket price is", ticket_price)