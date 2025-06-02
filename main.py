import random
import hangman_words
import hangman_art

lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""

for position in chosen_word:
    placeholder += "_"
print(placeholder)

game_loop = True
correct_letters = []

while game_loop:
    print(f"****************************<???>{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        print(f"{guess}, It's not in the word")
        lives -= 1

    if guess in chosen_word:
        print(hangman_art.stages[6])
    elif lives == 0:
        print(hangman_art.stages[lives])
        print("***********************YOU LOSE**********************")
        break
    elif guess not in chosen_word:
        print(hangman_art.stages[lives])

    if display == chosen_word:
        print("****************************YOU WIN****************************")
