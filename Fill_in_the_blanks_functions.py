lists_of_statements = []
words_to_replace = []


def main():
    while True:
        print("(make) to make\n(start) to start quiz\n(q) to quit")
        command = input(">")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if command.lower() == "make":
            make()
        elif command.lower() == "start":
            if len(lists_of_statements) <= 0:  # So that you can't start the quiz without inputting your statements first
                main()
            else:
                answering()
        elif command.lower() == "q":
            quit()
        else:
            print(f"\"{command}\" was invalid. Enter a valid command.\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def make():
    statement = input("Enter your statement:\n")
    statement_list = statement.split()

    replaced_word = input("What word do you want to replace:\n")
    print("──────────────────────────────")
    words_to_replace.append(replaced_word)

    #   replacing chosen word with underscores
    for words in statement_list:
        if words == replaced_word:
            underscored_word = len(words) * "_"

            index = statement_list.index(words)  # Getting index of the word chosen to be replaced

            # removes the chosen word then replaces it with the blank version
            statement_list.pop(index)
            statement_list.insert(index, underscored_word)
            lists_of_statements.append(statement_list)  # adds statement_list to lists_of_statements making a 2D list
    main()


def answering():
    score = 0
    total_points = 0
    joined_statement = " "

    # displaying statements
    for list_of_statements in lists_of_statements:
        total_points += len(lists_of_statements)
        print(joined_statement.join(list_of_statements))

    # once player answers
    answer = input("Answer: ")
    for word_to_replace in words_to_replace:  # checking if answer is correct or wrong
        if answer == word_to_replace:
            print('✅')
            score += 1
        else:
            print("❌")

    # if the player's score is above passing score or not
    print(f"You got {score}/{total_points}!")
    if score > total_points / 2:
        print("😁\n━━━━━━━━━━")
    elif total_points / 2 > score > 0:
        print("🥲\n━━━━━━━━━━")
    elif score == 0:
        print("DISAPPOINTMENT! 😤\n━━━━━━━━━━")

    ending_choice()  # After all questions have been answered


def ending_choice():
    ending_decision = input("(redo) to redo the set quiz\n(res) to reset quiz\n(q) to quit\n>>")
    if ending_decision.lower() == "q":
        quit()
    elif ending_decision.lower() == "redo":
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        answering()  # uses the previous statements
    elif ending_decision.lower() == "res":
        #  clears the lists, allowing a new batch of statements in the quiz
        lists_of_statements.clear()
        words_to_replace.clear()
        main()


# this is just a convenience
if __name__ == '__main__':
    main()
