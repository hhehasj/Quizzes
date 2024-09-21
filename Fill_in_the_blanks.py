statements: list[str] = []
blanks: list[str] = []
guesses: list[str] = []
score: int = 0
question_num: int = 0
not_ended = True

while not_ended:
    print("―" * 20)
    choices: str = input("Make questions (make)\n"
                         "Start quiz (start)\n"
                         "Exit (ex)\n"
                         "> ")
    print("―" * 20)

    if choices == "make" or choices == "Make" or choices == "MAKE":
        while True:
            users_statement: str = input("Statement: ")

            if users_statement == "b" or users_statement == "B":
                break

            else:
                statements.append(users_statement)

            chosen_word: str = input("Chosen word: ")
            blank: str = "_" * len(chosen_word)

            if chosen_word == "b" or chosen_word == "B":
                break
            else:
                blanks.append(blank)

    elif choices == "start" or choices == "Start" or choices == "START":
        ...

    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break

    else:
        print(f"\033[91m{choices} is not a valid command\033[0m")
