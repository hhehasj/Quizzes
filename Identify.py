questions: list[str] = []
answers: list[str] = []
guesses: list[str] = []
score: int = 0
question_num: int = 0
not_ended: bool = True

while not_ended:
    print("―" * 20)
    choices: str = input("Make questions (que)\n"
                         "Answers to the questions (ans)\n"
                         "Start quiz (start)\n"
                         "Exit (ex)\n> ")
    print("―" * 20)

    if choices == "que" or choices == "Que" or choices == "QUE":
        while True:
            users_question: str = input("Question: ")

            if users_question == "b" or users_question == "B":
                break
            else:
                questions.append(users_question)

    elif choices == "ans" or choices == "Ans" or choices == "ANS":
        while True:
            users_answer: str = input("Answer to the question: ")

            if users_answer == "b" or users_answer == "B":
                break
            else:
                answers.append(users_answer)

    elif choices == "start" or choices == "Start" or choices == "START":
        for question in questions:
            print(question)
            guess: str = input("Your answer: ")
            guesses.append(guess)

            if guess == answers[question_num]:
                print("Correct!")
                print("―" * 20)
                score += 1
            else:
                print("Wrong")
                print("―" * 20)

            question_num += 1

        not_ended = False

    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break

    else:
        print(f"\033[91m \"{choices}\" is not a valid command.\033[0m")


# Scoring system
print("             Results                     ")
print("―" * 20)

print("Answers: ", end="|")
for answer in answers:
    print(answer, end="|")
print()

print("Guesses: ", end="|")
for guess in guesses:
    print(guess, end="|")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")