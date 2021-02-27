print("Welcome to the calc program")
print("-"*30)
choice = input("Choose 1 to multiply, 2 to divide-> ")
num_1 = int(input("Enter first number-> "))
num_2 = int(input("Enter second number-> "))
if choice == "1":
    print(f"{num_1} multiplied by {num_2} is: {num_1*num_2}")
elif choice == "2":
    print(f"{num_1} divided by {num_2} is: {num_1/num_2}")
else:
    print("You have made an invalid selection")

