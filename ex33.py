i = 0
numbers = []

while i < 6 :
    print(f"This is count {i}.")
    numbers.append(i)

    i += 1
    print("Numbers now : ", numbers)
    print(f"At the bottom i is {i}.")

print("The numbers :")

for num in numbers :
    print(num)
