questions = []
correct_answers = []
choices = []
correct_answers_lowercase = []


def displaying_questions_and_choices():
    count = 0
    players_score = 0
    total_points = len(correct_answers)

    print("-------------------------------------------------")
    # to show the questions
    for i_for_question in range(len(questions)):
        print(f"{i_for_question+1}.) {questions[i_for_question]}")
        # displaying the choices
        for choice in choices[count]:
            print(f"{choice}")
        players_answer = input("Answer: ")
        count += 1
        print("─────────────────────────────────────────────────")
        # checking if the answer of player is correct
        if players_answer == correct_answers[i_for_question]:
            print("You got it  ┃\n━━━━━━━━━━━━━")
            players_score += 1
        elif players_answer == correct_answers_lowercase[i_for_question]:
            print("You got it  ┃\n━━━━━━━━━━━━━")
            players_score += 1
        else:
            horizontal_line = "━"
            length_of_correct_answer = len(correct_answers[i_for_question])
            print(f"Wrong! Correct Answer: {correct_answers[i_for_question]}  ┃\n{horizontal_line * (length_of_correct_answer + 26)}")

    print(f"Total score: {total_points}\nYou got {players_score}")
    if players_score < total_points / 2:
        print("DISAPPOINTMENT!!!😔")
    else:
        print("You passed! 😁👌")


def backend_of_make_option():
    users_questions = input("Enter one question:\n")
    questions.append(users_questions)
    users_correct_answers = input("Enter the answer to the question:\n")
    correct_answers.append(users_correct_answers)
    correct_answers_lowercase.append(users_correct_answers.lower())
    users_choices = input("Give 4 choices for the question:\n").split()
    choices.append(users_choices)


def command_interface():
    users_choice = input("(make) to make questions, choices, and the answer"
                         "\n(q) to quit"
                         "\n(start) to begin the quiz"
                         "\n> ").lower()

    # if user chooses "make"
    if users_choice == "make":
        backend_of_make_option()
        # to make another question or to go to command interface
        while users_choice != "N":
            users_choice = input("Do you want to make another question (Y/N)? ").upper()
            if users_choice == "Y":
                backend_of_make_option()
            elif users_choice == "N":
                print("-------------------------------------------------")
                command_interface()
            else:
                print(f"\"{users_choice}\" WHAT DO YOU MEAN!")

    # if user chooses "start"
    elif users_choice == "start":
        try:
           displaying_questions_and_choices()

# once player has entered his/her answer
        except ZeroDivisionError:
            command_interface()

    # if user chooses "q"
    elif users_choice == "q":
        exit()

    # if user didn't put any command
    else:
        command_interface()


if __name__ == "__main__":
    command_interface()
