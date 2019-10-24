number = 5
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("Right!")
        break
    else:
        print ("No no no :(")
        guess_count = guess_count + 1