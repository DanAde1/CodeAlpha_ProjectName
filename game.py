import random
words = ["goat", "ewe", "scandalous", "banana", "computer"]
secret_word = random.choice(words)
display_word = ["_"] * len(secret_word)
lives = 6
guessed_letters = []
while lives > 0:
    print(" ".join(display_word))
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct!")
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display_word[position] = guess
    else:
        print("Incorrect!")
        lives -= 1
        print("wrong guess")
    print("lives left:", lives)
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break
if lives == 0:
    print("Game over! The word was:", secret_word)
