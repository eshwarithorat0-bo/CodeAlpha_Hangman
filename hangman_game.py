import random

words = ["python", "apple", "computer", "college", "coding"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("\n===== WELCOME TO HANGMAN =====")
print("Guess the hidden word one letter at a time!")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over!")
    print("The correct word was:", word)

print("Thank you for playing!")