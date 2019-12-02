# Hangman
# This program requires the Random-Word module

from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()
length = len(word)
secret = list(word)
blanks = list('_' * length)
wrong_guesses = 0
letters = []

print("Welcome to Hangman:")
print(" ______ ")
print("|      |")
print("|       ")
print("|       ")
print("|       ")
print("|_______")
print()
print(' '.join(blanks))
print()

while blanks != secret:
    guess = input("Enter a letter:\n")

    if guess in letters:
        print("You've already guessed that. Your guesses so far are", set(letters))

    elif guess in secret:
        print("Good guess! That letter was in the clue.\n")
        for x in range(length):
            if guess == secret[x]:
                blanks[x] = guess
        print(' '.join(blanks))
        print()

    else:
        print("Unlucky... That letter was not in the clue. Try again.")
        wrong_guesses += 1

        if wrong_guesses == 1:
            print(" ______  ")
            print("|      | ")
            print("|      O ")
            print("|        ")
            print("|        ")
            print("|________")
            print(' '.join(blanks))
            print()

        elif wrong_guesses == 2:
            print(" ______ ")
            print("|      |")
            print("|      O")
            print("|      |")
            print("|       ")
            print("|_______")
            print(' '.join(blanks))
            print()

        elif wrong_guesses == 3:
            print(" ______  ")
            print("|      | ")
            print("|      O ")
            print("|     /| ")
            print("|        ")
            print("|________")
            print(' '.join(blanks))
            print()

        elif wrong_guesses == 4:
            print(" ______   ")
            print("|      |  ")
            print("|      O  ")
            print("|     /|\\")
            print("|         ")
            print("|________ ")
            print(' '.join(blanks))
            print()

        elif wrong_guesses == 5:
            print(" ______   ")
            print("|      |  ")
            print("|      O  ")
            print("|     /|\\")
            print("|     /   ")
            print("|________ ")
            print(' '.join(blanks))
            print()

        elif wrong_guesses == 6:
            print(" ______   ")
            print("|      |  ")
            print("|      O  ")
            print("|     /|\\")
            print("|     / \\")
            print("|________ ")
            print("\nYou're dead. Game over. The word was " + word + ".")
            print()
            break

    letters.append(guess)

if secret == blanks:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You won. Congratulations!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
