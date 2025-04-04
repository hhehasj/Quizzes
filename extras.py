import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

# Global Variables
Users_Questions: list[str] = []
Users_Answers: list[str] = []
Users_Guess: list[str] = []
score: int = 0
start_button_pressed: bool = False


# allows me to change the boolean value of start_button_pressed to disable or enable Make_Start_buttons
def quiz_started(value: bool):
    global start_button_pressed
    start_button_pressed = value


def get_start_button_pressed():
    return start_button_pressed


class Make_Questions(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        question_number: int = 0

        # Functions
        def stores_and_displays():
            nonlocal question_number
            users_questions = store_question()
            users_answers = store_answer()

            if self.question_textbox.get(1.0, "end") != "\n" and self.answer_textbox.get(1.0, "end") != "\n":

                for index, question in enumerate(users_questions):

                    self.preview_box.configure(state="normal")  # so that text can show in the preview

                    self.preview_box.insert("end", f"{question_number + 1}. {question}\n")
                    Users_Questions.append(question)

                    self.preview_box.insert("end", f"{users_answers[index]}\n")
                    Users_Answers.append(users_answers[index])

                    self.preview_box.insert("end", "―" * 15 + "\n")
                    question_number += 1

                self.preview_box.configure(state="disabled")  # prevents any external changes to the preview

                self.question_textbox.delete(0.0, "end")
                self.answer_textbox.delete(0.0, "end")

            else:
                showerror(title="EMPTY FIELDS", message="Fill in all fields.")

        def store_question() -> list[str]:
            questions: list[str] = []
            users_input: str = self.question_textbox.get("1.0", "end")

            users_input: list[str] = users_input.splitlines()  # removes new line character (\n)

            # removes \t characters
            for string in users_input:
                if string != "":
                    questions.append(string.replace("\t", ""))
                else:
                    continue
            return questions

        def store_answer() -> list[str]:
            answers: list[str] = []
            users_input: str = self.answer_textbox.get("1.0", "end")

            users_input: list[str] = users_input.splitlines()  # removes new line character (\n)

            # remove \t characters
            for string in users_input:
                if string != "":
                    answers.append(string.replace("\t", ""))
                else:
                    continue
            return answers

        # Frame's configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS

        # Where you can enter your questions
        self.question_textbox_label = ctk.CTkLabel(
            self,
            text="Questions",
            font=("Arial", 25),
            text_color=("black", "white"))
        self.question_textbox_label.place(relx=0.25, rely=0.15, anchor="center")

        self.question_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
        )
        self.question_textbox.place(relx=0.26, rely=0.3, anchor="center", relwidth=0.35, relheight=0.2)

        # Where you can enter your answers for the questions
        self.answer_textbox_label = ctk.CTkLabel(
            self,
            text="Answers",
            font=("Arial", 25),
            text_color=("black", "white")
        )
        self.answer_textbox_label.place(relx=0.25, rely=0.5, anchor="center")

        self.answer_textbox = ctk.CTkTextbox(
            self,
            font=("Helveltica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
        )
        self.answer_textbox.place(relx=0.26, rely=0.65, anchor="center", relwidth=0.35, relheight=0.2)

        # to stores the question and answer
        self.next_button = ctk.CTkButton(
            self,
            text="Next",
            font=("Helvetica", 20, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            border_color="black",
            border_width=3,
            border_spacing=10,
            command=stores_and_displays,
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
            font=("Helvetica", 15),
        )
        self.preview_box.place(relx=0.77, rely=0.5, anchor="center", relwidth=0.4, relheight=0.9)


class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        self.start_button = ctk.CTkButton(  # shows up the moment you choose Start_Quiz
            self,
            text="Start",
            font=("Helvetica", 30, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            border_color="black",
            border_width=3,
            command=self.start,
        )
        self.start_button.place(relx=0.5, rely=0.5, anchor="center", relheight=0.15, relwidth=0.25)

    def start(self):
        # Images
        correct_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/check.png"),
            dark_image=Image.open("./icons_and_images/check.png"),
        )

        wrong_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/wrong.png"),
            dark_image=Image.open("./icons_and_images/wrong.png"),
        )

        # Variables
        question_num: int = 0
        quiz_started(True)

        def next_question():
            nonlocal question_num

            # moves to the next question
            try:
                checking()   # checks if the user's guess is correct

                self.Questions_display.configure(state="normal")  # allows to change the text
                self.Questions_display.delete(0.0, "end")

                self.Questions_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")
                question_num += 1

                self.Questions_display.configure(state="disabled")  # prevents any external changes to the preview

            except IndexError:  # when the index is out of range. In other words, there are no more questions to display.
                self.Questions_display.configure(state="normal")
                self.Questions_display.delete(0.0, "end")

                self.Questions_display.insert(0.0, "Test Over")

                self.Questions_display.configure(state="disabled")
                self.next_question_button.configure(state="disabled")
                self.guess_box.configure(state="disabled")
                transition()

        def checking():
            nonlocal question_num
            global score

            guess: str = self.guess_box.get(0.0, "end").rstrip()  # removes the \n character
            Users_Guess.append(guess)

            if guess != "" and guess == Users_Answers[question_num - 1]:

                self.guess_box.delete(0.0, "end")
                self.status_label.configure(image=correct_icon)
                score += 1

            elif guess != "" and guess != Users_Answers[question_num - 1]:

                self.guess_box.delete(0.0, "end")
                self.status_label.configure(image=wrong_icon)

            else:
                self.guess_box.insert(0.0, "You didn't type your answer.")
                question_num -= 1  # The question will not be skipped

        def show_results():
            for Start_Quiz_widgets in self.winfo_children():
                Start_Quiz_widgets.place_forget()

            Results(parent=self.master)

        def transition():
            # Gets relative position and width of the next_question_button
            next_questions_info = self.next_question_button.place_info()  # returns a dictionary
            x_relpos = float(next_questions_info["relx"])

            if x_relpos >= 0.35:  # moves the button to the left
                x_relpos -= 0.01
                self.next_question_button.place_configure(relx=x_relpos)
                self.after(20, transition)

            else:
                self.results_button = ctk.CTkButton(
                    self,
                    text="Results",
                    font=("Helvetica", 20, "bold"),
                    text_color=("black", "white"),
                    corner_radius=10,
                    border_color="black",
                    border_width=3,
                    command=show_results,
                )
                self.results_button.place(relx=0.65, rely=0.7, anchor="center", relwidth=0.25, relheight=0.1)

        for widget in self.winfo_children():
            widget.place_forget()

        try:
            self.Questions_display = ctk.CTkTextbox(
                self,
                font=("Helvetica", 24, "bold"),
                fg_color=("#ebebeb", "#808080"),
                text_color=("black", "white"),
                wrap="word",
            )
            # Shows the 1st question then the 2nd question shows up through next_question()
            self.Questions_display.insert(0.0, f"{question_num + 1}. {Users_Questions[question_num]}")
            question_num += 1

            self.Questions_display.configure(state="disabled")  # disable once the first question is displayed
            self.Questions_display.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.5, relheight=0.2)

            # GUESS BOX
            self.guess_box_label = ctk.CTkLabel(
                self,
                text="GUESS: ",
                font=("Helvetica", 20, "bold"),
                text_color=("black", "white"),
            )
            self.guess_box_label.place(relx=0.32, rely=0.4, anchor="center")

            self.guess_box = ctk.CTkTextbox(
                self,
                font=("Helvetica", 18, "bold"),
                wrap="word",
                border_width=3,
                border_color="black",
                text_color="black",
                fg_color="#f9f9fa",
            )
            self.guess_box.place(relx=0.57, rely=0.44, anchor="center", relwidth=0.35, relheight=0.16)

            # STATUS BOX
            self.status_label = ctk.CTkLabel(
                self,
                image=None,
                text="",
                font=("Helvetica", 20, "bold")
            )
            self.status_label.place(relx=0.5, rely=0.6, anchor="center")

            # Next button
            self.next_question_button = ctk.CTkButton(
                self,
                text="Next",
                font=("Helvetica", 20, "bold"),
                text_color=("black", "white"),
                corner_radius=10,
                border_color="black",
                border_width=3,
                command=next_question,
            )
            self.next_question_button.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.25, relheight=0.1)

        # IF USER HASN'T ENTERED ANY QUESTIONS IN MAKE QUESTIONS
        except IndexError:
            self.error_label = ctk.CTkLabel(
                self,
                text="You haven't entered any questions.\nPlease go to Make Questions.",
                font=("Helvetica", 35, "bold"),
                text_color=("black", "white"),
            )
            self.error_label.place(relx=0.5, rely=0.5, anchor="center")


