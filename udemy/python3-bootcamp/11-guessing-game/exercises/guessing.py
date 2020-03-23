import random


def game():
    number = random.randint(1, 100)
    prompt = "Guess a number between 1 and 100: "
    guess = int(input(prompt))

    while guess != number:

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")

        guess = int(input(prompt))

    print("You guessed it! You won!")


def main():

    resp = 'y'
    while resp != 'n':
        game()
        resp = input("Do you want to play again (y/n): ")
    print("Thanks for playing. Bye!")

if __name__ == "__main__":
    main()
