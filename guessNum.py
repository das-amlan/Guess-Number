import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input("Guess a number: "))
        if guess < randomNumber:
            print("Sorry guess again. Too low!!")
        elif guess > randomNumber:
            print("Sorry guess again. Too High!!")
    print(f"Congratz!! You guessed it right. it's {randomNumber} 👍.")

guess(10)