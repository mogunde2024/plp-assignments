#function prompting user input and adding the numbers
num_list = input("Enter a list of numbers separated by spaces: \n").split()

sum = 0
for number in num_list:
    sum += int(number)
print("The sum of the numbers is:", sum)

#craeting a tuple of favorite books
books = ("The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye")
for book in books:
    print(book)
    
#creating a dictionary capturing personal information
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")
person_info = {"name": name, "age": age, "color": color}
print(person_info)

#creating a program that accepts user input to create two sets of integers and find the common elements
int_set1 = set(input("Enter the elements of set 1, separated by spaces: ").split())
int_set2 = set(input("Enter the elements of set 2, separated by spaces: ").split())
common_elements = int_set1.intersection(int_set2)
print("The common elements are:", common_elements)


#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
odd_length_words = [word for word in words if len(word) % 2 != 0]  
print(odd_length_words)