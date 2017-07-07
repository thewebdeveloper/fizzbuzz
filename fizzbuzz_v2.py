# Project: Fizz Buzz
import sys

if len(sys.argv) > 1:
	upper_limit = sys.argv[1]
else:
	upper_limit = input("Enter the upper limit number\n")

try:
	upper_limit = int(upper_limit)
	print("Fizz buzz counting up to {}".format(upper_limit))
		
	for i in range(1, upper_limit+1):
		if i % 3 == 0 and i % 5 == 0:
			print("fizz buzz")
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(i)
except ValueError:
	print("Please Enter a numeric value")