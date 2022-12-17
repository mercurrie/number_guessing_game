import random
from art import logo

# level_of_difficulty() returns number of attempts based on difficulty selection
def level_of_difficulty(choice: str)-> str:
    difficulty = {'easy': 10, 'hard': 5}
    return difficulty[choice]

def user_guesses(attempts: int, answer: int):
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
            
# play() generates random number, takes im input from user, and compared that input to the number generated 
def play():
    print(logo)
    print('Welcome to the number guessing game!')
    print("I'm thinking of a number between 1 and 100.")
    solution = random.randint(1,100)
    print(f'pssst the number is {solution}')
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    number_of_guesses = level_of_difficulty(choice = difficulty)
    
    user_guesses(attempts = number_of_guesses , answer = solution)
    
# used to call play()
if __name__ == '__main__':
    play()