#list comprehention why performance

marks=[20,30,40,50,60]
new_marks=[]
for x in marks:
    new_marks.append(x+2)
print(new_marks)

#list comprehention
narks=[20,30,40,50,60]
#for whom where
new_marks=[x+2 for x in marks]
print(new_marks)

#list comprehention
easy = [x ** 3 for x in range(10) if x % 2 == 0]
print("Using list comprehension:", easy)

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

#using map
nums = [1, 2, 3, 4, 5]  
def sq(n):    
    return n*n  
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)

#activity2 
names = ("smith", "john", "kelvin")
comps = ("Dell", "Apple","MS")

zipped = list(zip(names, comps))
print(zipped)

#for (a,b) in zipped:
#    print(a,b)

# Zip elements of two lists
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")


# Zip elements of two lists
# Print elements one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


# Zip into dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))


#activity3
for i in range(10):
	if i == 5:
		print(exit)
		exit()
	print(i)

#acp
# Take input from user
num = int(input("Enter a number: "))

# List of odd numbers less than input
odd_numbers = [x for x in range(num) if x % 2 != 0]

# List of even numbers less than input
even_numbers = [x for x in range(num) if x % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# List of fruits
fruits = ['apple', 'banana', 'mango', 'cherry']

# Capitalize first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized Fruits:", capitalized_fruits)




