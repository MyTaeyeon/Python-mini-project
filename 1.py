import random
n = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while n != guess:
    if n < guess:
        print("Correct number is smaller")
    else:
        print("Correct number is bigger")
    guess = int(input("Enter any number: "))
print('you guess it right!!')