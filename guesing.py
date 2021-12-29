import random
guess=int( input("guess a number between 1-9"))
number=random.randint(1,9)

print(number)

if (guess < number):
    print("wrong answer ,guess a number above 2")

elif(guess > number):
    print("wrong answer guess a number below 6")

else:
    print("congrats!! you won!")
