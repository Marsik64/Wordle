import random

def generate_word():
    words = ["абзац", "ангел", "архив", "багаж", "банан", "белка", "вагон", "ветка", "время", "вызов", "глина", "дверь", "дрель", "замок", "капля", "лапша", "макет", "налог", "океан", "ответ"] # список возможных слов
    return random.choice(words)

def check_guess(word, guess):
    if word == guess:
        return True

    for i in range(len(word)):
        if word[i] == guess[i]:
            print("\033[32m{}".format(guess[i]), end=" ") # отображаем букву зеленыи цветом (буква есть, на своём месте)
        elif guess[i] in word:
            print("\033[33m{}".format(guess[i]), end=" ") # отображаем букву желтым цветом (буква есть, но не на своем месте)
        else:
            print("\033[31m{}".format(guess[i]), end=" ") # отображаем букву красным цветом (буквы нет в слове)
    print()

    return False

def play_wordle():
    word = generate_word()
    attempts = 5
    guessed = False

    print("\nby. Marsel Sofronitsky, group 6110\n")
    print("Добро пожаловать в игру Wordle!")
    print("Угадайте задуманное слово. У вас есть", attempts, "попыток. Количество букв в слове - 5.")
    print("Каждая угаданная буква будет зеленой. Если буква содержится в слове, но стоит не в правильном месте, она будет желтой. Если буквы нет в слове, она будет красной.")

    while attempts > 0 and not guessed:
        guess = input("\033[37m{}".format("Введите вашу догадку: ")).lower()

        if len(guess) != len(word):
            print("\033[31m{}".format("Неверное количество букв. Попробуйте снова."))
            continue

        if check_guess(word, guess):
            guessed = True
            print("\033[32m{}".format("Поздравляю! Вы угадали слово - "), word)
        else:
            attempts -= 1
            print("\033[33m{}".format("Неверное слово. Осталось"), attempts, "попыток.")

    if not guessed:
        print("\033[31m{}".format("К сожалению, вы не угадали слово. Задуманное слово было - "), word)

play_wordle()
