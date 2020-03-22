import random

scores_list = [1000]

def high_score():
    return min(scores_list)


def random_number():
    return random.randint(1, 10)


def begin_game():
    if len(scores_list) >1:
        scores_list.sort
        print('-' * 40)
        print("\nThe current HIGHSCORE is {}.".format(high_score()))
    else:
        print('*' * 40)
        print("  Welcome to the Number Guessing Game!")
        print('*' * 40)
        print("\nThe rules are simple...\n\nChoose a number 1 - 10 (inclusive) until\nyou guess the number. The less attempts\nyou take the better. Good luck!")
        print("\nNo HIGHSCORE has been set. Go get it!")
        
        
def guess_the_number():
    answer = random_number() 
    attempts = 1
    guess = 0
    highscore = high_score()
    
    while guess != answer:
        try:
            guess = int(input("\nPick a number between 1 - 10:    "))
            if guess < 1 or guess > 10:
                raise ValueError
                continue
            elif guess < answer:
                print("\nIt's higher!")
                attempts += 1
                continue
            elif guess > answer:
                print("\nIt's lower!")
                attempts += 1
                continue
            else:
                print('-' * 40)
                print("\nGot it!")
                if len(scores_list) == 1:
                    print("\nYou set the score to beat... {} attemps.".format(attempts))
                elif attempts >= highscore:
                    print("\nYou took {} attempts.\n\nNo new HIGHSCORE :(".format(attempts))
                elif attempts < highscore:
                    print("\nYou only took {} attempts.\n\n*** Congratulations! ***\n\nThat's a new HIGHSCORE!!!".format(attempts))
                scores_list.append(attempts)
                    
        except ValueError:
            print("\nOops that's not a valid entry.\nOnly numbers 1 - 10 (inclusive) please.\nTry again...")
            continue
            
def replay_or_end():
    while len(scores_list) > 1:
        try:
            print('-' * 40)
            play_again = input("\nWould you like to play again?  Y/N    ")
            if play_again.lower() == "n":
                print('-' * 40)
                print("\nThe game is ending... Play again soon :)\n")
                break
            if play_again.lower() == "y": 
                random_number()
                attempts = 1
                guess = 0
                start_game()
                break
            else:
                raise ValueError
                continue
        except ValueError:
            print("\nOops, didnt understand your answer. Please enter 'Y' or 'N' only...")
            continue
    
def start_game():
    
    begin_game()
    guess_the_number()
    replay_or_end()

if __name__ == '__main__':
    start_game()
