import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

# Global Variables
Users_Statements: list[str] = []
Users_Blanks: list[str] = []
Users_Guess: list[str] = []
score: int = 0
start_button_pressed: bool = False


# allows me to change the boolean value of start_button_pressed to disable or enable Make_Start_buttons
def quiz_started(value: bool):
    global start_button_pressed
    start_button_pressed = value


def get_start_button_pressed():
    return start_button_pressed


class Make_Statements(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        def stores_and_displays():
            """
            Displays the output of the statements that will be used in the quiz.
            Then the other textboxes will be empty.
            """""

            if self.statements_textbox.get(1.0, "end") == "\n" and self.chosen_word_textbox.get(1.0, "end") == "\n":
                showerror(title="Empty field", message="Both textboxes are empty.")

            elif self.statements_textbox.get(1.0, "end") == "\n" or self.chosen_word_textbox.get(1.0, "end") == "\n":
                showerror(title="Empty field", message="One of the textboxes is empty.")

            else:
                users_statements: list[str] = store_statements()
                statement_with_blank: list[str] = statement_to_blank()

                for number, statement in enumerate(users_statements):
                    self.preview_box.configure(state="normal")

                    self.preview_box.insert("end", f"{statement}\n")
                    Users_Statements.append(statement)

                    self.preview_box.insert("end", f"{statement_with_blank[number]}\n")
                    Users_Blanks.append(statement_with_blank[number])

                    self.preview_box.insert("end", "―" * 15 + "\n")

                self.preview_box.configure(state="disabled")

                self.statements_textbox.delete(0.0, "end")
                self.chosen_word_textbox.delete(0.0, "end")

        def store_statements() -> list[str]:
            statements: list[str] = []
            users_input: str = self.statements_textbox.get("1.0", "end")

            users_input = users_input.replace("\t", "")
            users_input: list[str] = users_input.splitlines()

            for statement in users_input:
                statements.append(statement)
            return statements

        def statement_to_blank() -> list[str]:
            new_statement: list[str] = []
            initial_statement: str = self.statements_textbox.get(1.0, "end")
            chosen_word: str = self.chosen_word_textbox.get(1.0, "end")

            initial_statement = initial_statement.replace("\t", "")
            statements_list: list[str] = initial_statement.splitlines()
            chosen_word = chosen_word.replace("\t", "")
            chosen_words_list: list[str] = chosen_word.splitlines()

            for index, statement in enumerate(statements_list):
                if statement.find(chosen_words_list[index]) != -1:
                    new_statement.append(statement.replace(chosen_words_list[index], "_" * len(chosen_words_list[index])))
                else:
                    showerror(title="Word not found", message="The word you chose is not in the statement.")

            return new_statement

        # Frame's configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        # Where you enter your questions
        self.statements_textbox_label = ctk.CTkLabel(
            self,
            text="Statements",
            font=("Arial", 25),
            text_color=("black", "white"),
        )
        self.statements_textbox_label.place(relx=0.25, rely=0.15, anchor="center")

        self.statements_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.statements_textbox.place(relx=0.26, rely=0.3, anchor="center", relwidth=0.35, relheight=0.2)

        # Where you enter the answers to the questions
        self.chosen_word_to_blank_label = ctk.CTkLabel(
            self,
            text="The word you want\nto turn into a blank",
            font=("Arial", 20),
            text_color=("black", "white"),
        )
        self.chosen_word_to_blank_label.place(relx=0.25, rely=0.48, anchor="center")

        self.chosen_word_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.chosen_word_textbox.place(relx=0.26, rely=0.65, anchor="center", relwidth=0.35, relheight=0.2)

        # stores the question and answer
        self.next_button = ctk.CTkButton(
            self,
            text="Next",
            font=("Helvetica", 20, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            border_color="black",
            border_width=3,
            border_spacing=10,
            command=stores_and_displays
        )
        self.next_button.place(relx=0.25, rely=0.88, anchor="center")

        # Preview box that displays the questions and its answers
        self.preview_box = ctk.CTkTextbox(
            self,
            state="disabled",
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
            font=("Helvetica", 15)
        )
        self.preview_box.place(relx=0.77, rely=0.5, anchor="center", relwidth=0.4, relheight=0.9)


class Start_Quiz(ctk.CTkFrame):
    ...

class Results(ctk.CTkFrame):
    ...

class Summary(ctk.CTkFrame):
    ...