from tkinter.messagebox import showerror

import customtkinter as ctk
from PIL import Image

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

            def questions(questions):
                for question in users_questions:
                    Users_Questions.append(question)
                    self.questions_textbox.delete(0.0, "end")

            def answers(answers):
                for answer in answers.replace("\n", "").split(", "):
                    Users_Answers.append(answer)
                    self.answers_textbox.delete(0.0, "end")

            def choices(choices):
                for choice in users_choices:
                    one_group_of_choices: list[str] = choice.split(", ")

                    Users_Choices.append(one_group_of_choices)
                    self.choices_textbox.delete(0.0, "end")

            users_questions = self.questions_textbox.get(0.0, "end").splitlines()
            users_answers = self.answers_textbox.get(0.0, "end").upper()
            users_choices = self.choices_textbox.get(0.0, "end").splitlines()

            if users_questions != [""] and users_answers != "\n" and users_choices != [""]:  # There is an invisible \n character at the end of every string, and [""] is empty for .splitlines()

                for answer in users_answers.replace("\n", "").split(", "):
                    if answer == "A" or answer == "B" or answer == "C" or answer == "D":

                        for choice in users_choices:
                            one_group_of_choices: list[str] = choice.split(", ")

                            if len(one_group_of_choices) == 4:
                                questions(users_questions)
                                answers(users_answers)
                                choices(users_choices)

                            else:
                                showerror(title="Unfulfilled Requirement", message="Please enter 4 choices only")

                    else:
                        showerror(title="Unfulfilled Requirement", message="Answers must be A, B, C or D")

                print(Users_Questions)
                print(Users_Answers)
                print(Users_Choices)
        def show_preview():  # If there is an existing window, the current window is destroyed then replaced with a new & updated one
            if self.window_existence:
                self.preview_window.destroy()

            self.preview_window = Preview(self)
            self.window_existence = True

        # Variable
        self.window_existence: bool = False

        # Frame's configuration
        self.configure(fg_color=("#ebebeb", "808080"))
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
            command=store_questions_answers_choices
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

                # Displaying
                for question_number, question in enumerate(Users_Questions):
                    self.preview_textbox.configure(state="normal")

                    self.preview_textbox.insert("end", f"{question_number + 1}. {question}\n")

                    for letters_index, letter in enumerate(letters):
                        self.preview_textbox.insert("end",
                                                    f"{letter}. {Users_Choices[question_number][letters_index]}\n")

                    self.preview_textbox.insert("end", f'Ans: {Users_Answers[question_number]}\n')

                    self.preview_textbox.insert("end", "―" * 20 + "\n")

                    self.preview_textbox.configure(state="disabled")


class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Configuration
        self.configure(fg_color=("#ebebeb", "808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        self.start_btn = ctk.CTkButton(
            self,
            text="Start",
            font=("Helvetica", 30, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            border_color="black",
            border_width=3,
            command=self.start
        )
        self.start_btn.place(relx=0.5, rely=0.5, anchor="center")

    def start(self):
        # Images
        correct_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/check.png"),
            dark_image=Image.open("./icons_and_images/check.png")
        )

        wrong_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/wrong.png"),
            dark_image=Image.open("./icons_and_images/wrong.png")
        )

        # Variables
        question_num: int = 0

        for widget in self.winfo_children():
            widget.place_forget()

        try:
            self.Statements_display = ctk.CTkTextbox(
                self,
                font=("Helvetica", 24, "bold"),
                fg_color=("#ebebeb", "808080"),
                text_color=("black", "white"),
                wrap="word"
            )
            self.Statements_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")
            question_num += 1
            self.Statements_display.configure(state="disabled")
            self.Statements_display.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.5, relheight=0.2)

            self.first_radio_btn = ctk.CTkRadioButton(
                self,
                text="First"
            )
            self.first_radio_btn.place(relx=0.35, rely=0.45, anchor="center")


            self.second_radio_btn = ctk.CTkRadioButton(
                self,
                text="Second"
            )
            self.second_radio_btn.place(relx=0.35, rely=0.65, anchor="center")

            self.third_radio_btn = ctk.CTkRadioButton(
                self,
                text="Third"
            )
            self.third_radio_btn.place(relx=0.675, rely=0.45, anchor="center")

            self.fourth_radio_btn = ctk.CTkRadioButton(
                self,
                text="Fourth"
            )
            self.fourth_radio_btn.place(relx=0.675, rely=0.65, anchor="center")

            self.next_btn = ctk.CTkButton(
                self,
                text="NEXT",
                font=("Arial", 20, "bold"),
                text_color="black",
                corner_radius=10,
                border_color="black",
                border_width=2,
            )
            self.next_btn.place(relx=0.485, rely=0.835, anchor="center", relwidth=0.2, relheight=0.1)

        except IndexError:
            self.error_label = ctk.CTkLabel(
                self,
                text="You haven't entered any questions.\nPlease go to Make Questions.",
                font=("Helvetica", 35, "bold"),
                text_color=("black", "white")
            )
            self.error_label.place(relx=0.5, rely=0.5, anchor="center")
            quiz_started(False)


class Results(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Summary(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
