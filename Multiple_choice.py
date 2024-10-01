# Quiz
questions: list[str] = []
answers: list[str] = []
options_list: list[str] = []
guesses: list[str] = []
score: int = 0
question_num: int = 0
not_ended: bool = True
break_loop: bool = False
letters = ("A. ", "B. ", "C. ", "D. ")


while not_ended:
    print("―" * 20)
    choices: str = input("Make questions (make)\n"
                         "Start quiz (start)\n"
                         "Exit (ex)\n"
                         "> ")
    print("―" * 20)

    if choices == "make" or choices == "Make" or choices == "MAKE":
        while True:
            users_question: str = input("Question: ")
            if users_question == "b" or users_question == "B":
                break
            else:
                questions.append(users_question)

            users_answer: str = input("Answer: ")
            if users_answer == "b" or users_answer == "B":
                break
            else:
                answers.append(users_answer)

            for number_of_letters in range(len(letters)):
                users_options: str = input("Options: ")
                if users_options == "b" or users_options == "B":
                    break
                else:
                    options_list.append(users_options)
                print(options_list)

    elif choices == "start" or choices == "Start" or choices == "START":
        ...
    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break
    else:
        print(f"\033[91m\"{choices}\" is not a valid command\033[0m")


print("-----------------------------")
print("           RESULTS           ")
print("-----------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

print(questions, answers, options_list)