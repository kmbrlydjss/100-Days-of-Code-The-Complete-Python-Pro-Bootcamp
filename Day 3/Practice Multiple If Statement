print("Welcome to the Movie Ticket Booking!")
age = int(input("How old are you?"))
bill = 0

if age <= 13:
    bill = 6
    print("Please pay $6")
elif age <= 60:
    bill = 10
    print("Please pay $10")
else:
    bill = 7
    print("Please pay $7")

buy_popcorn = input("Would you like to buy a popcorn? Type y if Yes and n for No.")
if buy_popcorn == "y":
        bill += 4

glass_upgrade = input("Do you want 3D glasses? Type y if Yes and n for No.")
if glass_upgrade == "y":
     bill += 2

print(f"Your total bill is $ {bill}")
