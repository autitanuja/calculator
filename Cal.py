

# TASK 2: DESIGN A SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATION

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2


def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	return num1 / num2
print("---------SIMPLE CALCULATOR----------")
print("------------------------------------")
print("Please Select Operation -\n" \
		"1. Addition (+)\n" \
		"2. Subtraction (-)\n" \
		"3. Multiplication (*)\n" \
		"4. Division (/)\n")


select = int(input("Select operations from 1, 2, 3, 4 :"))

number_1 = int(input("Enter First Number: "))
number_2 = int(input("Enter Second Number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
