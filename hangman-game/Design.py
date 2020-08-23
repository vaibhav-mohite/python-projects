def design(guesses, word):
    if guesses == 0:
        print("__________\n"
              "|      |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________\n")

    elif guesses == 1:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________\n")

    elif guesses == 2:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|      |\n"
              "|\n"
              "|\n"
              "|__________\n")

    elif guesses == 3:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|      |\n"
              "|      |\n"
              "|\n"
              "|__________\n")

    elif guesses == 4:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|      |\n"
              "|      |\n"
              "|      |\n"
              "|__________\n")

    elif guesses == 5:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|      |\n"
              "|      |\n"
              "|     /|\ \n"
              "|__________\n")

    elif guesses == 6:
        print("__________\n"
              "|      |\n"
              "|      O\n"
              "|     \|/\n"
              "|      |\n"
              "|     /|\ \n"
              "|__________\n")
        print(f"The word was {word}")
