#if you are using inputs to compare, you need to make sure that you are using the correct data type.
#remember, in Python, inputs come in as strings
#since we are using a whole number to compare (integer) we have to convert the input into an integer using the int() function
age = int(input("What is your age? "))

#single alternative if...only runs if condition is true

if age >= 18:
    print("You can vote")
    print("Congrats")