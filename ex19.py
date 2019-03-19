def cheese_and_crackers(Cheese_count,box_of_crackers) :
    print(f"You have {Cheese_count} cheese!")
    print(f"You have {box_of_crackers} box of crackers.")
    print("Man, that's enough for the party!")
    print("Get a blanket.\n")

print("we can give you the function number directly:")
cheese_and_crackers(20,30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("And we can combine two, variables and math")
amount_of_cheese = 30

cheese_and_crackers(amount_of_cheese,60)

print("And one more thing!")
amt_of_cheese = int(input("How many cheese do you have?"))
amt_of_crackers = int(input("Then, how many box of crackers do you have?"))

cheese_and_crackers(amt_of_cheese,amt_of_crackers)
