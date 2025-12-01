
import random 
choice = random.randint(1,2)
if choice == 1:
	name = input("Enter your name:")
	print(f"Hello {name}")
	fav1 = input("What is your favorite animal:")
	fav2 = input("What is your favorite color:")
	fav3 = input("What is your favorite number:")
	print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

if choice == 2:
	fav4 = input("Who is your favorite artist:")
	fav5 = input("What is your favorite album by them?:")
	fav6 = input("Pick a number 1-5:")
	print(f"{fav4}'s album {fav5} is undeniably top {fav6} albums of all time")
