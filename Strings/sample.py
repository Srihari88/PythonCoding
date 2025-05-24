"""
Multiple ways to reverse the string.
"""

# Using the slice operator
my_string="Welcome to the Python"


reverse_string=my_string[::-1]
print(reverse_string)



# Using the inbuilt reversed method
inbuilt_method=reversed(my_string)

reverseList=[]

for i in inbuilt_method:
    reverseList.append(i)

print("".join(reverseList))



# bootforce soulation
my_string = "Welcome to the Python"

# Split the string into words
list_my_string = my_string.split()

# Initialize an empty list to store reversed words
reversed_list = []

# Loop through each word in the list
for word in list_my_string:
    # Reverse the word using slicing and append to the new list
    reversed_list.append(word[::-1])

# Join the reversed words with spaces and print the final string
print(" ".join(reversed_list))


# Bootforce soulation -2

my_string = "Welcome to the Python"

reverseString=""

for i in range(len(my_string)-1,-1,-1):
    reverseString=reverseString+my_string[i]


print(reverseString)
