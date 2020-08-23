import random
from Design import design
from WordData import word


def random_word():
    my_word = random.choice(word)
    return my_word.upper()


def hangman():
    guesses = 0  # No. of Guesses
    word = random_word()  # Randomly Selects a Word from WordData
    wordlist = list(word)
    blanks = "_" * len(word)  # Creating Blanks
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    print("*" * 20 + " HANGMAN GAME " + "*" * 20)
    print("Lets Play!")
    design(guesses, word)
    print("\n" + ''.join(blanks_list))

    while guesses < 6:
        print()
        print(f"TRIES LEFT = {6 - guesses}")
        guess = input("Guess a Letter ---> ")
        guess = guess.upper()

        if len(guess) == 0:  # If the user doesn't enter a letter
            print("Enter a Letter !")

        elif len(guess) > 1:  # If user enters more than 1 letter
            print("Only 1 Letter can be Entered !")

        elif guess in guess_list:  # If user enter the letter that is already guessed
            print("You have Already Guessed this letter !")
            print(' '.join(guess_list))

        else:  # If all above conditions failed
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = wordlist[i]
                i = i + 1

            # If Guessed letter is wrong
            if new_blanks_list == blanks_list:
                print(f"OOPS! The letter {guess} isn't there in the word. Try Again\n")
                guesses = guesses + 1
                design(guesses, word)
                if guesses < 6:
                    print("Guess Again.")
                    print()
                    print("".join(blanks_list))

            # If Guessed letter is correct
            elif wordlist != blanks_list:
                blanks_list = new_blanks_list[:]
                print("".join(blanks_list))

                if wordlist == blanks_list:  # Guessed WORD is Correct
                    print("CONGRATULATIONS! YOU WON")
                    print()
                    again = "Do you wish to continue [Y/N] : "
                    if again.upper() == "Y":
                        hangman()
                    else:
                        print("Thanks For Playing")
                        quit()

                else:  # Guessed letter is Correct
                    print("Great Guess! Guess the next letter!")


hangman()
