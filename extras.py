import customtkinter as ctk
from PIL import Image

Users_Questions: list[str] = []
Users_Answers: list[str] = []


class Make_Questions(ctk.CTkFrame):
    # global Users_Questions, Users_Answers
    def __init__(self, parent):
        super().__init__(master=parent)

        # Functions
        def stores_and_displays():
            """"
            Displays the output of the functions into the preview frame.
            Then the Question and Answer textboxes will be empty, ready for the next question.
            """""

            questions = store_question()
            answers = store_answer()

            for question_num, question in enumerate(questions):
                self.preview.configure(state="normal")  # so that text can show in the preview

                # the textbox inserts these weirdly. The gist is question, answer, and then lines
                self.preview.insert(1.0, f"{answers[question_num]}\n")
                Users_Answers.append(answers[question_num])
                self.preview.insert(2.0, "―" * 10 + "\n")
                self.preview.insert(0.0, question + "\n")
                Users_Questions.append(question)

            self.preview.configure(state="disabled")  # prevents any external changes to the preview

            self.question_textbox.delete(0.0, "end")
            self.answer_textbox.delete(0.0, "end")

        def store_question() -> list[str]:
            questions: list[str] = []
            users_input: str = self.question_textbox.get(0.0, "end")

            users_input: list[str] = reversed(users_input.splitlines())  # removes new line character (\n)

            # removes \t characters
            for string in users_input:
                if string != "":
                    questions.append(string.replace("\t", ""))
                else:
                    continue
            return questions

        def store_answer() -> list[str]:
            answers: list[str] = []
            users_input: str = self.answer_textbox.get(0.0, "end")

            users_input: list[str] = reversed(users_input.splitlines())  # removes new line character (\n)

            # remove \t characters
            for string in users_input:
                if string != "":
                    answers.append(string.replace("\t", ""))
                else:
                    continue
            return answers

        # Configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS

        # Questions widget
        self.question_label = ctk.CTkLabel(
            self, text="Questions", font=("Arial", 25), text_color=("black", "white")
        )
        self.question_label.place(relx=0.25, rely=0.15, anchor="center")
        self.question_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
        )
        self.question_textbox.place(
            relx=0.26, rely=0.3, anchor="center", relwidth=0.35, relheight=0.2
        )

        # Answers widget
        self.answer_label = ctk.CTkLabel(
            self, text="Answers", font=("Arial", 25), text_color=("black", "white")
        )
        self.answer_label.place(relx=0.25, rely=0.5, anchor="center")
        self.answer_textbox = ctk.CTkTextbox(
            self,
            font=("Helveltica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
        )
        self.answer_textbox.place(
            relx=0.26, rely=0.65, anchor="center", relwidth=0.35, relheight=0.2
        )

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
        self.preview = ctk.CTkTextbox(
            self,
            state="disabled",
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black",
            font=("Helvetica", 15)
        )
        self.preview.place(
            relx=0.77, rely=0.5, anchor="center", relwidth=0.4, relheight=0.9
        )


class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS

        self.start_button = ctk.CTkButton(self,
                                          text="Start",
                                          font=("Helvetica", 30, "bold"),
                                          text_color=("black", "white"),
                                          corner_radius=10,
                                          border_color="black",
                                          border_width=3,)
        self.start_button.place(relx=0.5, rely=0.5, anchor="center",
                                relheight=0.15, relwidth=0.25)
        self.start_button.focus()
        self.start_button.bind("<Return>", self.start)
        self.start_button.bind("<Button-1>", self.start)

    def start(self, event):

        correct_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/check.png"),
            dark_image=Image.open("./icons_and_images/check.png"),
        )

        wrong_icon = ctk.CTkImage(
            light_image=Image.open("./icons_and_images/wrong.png"),
            dark_image=Image.open("./icons_and_images/wrong.png"),)

        # Variables
        question_num: int = 0

        def next_question():
            nonlocal question_num

            """"
            Displays the next questions inside the Users_Questions list
            """""
            if question_num < len(Users_Questions):
                self.questions_label.configure(state="normal")
                self.questions_label.delete(0.0, "end")
                self.questions_label.insert(0.0, f"{question_num + 1}. {Users_Questions[::-1][question_num]}")
                question_num += 1
                self.questions_label.configure(state="disabled")
            else:
                self.questions_label.configure(state="normal")
                self.questions_label.delete(0.0, "end")
                self.questions_label.insert(0.0, "Test Over")
                self.questions_label.configure(state="disabled")

        def checking():
            nonlocal question_num
            users_guess: str = self.guess_box.get(0.0, "end")

            print(question_num)
            if question_num > 0:
                if users_guess.rstrip() == Users_Answers[question_num - 1]:
                    self.guess_box.delete(0.0, "end")
                    self.status_btn = ctk.CTkLabel(self, image=correct_icon, text="", font=("Helvetica", 20, "bold"))
                    self.status_btn.place(relx=0.5, rely=0.7, anchor="center")
                    question_num -= 1
                else:
                    self.guess_box.delete(0.0, "end")
                    self.status_btn.configure(image=wrong_icon)
                    question_num -= 1



        """"
        Displays the questions and shows an answer box.
        """""
        for widget in self.winfo_children():
            widget.place_forget()
        try:
            self.questions_label = ctk.CTkTextbox(self,
                                                  font=("Helvetica", 24, "bold"),
                                                  fg_color=("#ebebeb", "#808080",),
                                                  text_color=("black", "white"),
                                                  wrap="word",
                                                  )
            self.questions_label.insert(0.0, f"{question_num + 1}. {Users_Questions[::-1][question_num]}")
            question_num += 1
            self.questions_label.configure(state="disabled")
            self.questions_label.place(relx=0.5, rely=0.2, anchor="center",
                                       relwidth=0.5, relheight=0.2)
            # GUESS BOX
            self.guess_label = ctk.CTkLabel(self,
                                            text="GUESS: ",
                                            font=("Helvetica", 20, "bold"),
                                            text_color=("black", "white"),
                                            )
            self.guess_label.place(relx=0.32, rely=0.4, anchor="center",)

            self.guess_box = ctk.CTkTextbox(self,
                                            font=("Helvetica", 18, "bold"),
                                            wrap="word",
                                            border_width=3,
                                            border_color="black",
                                            text_color="black",
                                            fg_color="#f9f9fa",
                                            )
            self.guess_box.place(relx=0.57, rely=0.44, anchor="center",
                                 relwidth=0.35, relheight=0.16)


            self.next_question_btn = ctk.CTkButton(self,
                                                   text="Next",
                                                   font=("Helvetica", 20, "bold"),
                                                   text_color=("black", "white"),
                                                   corner_radius=10,
                                                   border_color="black",
                                                   border_width=3,
                                                   command=lambda: [next_question(), checking()],
                                                   )
            self.next_question_btn.place(relx=0.5, rely=0.8, anchor="center",
                                         relwidth=0.25, relheight=0.1)
        except IndexError:
            self.error_label = ctk.CTkLabel(self, text="You haven't entered any questions.\nPlease go to Make Questions.",
                                            font=("Helvetica", 35, "bold"),
                                            text_color=("black", "white"))
            self.error_label.place(relx=0.5, rely=0.5, anchor="center")