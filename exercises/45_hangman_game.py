# Exercise 1 from lesson 45
# Hangman in Python

import random

words = (
    "apple", "orange", "banana", "coconut", "pineapple", "grapefruit", "kiwi", "mango",
    "strawberry", "blueberry", "watermelon", "peach", "pear", "plum", "cherry", "apricot",
    "lemon", "lime", "avocado", "tomato", "carrot", "potato", "onion", "lettuce", "cucumber",
    "broccoli", "pepper", "pumpkin", "spinach", "zucchini", "eggplant", "chicken", "turkey",
    "beef", "salmon", "shrimp", "tuna", "cheese", "bread", "butter", "yogurt", "pizza", "burger",
    "pasta", "sushi", "noodles", "rice", "cake", "cookie", "chocolate", "icecream", "donut",
    "pancake", "waffle", "sandwich", "milk", "coffee", "tea", "juice", "soda", "water",
    "lion", "tiger", "bear", "zebra", "giraffe", "elephant", "monkey", "panda", "dog", "cat",
    "rabbit", "mouse", "horse", "shark", "dolphin", "eagle", "owl", "snake", "lizard", "frog",
    "spoon", "fork", "knife", "plate", "cup", "glass", "bottle", "phone", "laptop", "tablet",
    "keyboard", "screen", "window", "door", "chair", "table", "pillow", "blanket", "couch",
    "book", "pencil", "pen", "notebook", "paper", "clock", "watch", "lamp", "shoe", "sock",
    "shirt", "pants", "hat", "jacket", "scarf", "glove", "umbrella", "backpack", "wallet",
    "bicycle", "car", "truck", "train", "plane", "boat", "rocket", "helmet"
)

# dictionary of key:()
hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               1: ("  𝗼  ",
                   "     ",
                   "     "),
               2: ("  𝗼  ",
                   "  |  ",
                   "     "),
               3: ("  𝗼  ",
                   " /|  ",
                   "    "),
               4: ("  𝗼  ",
                   " /|\\ ",
                   "     "),
               5: ("  𝗼  ",
                   " /|\\ ",
                   " /   "),
               6: ("  𝗼  ",
                   " /|\\ ",
                   " / \\ ")}


def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()