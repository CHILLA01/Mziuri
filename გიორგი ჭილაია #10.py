import random


words = ["apple", "orange", "banana", "grapes", "cherry", "peach", "mango", "lemon", "pear", "kiwi"]



def play_word_jumble():
    print("Welcome to Word Jumble!")
    print("Guess the original word or type 'quit' to exit.")

    while True:

        original_word = random.choice(words)

        jumbled = list(original_word)
        random.shuffle(jumbled)
        jumbled = ''.join(jumbled)


        print(f"\nJumbled word: {jumbled}")


        user_guess = input("Your guess: ")


        if user_guess == "quit":
            print("Thanks for playing! Goodbye!")
            break


        if user_guess == original_word:
            print("Correct!")
        else:
            print(f"Wrong! The correct word was '{original_word}'.")


play_word_jumble()
