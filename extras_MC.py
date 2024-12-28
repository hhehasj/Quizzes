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

            def questions():
                for question in users_questions:
                    Users_Questions.append(question)
                    self.questions_textbox.delete(0.0, "end")

            def return_answer():
                return users_answers.replace("\n", "").split(", ")

            def return_choices():
                for choice in users_choices:
                    one_group_of_choices: list[str] = choice.split(", ")
                    return one_group_of_choices

            users_questions = self.questions_textbox.get(0.0, "end").splitlines()
            users_answers = self.answers_textbox.get(0.0, "end").upper()
            users_choices = self.choices_textbox.get(0.0, "end").splitlines()

            if users_questions != [""] and users_answers != "\n" and users_choices != [""]:  # There is an invisible \n character at the end of every string, and [""] is empty for .splitlines()

                if any(answer not in ["A", "B", "C", "D"] for answer in return_answer()) and len(return_choices()) != 4:
                    showerror(title="REQUIREMENT NOT MET", message="Check Answers AND Choices.\nChoices can only have 4.\nAnswers must be A, B, C, or D.")

                elif any(answer not in ["A", "B", "C", "D"] for answer in return_answer()) or len(return_choices()) != 4:
                    showerror(title="REQUIREMENT NOT MET", message="Check Answers OR Choices.\nChoices can only have 4.\nAnswers must be A, B, C, or D.")

                else:
                    questions()

                    for answer in return_answer():
                        Users_Answers.append(answer)
                        self.answers_textbox.delete(0.0, "end")

                    for choice in users_choices:
                        one_group_of_choices: list[str] = choice.split(", ")
                        Users_Choices.append(one_group_of_choices)
                        self.choices_textbox.delete(0.0, "end")

        def show_preview():  # if there is an existing window, the current window is destroyed then replaced with a new & updated one
            if self.window_existence:
                self.preview_window.destroy()

            self.preview_window = Preview(self)
            self.window_existence = True

        # variable
        self.window_existence: bool = False

        # frame's configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # widgets
        self.questions_label = ctk.CTkLabel(
            self,
            text="QUESTIONS",
            font=("arial", 25, "bold"),
            text_color=("black", "white")
        )
        self.questions_label.place(relx=0.195, rely=0.11, anchor="center")

        self.questions_textbox = ctk.CTkTextbox(
            self,
            font=("helvetica", 14),
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
        self.configure(fg_color=("#ebebeb", "#808080"))
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
        def next_question():
            try:
                checking()

                self.Questions_display.configure(state="normal")
                self.Questions_display.delete(0.0, "end")

                self.Questions_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")

                self.Questions_display.configure(state="disabled")

            except IndexError:
                self.Questions_display.configure(state="normal")
                self.Questions_display.delete(0.0, "end")

                self.Questions_display.insert(0.0, "Test Over")

                self.Questions_display.configure(state="disabled")
                self.next_btn.configure(state="disabled")
                transition()

        def checking():
            nonlocal question_num
            global score

            question_num += 1
            Users_Guess.append(users_guess.get())

            if users_guess.get() != "" and users_guess.get() == Users_Answers[question_num - 1]:
                self.status_label.configure(image=correct_icon)
                score += 1

            elif users_guess.get() != "" and users_guess.get() != Users_Answers[question_num - 1]:
                self.status_label.configure(image=wrong_icon)

            else:
                showerror(title="You didn't choose one", message="Please choose!")
                question_num -= 1

            self.Questions_display.configure(state='normal')
            self.Questions_display.delete(0.0, "end")

            self.Questions_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")

            self.Questions_display.configure(state='disabled')

            self.first_radio_btn.configure(text=f"{letters[0]}. {Users_Choices[question_num][0]}")
            self.second_radio_btn.configure(text=f"{letters[1]}. {Users_Choices[question_num][1]}")
            self.third_radio_btn.configure(text=f"{letters[2]}. {Users_Choices[question_num][2]}")
            self.fourth_radio_btn.configure(text=f"{letters[3]}. {Users_Choices[question_num][3]}")

        def show_results():
            for Start_Quiz_widgets in self.winfo_children():
                Start_Quiz_widgets.place_forget()

            Results(parent=self.master)

        def transition():
            # Gets relative position and width of the next_question_btn
            next_questions_info = self.next_btn.place_info()
            x_relpos = float(next_questions_info["relx"])

            if x_relpos >= 0.35:  # Moves the button to the left
                x_relpos -= 0.01
                self.next_btn.place_configure(relx=x_relpos)
                self.after(20, transition)

            else:
                self.results_btn = ctk.CTkButton(
                    self,
                    text="Results",
                    font=("Helvetica", 20, "bold"),
                    text_color=("black", "white"),
                    corner_radius=10,
                    border_width=3,
                    border_color="black",
                    command=show_results
                )
                self.results_btn.place(relx=0.65, rely=0.835, anchor="center", relwidth=0.2, relheight=0.1)

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
        letters: tuple[str, str, str, str] = ("A", "B", "C", "D")
        quiz_started(True)

        for widget in self.winfo_children():
            widget.place_forget()

        try:
            self.Questions_display = ctk.CTkTextbox(
                self,
                font=("Helvetica", 24, "bold"),
                fg_color=("#ebebeb", "#808080"),
                text_color=("black", "white"),
                wrap="word"
            )
            self.Questions_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")
            self.Questions_display.configure(state="disabled")
            self.Questions_display.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.5, relheight=0.2)

            users_guess = ctk.StringVar(value="")
            self.first_radio_btn = ctk.CTkRadioButton(
                self,
                text=f"{letters[0]}. {Users_Choices[question_num][0]}",
                variable=users_guess,
                value=letters[0]
            )
            self.first_radio_btn.place(relx=0.35, rely=0.45, anchor="center")

            self.second_radio_btn = ctk.CTkRadioButton(
                self,
                text=f"{letters[1]}. {Users_Choices[question_num][1]}",
                variable=users_guess,
                value=letters[1]
            )
            self.second_radio_btn.place(relx=0.35, rely=0.65, anchor="center")

            self.third_radio_btn = ctk.CTkRadioButton(
                self,
                text=f"{letters[2]}. {Users_Choices[question_num][2]}",
                variable=users_guess,
                value=letters[2]
            )
            self.third_radio_btn.place(relx=0.675, rely=0.45, anchor="center")

            self.fourth_radio_btn = ctk.CTkRadioButton(
                self,
                text=f"{letters[3]}. {Users_Choices[question_num][3]}",
                variable=users_guess,
                value=letters[3]
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
                command=next_question
            )
            self.next_btn.place(relx=0.485, rely=0.835, anchor="center", relwidth=0.2, relheight=0.1)

            self.status_label = ctk.CTkLabel(
                 self,
                 image=None,
                 text="",
                 font=("Helvetica", 20, "bold")
            )
            self.status_label.place(relx=0.485, rely=0.735, anchor="center")

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

        def show_summary():
            summary_page.animate()
            if summary_page.in_start_position:
                self.hide_btn.place(
                    relx=0.5, rely=0.85, anchor="center", relwidth=0.2, relheight=0.1
                )
                self.acronym_guide.place(
                    relx=0.75, rely=0.85, anchor="center", relwidth=0.25, relheight=0.15
                )
            else:
                self.hide_btn.place_forget()
                self.acronym_guide.place_forget()

        # Frame configuration
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)
        self.configure(fg_color=("#ebebeb", "#808080"))

        # Instance of Summary()
        summary_page = Summary(parent=self.master, start_position=1.5, end_position=0.4)

        # WIDGETS
        self.score_label = ctk.CTkLabel(
            self,
            text=f"{score}/{len(Users_Questions)}",
            font=("Helvetica", 50, "bold"),
            text_color="black",
        )
        self.score_label.place(relx=0.5, rely=0.3, anchor="center")

        self.percentage_label = ctk.CTkLabel(
            self,
            text=f"{score / len(Users_Questions) * 100:.2f}%",
            font=("Helvetica", 65, "bold"),
            text_color="black",
        )
        self.percentage_label.place(relx=0.5, rely=0.5, anchor="center")

        # Buttons
        self.retake_btn = ctk.CTkButton(
            self,
            text="RETAKE",
            font=("Helvetica", 25, "bold"),
            text_color=("black", "white"),
            border_width=3,
            corner_radius=10,
            border_color="black",
            border_spacing=10,
            command=self.retake,
        )

        self.summary_btn = ctk.CTkButton(
            self,
            text="SUMMARY",
            font=("Helvetica", 25, "bold"),
            text_color=("black", "white"),
            border_width=3,
            corner_radius=10,
            border_color="black",
            border_spacing=10,
            command=show_summary,
        )

        self.new_quiz_btn = ctk.CTkButton(
            self,
            text="NEW QUIZ",
            font=("Helvetica", 25, "bold"),
            text_color=("black", "white"),
            border_width=3,
            corner_radius=10,
            border_color="black",
            border_spacing=10,
            command=self.new_quiz,
        )

        self.retake_btn.place(relx=0.263, rely=0.7, anchor="center", relwidth=0.2, relheight=0.13)
        self.summary_btn.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.23, relheight=0.13)
        self.new_quiz_btn.place(relx=0.75, rely=0.7, anchor="center", relwidth=0.23, relheight=0.13)

        # Hide summary button
        self.hide_btn = ctk.CTkButton(
            self,
            text="HIDE",
            font=("Helvetica", 23, "bold"),
            corner_radius=10,
            border_color="black",
            border_spacing=10,
            border_width=3,
            text_color=("black", "white"),
            command=show_summary,
        )

        self.acronym_guide = ctk.CTkLabel(
            self,
            text="G: Guess\nCA: Correct Answer",
            font=("Helvetica", 16, "bold"),
            text_color=("black", "white"),
        )

    def retake(self):
        global score
        score = 0

        Users_Guess.clear()
        Start_Quiz(parent=self.master)

    def new_quiz(self):
        global score
        score = 0
        quiz_started(False)

        self.place_forget()  # removes everything then after_msg will be placed

        Users_Questions.clear()
        Users_Answers.clear()
        Users_Choices.clear()
        Users_Guess.clear()

        self.after_msg = ctk.CTkLabel(self.master,
                                      text="Go to Make Questions\nto enter your new questions.",
                                      font=("Helvetica", 35, "bold"),
                                      text_color=("black", "white"), )
        self.after_msg.place(relx=0.5, rely=0.5, anchor="center")


