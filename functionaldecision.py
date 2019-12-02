import sys

def choose(prompt, choices):
	print(prompt)
	for i in range(len(choices)):
		print(str(i + 1) + ": " + choices[i])
	inp = int(input("\n"))
	if inp in range(1, len(choices) + 1):
		return inp
	else:
		print("Unexpected input")
		return "error"

response = choose("y or n", ["y","n"])
if response == 1:
	print("You chose yes")
elif response == 2:
	print("You chose no")
