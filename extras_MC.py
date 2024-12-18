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
            users_answers = self.answers_textbox.get(0.0, "end")
            users_choices = self.choices_textbox.get(0.0, "end").splitlines()

            if users_questions != [""] and users_answers != "\n" and users_choices != [""]:

                for question in users_questions:
                    Users_Questions.append(question)

                for answer in users_answers.split(", "):
                    Users_Answers.append(answer.upper().replace("\n", ""))

                for choice in users_choices:
                    one_group_of_choices: list[str] = choice.split(", ")
                    Users_Choices.append(one_group_of_choices)

            else:
                showerror(title="Empty Field", message="Please fill in all fields :)")

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
            text_color=("black", "white"),
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
            text_color=("black", "white"),
            corner_radius=10,
            border_width=2,
            border_color="black",
            # command=
        )
        self.preview_btn.place(relx=0.873, rely=0.5, anchor="center", relwidth=0.2, relheight=0.1)


class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Results(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Summary(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)