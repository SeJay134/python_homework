# Task 4

def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(a_letter):
        guesses.append(a_letter)

        displayed = ""
        for char in secret_word:
            if char in guesses:
                displayed += char
            else:
                displayed += "_"
        print(displayed)

        return "_" not in displayed

    return hangman_closure

def main():
    secret_word = input("Enter the secret word:").strip().lower()
    hangman = make_hangman(secret_word)
    print("\n Start game")

    while True:
        guess = input("Enter the guess letter:").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Wrong, try to enter again")
            continue

        word_finished = hangman(guess)
        if word_finished:
            print("You win, the secret word is:", secret_word)
            break

if __name__ == "__main__":
    main()