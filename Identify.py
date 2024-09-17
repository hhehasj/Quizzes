questions = []
answers = []
guesses = []
score = 0
question_num = 0

while True:
    print("―" * 20)
    choices = input("Make questions (que)\n"
                    "Answers to the questions (ans)\n"
                    "Start quiz (start)\n"
                    "Exit (ex)\n> ")
    print("―" * 20)

    if choices == "que" or choices == "Que" or choices == "QUE":
        while True:
            users_question = input("Question: ")

            if users_question == "b" or users_question == "B":
                break
            else:
                questions.append(users_question)

    elif choices == "ans" or choices == "Ans" or choices == "ANS":
        while True:
            users_answer = input("Answer to the question: ")

            if users_answer == "b" or users_answer == "B":
                print("\n")
                break
            else:
                answers.append(users_answer)

    elif choices == "start" or choices == "Start" or choices == "START":
        pass

    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break

    else:
        print(f"\033[91m \"{choices}\" is not a valid command.\033[0m")

