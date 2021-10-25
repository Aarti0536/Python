import random
number = random.randint(1,10)
for i in range(0,1):
	user = int(input("Guess the number"))
	if user == number:
		print("Hurray!!")
		print(f"you guessed the right number the number is :- {number}")
		break
if user != number:
	print(f"Your guess is incorrect the number is :- {number}")