## The simplest choose your own adventure
import sys

def choose(prompt, choices):
	print(prompt)
	for i in range(len(choices)):
		print(str(i) + ": " + choices[i])
	inp = input("\n")
	if inp in range(1, len(choices) + 1):
		return inp
	else:
		print("Unexpected input")
		return "error"

#response = input("y or n")

#response = choose("y or n", ["y","n"])

## object oriented stuff whoo
class Decision:
	def __init__(self, content = "", prompt = "", pathes = {}):
		self.content = content
		self.prompt = prompt
		self.pathes = pathes
	
	## shows options and prompts the player for input
	def choose(self):
		if len(self.content) > 0:
			print(self.content)
		if len(self.prompt) > 0:
			print(self.prompt)
		if len(list(self.pathes.keys())) > 0:
			for i in range(len(self.pathes)):
				print(str(i + 1) + ": " + str(list(self.pathes.keys())[i]))
			inp = int(input("\n"))
			if inp not in range(1, len(self.pathes) + 1):
				print("Unexpected input")
			self.pathes[inp].choose()


## object initialization
one = Decision(content = "This was decision one")
two = Decision(content = "This was decision two")
zero = Decision(prompt = "Which option do you want?", pathes = {1:one, 2:two})

zero.choose()