class Summary(ctk.CTkFrame):
    def __init__(self, parent, start_position: float, end_position: float):
        super().__init__(master=parent)

        # Attributes
        self.start_position: float = start_position
        self.end_position: float = end_position

        # Frame configuration
        self.configure(fg_color=("#e1e1e1", "#eeeeee"))
        self.place(relx=0.5, rely=start_position, anchor="center", relwidth=0.8, relheight=0.7)

        # Animation attributes
        self.position = start_position
        self.in_start_position: bool = True

        # WIDGETS
        self.quiz_summary_box = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15, "bold"),
            text_color=("black", "white"),
            border_width=3,
            border_color="black",
            border_spacing=5,
            wrap="word"
        )
        self.quiz_summary_box.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.85)

    def animate(self):
        def animate_up():
            if self.position > self.end_position:
                self.position -= 0.05
                self.place_configure(rely=self.position)
                self.after(15, animate_up)

            else:
                self.display_summary()
                self.in_start_position = False

        def animate_down():
            if self.position < self.start_position:
                self.position += 0.05
                self.place_configure(rely=self.position)
                self.after(15, animate_down)

            else:
                self.quiz_summary_box.delete(1.0, "end")
                self.in_start_position = True

        if self.in_start_position:
            animate_up()
        else:
            animate_down()

    def display_summary(self):
        letters: tuple[str, str, str, str] = ("A", "B", "C", "D")

        for question_number, question in enumerate(Users_Questions):
            self.quiz_summary_box.configure(state="normal")

            self.quiz_summary_box.insert("end", f"{question_number + 1}. {question}\n")

            for letters_index, letter in enumerate(letters):
                self.quiz_summary_box.insert("end", f"{letter}. {Users_Choices[question_number][letters_index]}\n")

            self.quiz_summary_box.insert("end", f"G --> {Users_Guess[question_number]}\n")
            self.quiz_summary_box.insert("end", f"CA --> {Users_Answers[question_number]}\n")

            self.quiz_summary_box.insert("end", f"―" * 20 + "\n")
            self.quiz_summary_box.configure(state="disabled")
