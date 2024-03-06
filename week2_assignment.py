#creating a list
my_list = []
for i in range(10, 50, 10):
    my_list.append(i)
    
#Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(my_list)

#Extend my_list with another list: [50, 60, 70].
new_list = [50, 60, 70]
my_list.extend(new_list)
print(my_list)

#Remove the last element from my_list.
my_list.pop()
print(my_list)

#Sort my_list in ascending order.
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
print(my_list.index(30))
