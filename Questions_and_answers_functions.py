questions = []
answers = []
answers_lowercase = []
answers_uppercase = []


def commands_looping():
    print("Commands:\n(que) to enter a question\n(ans) to enter the answer to the question\n(start) to start program\n"
          "(q) to end the program")
    users_input = input("> ").lower()
    # Questions
    while users_input != "q":
        if users_input == "que":
            print("(b) to go back to the commands list")
            questions_from_user = input(">> ")
            if questions_from_user != "b" and questions_from_user != "B":
                questions.append(questions_from_user)
            if questions_from_user.lower() == "b":
                print()
                commands_looping()
        # Answers
        elif users_input == "ans":
            print("(b) to go back to the commands list")
            answers_to_questions = input(">>> ")
            if answers_to_questions != "b" and answers_to_questions != "B":
                answers.append(answers_to_questions)
                answers_uppercase.append(answers_to_questions.title())
                answers_lowercase.append(answers_to_questions.lower())
            if answers_to_questions.lower() == "b":
                print()
                commands_looping()
        # Start
        elif users_input == "start":
            try:
                print()
                checks_answer()
            except ZeroDivisionError:
                commands_looping()


# Checks if your answer is correct
def checks_answer():
    total_points = 0
    ans = []
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        total_points += 1
        anr = input("Enter your answer:\n")
        ans.append(anr)
        if anr == answers[i]:
            print("Correct!")
            score += 1
        elif anr == answers_lowercase[i]:
            print("Correct!")
            score += 1
        elif anr == answers_uppercase[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print("------------------------------------------------------")
    percentage = score / total_points * 51 + 49
    # Aesthetics

    print()
    for a in range(len(answers)):
        print(f"CORRECT ANSWER: {answers[a]:}\nYOUR ANSWER: {ans[a]:}\n")
    print(f'Score:\nYour score is {score}/{total_points} or {percentage}%')
    print()
    res_or_replay = input("(res) to restart program\n(r) to replay the program\n> ")
    if res_or_replay.lower() == "res":
        questions.clear()
        answers.clear()
        answers_uppercase.clear()
        answers_uppercase.clear()
        print()
        commands_looping()
    elif res_or_replay.lower() == "r":
        print()
        checks_answer()


if __name__ == "__main__":
    commands_looping()
