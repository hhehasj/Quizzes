statements: list[str] = []
answers: list[str] = []
guesses: list[str] = []
score: int = 0
question_num: int = 0
not_ended = True


def convert_statement(statement, word, blank):
    statement_list: list[str] = statement.split()
    index_of_chosen_word: int = statement_list.index(word)

    statement_list.pop(index_of_chosen_word)
    statement_list.insert(index_of_chosen_word, blank)
    new_string: str = " ".join(statement_list)

    return new_string


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

            chosen_word: str = input("Chosen word: ")

            blank: str = "_" * len(chosen_word)
            converted_statement: str = convert_statement(statement=users_statement, word=chosen_word, blank=blank)

            if chosen_word == "b" or chosen_word == "B":
                break
            else:
                statements.append(converted_statement)
                answers.append(chosen_word)

    elif choices == "start" or choices == "Start" or choices == "START":
        for statement in statements:
            print(statement)
            guess: str = input("Your answer: ")
            guesses.append(guess)

            if guess == answers[question_num]:
                print("Correct!")
                print("-" * 20)
                score += 1
            else:
                print("Wrong!")
                print("-" * 20)

            question_num += 1

        not_ended = False

    elif choices == "ex" or choices == "Ex" or choices == "EX":
        break

    else:
        print(f"\033[91m{choices} is not a valid command\033[0m")

# Scores
print("Results".center(35))
print("_" * 20)

print("Answers: ", end="|")
for answer in answers:
    print(answer, end="|")
print()

print("Guesses: ", end="|")
for guess in guesses:
    print(guess, end="|")
print()

score = int(score / len(statements) * 100)
print(f"Your score is: {score}%")