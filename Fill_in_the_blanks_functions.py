replacement_words = []
lists_of_statements = []
words_to_replace = []


def main():
    users_statement = input("Enter your statement:\n")
    users_statements_as_list = users_statement.split()

    w_to_replace = input("What word do you want to replace:\n")
    words_to_replace.append(w_to_replace)

    #   replacing chosen word with underscores
    for words in users_statements_as_list:
        if words == w_to_replace:
            underscored_word = len(words) * "_"
            replacement_words.append(underscored_word)

            index_of_underscored_word = users_statements_as_list.index(words)
            users_statements_as_list.pop(index_of_underscored_word)
            users_statements_as_list.insert(index_of_underscored_word, underscored_word)
            lists_of_statements.append(users_statements_as_list)

    # to display the statement and its missing word
    answering()


def answering():
    score = 0
    total_points = 0
    for list_of_statements in lists_of_statements:
        total_points += len(lists_of_statements)
        for words in list_of_statements:
            print(words, end=" ")
    answer_of_user = input("|Answer: ")
    for word_to_replace in words_to_replace:
        if answer_of_user == word_to_replace:
            print('Correct!!!\n━━━━━━━━━━')
            score += 1
        else:
            print("Wrong!!!\n━━━━━━━━━━")
    print(f"You got {score}/{total_points}!")
    if score > total_points / 2:
        print("😁")
    elif total_points / 2 > score > 0:
        print("🥲")
    elif score == 0:
        "DISAPPOINTMENT! 😤"


if __name__ == '__main__':
    main()
