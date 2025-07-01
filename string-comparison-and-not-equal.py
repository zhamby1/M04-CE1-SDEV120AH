#this program checks to see if it is your birthday...if it is then will sing happy birthday..if not it will say just a normal day

#string do not need to be converted from input when comparing

birthday = input("Is it your birthday? Press y and enter for yes, or n and enter for no ")

#conditions are VERY exact. When you compare strings capitalization matters.. ie Y will not work
if birthday == "y":
    print("Happy Birthday")
else:
    print("Just a normal day")

#sometimes when we want to be exact, we can just use if statements

birthday = input("Is it your birthday? Press y and enter for yes, or n and enter for no ")

if birthday == "y":
    print("Happy Birthday")
if birthday == "n":
    print("Just a normal day")


#this is doing the same problem but using !=

birthday = input("Is today a normal day?  If so press y and enter.  If it is your birthday press n and enter ")
if birthday != "n":
    print("Just a normal day")
else:
    print("Happy birthday to you")