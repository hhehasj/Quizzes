questions = []
answers = []
guesses = []
score = 0
question_num = 0
not_started = True

# Commands
choices = input("Questions (que)\nAnswers (ans)\nStart quiz (start)\nexit (ex)\n>")

while not_started:
    if choices == "que" or choices == "QUE":
        que_of_user = input("――――――――――――――――――――――――――――\n>>")
        questions.append(que_of_user)

    elif choices == "ans" or choices == "ANS":
        ans_of_user = input("――――――――――――――――――――――――――――\n>>>")
        answers.append(ans_of_user)

    elif choices == "start" or choices == "START":
        not_started = False

    elif choices == "ex" or choices == "EX":
        quit()

    else:
        print(f"\"{choices}\" is not a valid command.\n――――――――――――――――――――――――――――")
