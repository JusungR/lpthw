numbers = [1,2,3,4,5]
fruits = ['apple','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3,'quarters']

#this first kind of for-loop goes through a list
for number in numbers :
    print(f'This is {number}.')
    #print('This is {}.'.format(number))

#same as above
for fruit in fruits :
    print(f"This is a {fruit}.")

#also we can go through mixed lists too.
#notice we have to use {} since we don't know what is in it.
for i in change :
    print(f"I got {i}.")

#we can also build the lists, first start with an empty one.
elements = []

for i in range(0,6) :
    print(f"adding {i} to the list.")
    # append is a function to do 0 to 5 counts.
    elements.append(i)

#print(elements)

for i in elements :
    print(f"elemnt is {i}.")
