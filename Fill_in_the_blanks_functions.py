<<<<<<< HEAD
replacement_words = []


def main():
    users_statement = input("Enter your statement:\n")
    users_statement_as_list = users_statement.split()

    word_to_replace = input("What word do you want to replace:\n")

    #   replacing chosen word with underscores
    for words in users_statement_as_list:
        if words == word_to_replace:
            underscored_word = len(words) * "_"
            replacement_words.append(underscored_word)
            index_of_underscored_word = users_statement_as_list.index(words)
            users_statement_as_list.pop(index_of_underscored_word)
            users_statement_as_list.insert(index_of_underscored_word, underscored_word)




#   putting replace_words into the statement

if __name__ == "__main__":
    main()
=======
if __name__ == "__main__":
    command_line()
>>>>>>> a6cbd2fd5ab98b6eaad7900ed2c4120b0dfa3c99