class Results(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        def show_summary():
            summary_page.animate()
            if summary_page.in_start_position:
                self.hide_button.place(
                    relx=0.5, rely=0.85, anchor="center", relwidth=0.2, relheight=0.1
                )
                self.acronym_guide.place(
                    relx=0.75, rely=0.85, anchor="center", relwidth=0.3, relheight=0.2
                )
            else:
                self.hide_button.place_forget()
                self.acronym_guide.place_forget()

        # Frame configuration
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)
        self.configure(fg_color=("#ebebeb", "#808080"))

        # Instance of Summary()
        summary_page = Summary(parent=self.master, start_position=1.5, end_position=0.4)

        # WIDGETS
        self.percentage_label = ctk.CTkLabel(
            self,
            text=f"{score / len(Users_Questions) * 100:.2f}%",
            font=("Helvetica", 65, "bold"),
            text_color="black",
        )
        self.percentage_label.place(relx=0.5, rely=0.2, anchor="center")

        self.score_label = ctk.CTkLabel(
            self,
            text=f"{score}/{len(Users_Questions)}",
            font=("Helvetica", 45, "bold"),
            text_color="black",
        )
        self.score_label.place(relx=0.5, rely=0.4, anchor="center")

        # Buttons
        self.retake_button = ctk.CTkButton(
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

        self.summary_button = ctk.CTkButton(
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

        self.new_quiz_button = ctk.CTkButton(
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

        self.retake_button.place(relx=0.263, rely=0.6, anchor="center", relwidth=0.2, relheight=0.1)
        self.summary_button.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.23, relheight=0.1)
        self.new_quiz_button.place(relx=0.75, rely=0.6, anchor="center", relwidth=0.23, relheight=0.1)

        # Hide summary button
        self.hide_button = ctk.CTkButton(
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
        Users_Guess.clear()

        self.after_msg = ctk.CTkLabel(self.master,
                                      text="Go to Make Questions\nto enter your new questions.",
                                      font=("Helvetica", 35, "bold"),
                                      text_color=("black", "white"),)
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
            wrap="word",
        )
        self.quiz_summary_box.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.85)

    # Animation Logic
    def animate(self):
        def animate_up():
            if self.position > self.end_position:
                self.position -= 0.1
                self.place_configure(rely=self.position)
                self.after(20, animate_up)

            else:
                self.display_summary()
                self.in_start_position = False

        def animate_down():
            if self.position < self.start_position:
                self.position += 0.1
                self.place_configure(rely=self.position)
                self.after(20, animate_down)

            else:
                self.quiz_summary_box.delete("1.0", "end")
                self.in_start_position = True

        if self.in_start_position:
            animate_up()
        else:
            animate_down()

    def display_summary(self):
        for question_num, question in enumerate(Users_Questions):
            self.quiz_summary_box.configure(state="normal")
            self.quiz_summary_box.delete(0.0, "end")

            self.quiz_summary_box.insert("end", f"{question_num + 1}. {question}\n")
            self.quiz_summary_box.insert("end", f"G --> {Users_Guess[question_num]}\n")
            self.quiz_summary_box.insert("end", f"CA --> {Users_Answers[question_num]}\n")

            self.quiz_summary_box.insert("end", "―" * 20 + "\n")
            self.quiz_summary_box.configure(state="disabled")
