import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

Users_Questions: list[str] = []
Users_Choices: list[list[str]] = []
Users_Answers: list[str] = []
Users_Guess: list[str] = []
score: int = 0
start_btn_pressed: bool = False


def quiz_started(value: bool):
    global start_btn_pressed
    start_btn_pressed = value


def get_start_btn_pressed():
    return start_btn_pressed


class Make_Questions(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        def store_questions_answers_choices():
            users_questions = self.questions_textbox.get(0.0, "end").splitlines()
            users_answers = self.answers_textbox.get(0.0, "end").upper()
            users_choices = self.choices_textbox.get(0.0, "end").splitlines()

            if users_questions != [""] and users_answers != "\n" and users_choices != [""]:

                for question in users_questions:
                    Users_Questions.append(question)
                    self.questions_textbox.delete(0.0, "end")

                for answer in users_answers.replace("\n", "").split(", "):

                    if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                        Users_Answers.append(answer.upper().replace("\n", ""))
                        self.answers_textbox.delete(0.0, "end")

                    else:
                        showerror(title="Requirement Unfulfilled", message="Only A, B, C, D is allowed. No other letter or character.")
                        Users_Questions.pop()

                for choice in users_choices:
                    one_group_of_choices: list[str] = choice.split(", ")

                    if len(one_group_of_choices) == 4:
                        Users_Choices.append(one_group_of_choices)
                        self.choices_textbox.delete(0.0, "end")

                    else:
                        showerror(title="Requirement Unfulfilled", message="The Choices field requires 4 choices only.")
                        Users_Questions.pop()

            else:
                showerror(title="Empty Field", message="Please fill in all fields :)")

            print(Users_Questions)
            print(Users_Answers)
            print(Users_Choices)

        def show_preview():
            if self.window_existence:
                self.preview_window.destroy()

            self.preview_window = Preview(self)
            self.window_existence = True

        # Variable
        self.window_existence: bool = False

        # Frame's configuration
        self.configure(fg_color=("#ebebeb", "808080"))
        # self.configure(fg_color="red")
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        self.questions_label = ctk.CTkLabel(
            self,
            text="QUESTIONS",
            font=("Arial", 25, "bold"),
            text_color=("black", "white")
        )
        self.questions_label.place(relx=0.195, rely=0.11, anchor="center")

        self.questions_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 14),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.questions_textbox.place(relx=0.2, rely=0.2, anchor="n", relwidth=0.35, relheight=0.75)

        self.choices_label = ctk.CTkLabel(
            self,
            text="CHOICES",
            font=("Arial", 25, "bold"),
            text_color=("black", "white")
        )
        self.choices_label.place(relx=0.565, rely=0.11, anchor="center")

        self.choices_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 14),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.choices_textbox.place(relx=0.57, rely=0.2, anchor="n", relwidth=0.35, relheight=0.75)

        self.answers_label = ctk.CTkLabel(
            self,
            text="ANSWERS",
            font=("Arial", 20, "bold"),
            text_color=("black", "white")
        )
        self.answers_label.place(relx=0.87, rely=0.11, anchor="center")

        self.answers_textbox = ctk.CTkTextbox(
            self,
            font=("Arial", 15, "bold"),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.answers_textbox.place(relx=0.873, rely=0.2, anchor="n", relwidth=0.2, relheight=0.2)

        self.enter_btn = ctk.CTkButton(
            self,
            text="Enter",
            font=("Arial", 20, "bold"),
            text_color="black",
            corner_radius=10,
            border_width=2,
            border_color="black",
            command= store_questions_answers_choices
        )
        self.enter_btn.place(relx=0.873, rely=0.65, anchor="center", relwidth=0.2, relheight=0.1)

        self.preview_btn = ctk.CTkButton(
            self,
            text="Preview",
            font=("Arial", 20, "bold"),
            text_color="black",
            corner_radius=10,
            border_width=2,
            border_color="black",
            command=show_preview
        )
        self.preview_btn.place(relx=0.873, rely=0.5, anchor="center", relwidth=0.2, relheight=0.1)

        class Preview(ctk.CTkToplevel):
            def __init__(self, parent):
                super().__init__(parent)

                letters: tuple[str, str, str, str] = ("A", "B", "C", "D")

                self.geometry("300x300")
                self.title("Preview Window")
                self.attributes("-topmost", True)

                self.preview_textbox = ctk.CTkTextbox(
                    self,
                    fg_color="white",
                    text_color="black",
                    font=("Arial", 12, "bold"),
                    corner_radius=10,
                    border_width=2,
                    border_color="black",
                    wrap="word"
                )
                self.preview_textbox.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.95)

                # Entering questions, choices, and answers into textbox
                # try:
                for question_number, question in enumerate(Users_Questions):
                    self.preview_textbox.configure(state="normal")

                    self.preview_textbox.insert("end", f"{question_number + 1}. {question}\n")

                    for letters_index, letter in enumerate(letters):
                        self.preview_textbox.insert("end", f"{letter}. {Users_Choices[question_number][letters_index]}\n")

                    self.preview_textbox.insert("end", f'Ans: {Users_Answers[question_number]}\n')

                    self.preview_textbox.insert("end", "―" * 20 + "\n")

                    self.preview_textbox.configure(state="disabled")

                # except IndexError:
                #     showerror(title="Requirement Unfulfilled", message="The Choices field requires 4 choices only.")
                #     Users_Questions.pop()
                #     Users_Choices.pop()
                #     Users_Answers.pop()



class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Results(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Summary(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)