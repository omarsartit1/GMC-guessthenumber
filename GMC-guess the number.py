import random
min_range = int(input("insert min number"))
max_range = int(input("insert max number"))
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between ",min_range," and ",max_range,". Can you guess what it is?")
    
# Generate a random number between 1 and 100
number_to_guess = random.randint(min_range, max_range)
attempts = 0
max_attempts = int(input("choose the number of attempts"))

while attempts < max_attempts :

    guess = input("Enter your guess: ")
    guess = int(guess)
    difference = (guess-number_to_guess)
    if guess < number_to_guess:
                if difference <=15:
                    print ("your guess is low")    
                else :
                    print("Your guess is too low. Guess again.")
    elif guess > number_to_guess:
                if  difference <=15 :
                    print ("your guess is high")
                else :
                    print("Your guess is too high. Guess again.")
    else:
                print("Congratulations! You guessed the number correctly!")
    attempts += 1           
        