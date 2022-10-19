# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

# Running outer for loop to
# iterate through a list1.
for item in list1:
    # Printing outside inner loop
    print("start outer for loop ")

    for item2 in list2:
        # Printing inside inner loop
        print(item, item2)
    # Printing outside inner loop
print("end for loop ")
