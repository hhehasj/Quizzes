import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

# Global Variables
User_Statements: list[str] = []
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


class Make_Statements(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        statement_num: int = 0

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
                nonlocal statement_num
                to_be_displayed_statements, final_statements = revise_statement()

                for index, statement in enumerate(to_be_displayed_statements):
                    self.preview_box.configure(state="normal")

                    self.preview_box.insert("end", f"{statement_num + 1}. {statement}\n")

                    self.preview_box.insert("end", f"{statement_num + 1}. {final_statements[index]}\n")
                    User_Statements.append(final_statements[statement_num])

                    self.preview_box.insert("end", "―" * 15 + "\n")
                    statement_num += 1

                self.preview_box.configure(state="disabled")

                self.statements_textbox.delete(0.0, "end")
                self.chosen_word_textbox.delete(0.0, "end")

        def revise_statement():
            def removing_excess_characters():
                users_statement: str = self.statements_textbox.get(1.0, "end")
                users_chosen_word: str = self.chosen_word_textbox.get(1.0, "end")
                
                users_statement.replace("\t", "")
                users_statement: list[str] = users_statement.splitlines()  # splits statements from \n
                users_chosen_word.replace("\t", "")
                users_chosen_word: list[str] = users_chosen_word.splitlines()

                return users_statement, users_chosen_word

            revised_initial_statement, revised_chosen_word = removing_excess_characters()
            final_statements: list[str] = []
            displayed_statements: list[str] = []

            for index, statement in enumerate(revised_initial_statement):
                if statement.find(revised_chosen_word[index]) != -1:
                    final_statements.append(statement.replace(revised_chosen_word[index], "_" * len(revised_chosen_word[index])))
                    displayed_statements.append(statement)
                    Users_Answers.append(revised_chosen_word[index])

                else:
                    showerror(title="Error", message="The word you want to turn into a blank is not in the statement.")

            if len(final_statements) != len(revised_initial_statement):  # so that a statement will not sneak pass through.
                final_statements.clear()
                displayed_statements.clear()
                Users_Answers.clear()

            else:
                return displayed_statements, final_statements

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
        self.next_btn = ctk.CTkButton(
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
        self.next_btn.place(relx=0.25, rely=0.88, anchor="center")

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
    def __init__(self, parent):
        super().__init__(master=parent)

        # Configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        self.start_btn = ctk.CTkButton(  # shows up the moment you choose Start_Quiz
            self,
            text="Start",
            font=("Helvetica", 30, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            border_color="black",
            border_width=3,
            command=self.start,
        )
        self.start_btn.place(relx=0.5, rely=0.5, anchor="center", relheight=0.15, relwidth=0.25)

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

        def next_statement():
            nonlocal question_num

            try:
                checking()

                self.Statements_display.configure(state="normal")
                self.Statements_display.delete(0.0, "end")

                self.Statements_display.insert(0.0, f"{question_num + 1}. {User_Statements[question_num]}")
                question_num += 1

                self.Statements_display.configure(state="disabled")

            except IndexError:  # When there are no more statemetns to answer
                self.Statements_display.configure(state="normal")
                self.Statements_display.delete(0.0, "end")

                self.Statements_display.insert(0.0, "Test Over")

                self.Statements_display.configure(state="disabled")
                self.next_question_btn.configure(state="disabled")
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
            next_questions_info = self.next_question_btn.place_info()  # returns a dictionary
            x_relpos = float(next_questions_info["relx"])

            if x_relpos >= 0.35:  # moves the button to the left
                x_relpos -= 0.01
                self.next_question_btn.place_configure(relx=x_relpos)
                self.after(20, transition)

            else:
                self.results_btn = ctk.CTkButton(
                    self,
                    text="Results",
                    font=("Helvetica", 20, "bold"),
                    text_color=("black", "white"),
                    corner_radius=10,
                    border_color="black",
                    border_width=3,
                    command=show_results,
                )
                self.results_btn.place(relx=0.65, rely=0.7, anchor="center", relwidth=0.25, relheight=0.1)

        for widget in self.winfo_children():
            widget.place_forget()

        try:
            self.Statements_display = ctk.CTkTextbox(
                self,
                font=("Helvetica", 24, "bold"),
                fg_color=("#ebebeb", "#808080"),
                text_color=("black", "white"),
                wrap="word",
            )
            # Shows the 1st question then the 2nd question shows up through next_question()
            self.Statements_display.insert(0.0, f"{question_num + 1}. {User_Statements[question_num]}")
            question_num += 1

            self.Statements_display.configure(state="disabled")  # disable once the first question is displayed
            self.Statements_display.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.5, relheight=0.2)

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
            self.next_question_btn = ctk.CTkButton(
                self,
                text="Next",
                font=("Helvetica", 20, "bold"),
                text_color=("black", "white"),
                corner_radius=10,
                border_color="black",
                border_width=3,
                command=next_statement,
            )
            self.next_question_btn.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.25, relheight=0.1)

            # IF USER HASN'T ENTERED ANY QUESTIONS IN MAKE QUESTIONS
        except IndexError:
            self.error_label = ctk.CTkLabel(
                self,
                text="You haven't entered any questions.\nPlease go to Make Questions.",
                font=("Helvetica", 35, "bold"),
                text_color=("black", "white"),
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
                    relx=0.75, rely=0.85, anchor="center", relwidth=0.3, relheight=0.2
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
        self.percentage_label = ctk.CTkLabel(
            self,
            text=f"{score / len(User_Statements) * 100:.2f}%",
            font=("Helvetica", 65, "bold"),
            text_color="black",
        )
        self.percentage_label.place(relx=0.5, rely=0.2, anchor="center")

        self.score_label = ctk.CTkLabel(
            self,
            text=f"{score}/{len(User_Statements)}",
            font=("Helvetica", 45, "bold"),
            text_color="black",
        )
        self.score_label.place(relx=0.5, rely=0.4, anchor="center")

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

        self.retake_btn.place(relx=0.263, rely=0.6, anchor="center", relwidth=0.2, relheight=0.1)
        self.summary_btn.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.23, relheight=0.1)
        self.new_quiz_btn.place(relx=0.75, rely=0.6, anchor="center", relwidth=0.23, relheight=0.1)

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

        User_Statements.clear()
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
        for question_num, question in enumerate(User_Statements):
            self.quiz_summary_box.configure(state="normal")

            self.quiz_summary_box.insert("end", f"{question_num + 1}. {question}\n")
            self.quiz_summary_box.insert("end", f"G --> {Users_Guess[question_num]}\n")
            self.quiz_summary_box.insert("end", f"CA --> {Users_Answers[question_num]}\n")

            self.quiz_summary_box.insert("end", "―" * 20 + "\n")
            self.quiz_summary_box.configure(state="disabled")
