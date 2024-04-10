statement_list: list[str] = []
blank_words_list: list[str] = []
blank_list: list[str] = []

choice: str = input("(m) to make\n(s) to start\n(q) to quit\n> ")


def making_blank_word(chosen_word):
    blank = len(chosen_word) * "_"
    blank_list.append(blank)


def response(users_choice):
    if users_choice.lower() == "m":
        statement = input("Statement: ")
        statement_list.append(statement)
        blank_word = input("Word to become blank: ")
        blank_words_list.append(blank_word)
        making_blank_word(blank_word)

        print(blank_list)
        print(blank_words_list)

    elif users_choice.lower() == "s":
        start()

    elif users_choice.lower() == "q":
        quit()
    else:
        print(f"\"{choice}\" is not valid. Enter a valid command!")




def start():
    print('starting')


if __name__ == '__main__':
    response(choice)