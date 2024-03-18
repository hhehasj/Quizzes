replacement_words = []
lists_of_statements = []


def main():
    users_statement = input("Enter your statement:\n")
    users_statements_as_list = users_statement.split()

    word_to_replace = input("What word do you want to replace:\n")

    #   replacing chosen word with underscores
    for words in users_statements_as_list:
        if words == word_to_replace:
            underscored_word = len(words) * "_"
            replacement_words.append(underscored_word)

            index_of_underscored_word = users_statements_as_list.index(words)
            users_statements_as_list.pop(index_of_underscored_word)
            users_statements_as_list.insert(index_of_underscored_word, underscored_word)
            lists_of_statements.append(users_statements_as_list)

    for list_of_statements in lists_of_statements:
        for words in list_of_statements:
            print(words, end=" ")

if __name__ == "__main__":
    main()
