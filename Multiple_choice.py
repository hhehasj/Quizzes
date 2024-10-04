# Quiz
statements: list[str] = []
answers: list[str] = []
guesses: list[str] = []
score: int = 0
question_num: int = 0
not_ended: bool = True
break_loop: bool = False
users_options: list[str] = []
options: list[list[str]] = []
letters: list[str] = ["A. ", "B. ", "C. ", "D. "]


def combine(*args) -> None:
    combined_list: list[str] = []

    for list_in_args in args:
        for index in range(len(list_in_args)):
            combined = letters[index] + list_in_args[index]
            combined_list.append(combined)

        options.append(combined_list)


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
            if users_statement == "exit" or users_statement == "Exit":
                break
            else:
                statements.append(users_statement)

            option_A: str = input("A. ")
            if option_A == "exit" or option_A == "Exit":
                break
            else:
                users_options.append(option_A)

            option_B: str = input("B. ")
            if option_B == "exit" or option_B == "Exit":
                break
            else:
                users_options.append(option_B)

            option_C: str = input("C. ")
            if option_C == "exit" or option_C == "Exit":
                break
            else:
                users_options.append(option_C)

            option_D: str = input("D. ")
            if option_D == "exit" or option_D == "exit":
                break
            else:
                users_options.append(option_D)
                copy_of_options = users_options.copy()
                users_options.clear()

            combine(copy_of_options)

            users_answer: str = input("Answer: ")
            if users_answer == "exit" or users_answer == "Exit":
                break
            else:
                answers.append(users_answer)

    elif choices == "start" or choices == "Start" or choices == "START":
        try:
            for statement in statements:
                print(statement)

                for option in options[question_num]:
                    print(option)

                guess: str = input("Guess (A, B, C, D): ")
                guesses.append(guess)

                if guess.upper() == answers[question_num]:
                    score += 1
                    print("CORRECT!")
                    print("―" * 20)
                else:
                    print("WRONG!")
                    print(f"{answers[question_num]} is the correct answer.")
                    print("――――――――――――――――――――――――――――")

                question_num += 1
        except IndexError:
            print("An error occured")

    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break
    else:
        print(f"\033[91m\"{choices}\" is not a valid command\033[0m")


print("           RESULTS           ")
print("―" * 20)

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(statements) * 100)
print(f"Your score is: {score}%")
