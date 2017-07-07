# Project: Fizz Buzz
upper_limit = 101

print("Fizz buzz counting up to {}".format(upper_limit - 1))

for i in range(1,upper_limit):
	if i % 3 == 0 and i % 5 == 0:
		print("fizz buzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)