FLOW CONTROL STATEMENTS

## IF STATEMENT
if test expression:
	statement(s)

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
while test_expression:
	Body of while

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
for element in sequence:
	Body of for

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
































