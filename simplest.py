## The simplest choose your own adventure
import sys

response = input("y or n")
if response == "y":
    print("yes")
elif response == "n":
    print("nope")
else:
    print("error")
