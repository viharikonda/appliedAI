## FLOW CONTROL STATEMENTS

## IF STATEMENT
#if test expression:
#	statement(s)

## IF 
num = 10
if num > 10 :
	print("Number is positive")
print("This will print always")

## IF ELSE
num = 10
if num > 0:
	print("positive number")
else:
	print("negative number")

## ELIF/ELSE IF
num = 10.5
if num >0:
	print("positive number")
elif num == 0:
	print("zero")
else:
	print("Negatie number")

## NESTED IF
num = 10.5
if num >=0:
	if num == 0:
		print("zero")
	else:
		print("Positive number")
else:
	print("Negatie number")

## Largest of three numbers
num1 = 10
num2 = 50
num3 = 15

if (num1 >= num2) and (num1 >= num3):
	largest = num1
elif (num2 >= num1) and (num2 >= num3) :
	largest = num2
else:
	largest = num3
print("Largest element among three numbers is: {}".format(largest))

## WHILE LOOP
#while test_expression:
#	Body of while

## while
lst = [10, 20, 30, 40, 50]

product = 1
index = 0

while index < len(lst):
	product *= lst[index]
	index += 1
print("product is: {}".format(product))

## while loop with else
numbers = [1,2,3]

index = 0
while index < len(numbers):
	print(numbers[index])
	index += 1 ## important line in the loop - endless loop/ infinite loop
else:
	print("no item left in the list")

## check if a given number is prime
num = int(input("Enter a number:"))
isDivisible = False;
i = 2;
while i < num:
	if num % i == 0:
		isDivisible = True;
		print("{} is divisible by {}". format(num, i))
	i += 1;
if isDivisible:
	print("{} is not a prime number".format(num))
else:
	print("{} is a prime number". format(num))

## FOR LOOP
#for element in sequence:
#	Body of for

## for loop
lst = [10, 20, 30, 40, 50]
product = 1
for ele in lst:
	product *= ele
print("product is: {}".format(product))

## range function
for i in range(10):
	print(i)

for i in range(1,20,2):
	print(i)

lst = ["text1", "text2", "text3", "text4", "text5"]
for index in range(len(lst)):
	print(lst[index])

for ele in lst:
	print(ele)

## prime numbers within an interval
index1 = 10
index2 = 50

print("prime numbers between {0} and {1} are:". format(index1, index2))
for num in range(index1, index2 + 1):
	if num > 1:
		isDivisible = False;
		for index in range(2, num):
			if num % index == 0:
				isDivisible = True;
		if not isDivisible:
			print(num);

## Break and continue

## break
numbers = [1,2,3,4]
for num in numbers:
	if num == 4:
		Break
	print(num)
else:
	print("in the else-block")
print("outside the for block")

## prime numbers between intervals
index1 = 10
index2 = 50

print("prime numbers between {0} and {1} are:". format(index1, index2))
num = int(input("Enter a number:"))
isDivisible = False;
i = 2;
while i < num:
	if num % i == 0:
		isDivisible = True;
		print("{} is divisible by {}". format(num, i))
		Break;
	i += 1;
if isDivisible:
	print("{} is not a prime number".format(num))
else:
	print("{} is a prime number". format(num))

## continue
numbers = [1,2,3,4,5]
for num in numbers:
	if num % 2 == 0:
		continue
	print(num)
else:
	print("else-block")

## lists
## list is one of the sequence data structures
## lists ate collection of items
## each item in the list has an assigned index value
## lists are mutable

emptyList = []
lst = ['one', 'two', 'three']
lst2 = [1,2,3,4,5]
lst3 = [[1,2],[3,4]]
lst4 = [1,'text', [1,2,3], 24.5, True]

lst.insert(2, 'three') # second position insert 'three' 
lst.remove('two') # removes first occurance
lst.append(lst2) # list inside a list
lst.extend(lst2) # add elements at last
lst_final = lst1 + lst2 # extend another method
del lst[1] # delete index 1 in list
lst.pop(1) #another way to delete
lst.remove('three') # dynamic way

## in keyword
lst = ['one', 'two', 'three']
if 'two' in lst:
    print('AI')

if 'six' not in lst:
    print('ML')

lst.reverse() # reverse the list

# sorting
numbers = [1,2,3,4,5]
sorted_listed  = sorted(numbers, reverse = True) # desc numbers
sorted_listed  = sorted(numbers) # asc numbers

lst.sort() # asc order

a = "one, two, three, four, five"
slst = a.split(',')
print(slst)

# list indexing
lst = [1,2,3,4]
print(lst[0:2]) # print 0 upto 2 indexes
print(lst[::2]) # from 0 to end with stepsize 2
print(lst[2::2])

numbers = [1,2,3,4,5,6,7,8,9,1]
frequency_of_1 = print(numbers.count(1))

for ele in numbers:
    print (ele)

## list comprehension
    
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

squares = [i**2 for i in range(10)]
print(squares)

lst = [-10, 20, 30, -40, 20, 10]
new_lst = [i*2 for i in lst]
print(new_lst)

new_lst = [i for i in lst if i >= 0]
print(new_lst)

matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]

transposed = []
for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row(i))
        transposed.append(lst)
print(transposed)


transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

## sets
#Set is an unordered collection of items. every element is unique
#The set itself is mutable
#sets can be used to perform mathematical operations

s = {1,2,3,4}
print(type(s))

## Python functions
# syntax 
# def function_name(parameters):
#    _____________
    

def print_name(name):
    """
    This function prints name
    """
    print("Hello" + str(name))

print_name('vihari')

print(print_name.__doc__) # print doc name of the function

# return statement
def get_sum(lst):
    """
    this function returns the sum of all elements in a list
    """
    _sum = 0
    for num in lst:
        _sum += num
    return _sum

## scope and life time of variable
global_var = "this is global variable"

def test_life_time():
    """
    this function test the life time of a variable
    """
    local_var = "this is local variable"
    print(local_var)
    print(global_var)
    
test_life_time()

print(global_var)
print(local_var)

def computeHCF(a,b):
    """
    computing HCF of two numbers
    """
    smaller = b if a > b else a
    hcf = 1
    for i in range(1, smaller+1):
        if(a % i == 0) and (b % i ==0):
            hcf = i
    return hcf

num1 = 98
num2 = 78
print("hcf of {0} is : {2}".format(num1, num2, computeHCF(num1, num2)))
        
# Types of functions
# built in functions
# user-defined functions

abs() # defines absolute value of the number
all() # true if all elements in iterable are true vice versa for false
dir() # returns a valid attributes
divmod() # returns pair of quotient and remainder as a tuple
enumerate()
 numbers = [10, 20, 30, 40]
 for index, num in enumerate(numbers):
     print("index {0} has a value {1}". format(index, num))

















    

























