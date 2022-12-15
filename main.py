import random
from art import logo

# level_of_difficulty() returns number of attempts based on difficulty selection
def level_of_difficulty(choice):
    if choice == 'easy':
        return 10
    else:
        return 5
    
# play() generates random number, takes im input from user, and compared that input to the number generated 
def play():
    print(logo)
    print('Welcome to the number guessing game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f'pssst the number is {answer}')
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    attempts = level_of_difficulty(choice = difficulty)
    guess = 0
    
    while attempts > 0 and guess != answer:
        print(f'\nYou have {attempts} attempts remaining to guess the number. ')
        guess = int(input('Pick a number. '))
        if guess > answer:
            print('Your guess is too high.\nGuess again.')
        elif guess < answer:
            print('Your guess is too low. \nGuess again.')
        attempts -= 1
    
    if guess == answer:
        print('You guessed the number. You win!')
    else:
        print('You ran out of attempts. You lose.')
        
    
    
# used to call play()
if __name__ == '__main__':
    play()