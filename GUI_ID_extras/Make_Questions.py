import customtkinter as ctk

Users_Questions: list[str] = []
Users_Answers: list[str] = []

class make_questions(ctk.CTkFrame):
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

            if questions == [""] and answers == [""]:
                self.preview.insert(0.0, "")
            elif questions == [""] or answers == [""]:
                self.preview.insert(0.0, "")

            else:
                for question_num, question in enumerate(questions):
                    self.preview.configure(state="normal")  # so that text can show in the preview

                    # the textbox inserts these weirdly. The gist is question, answer, and then lines
                    self.preview.insert(1.0, f"{answers[question_num]}\n")
                    self.preview.insert(2.0, "―" * 20 + "\n")
                    self.preview.insert(0.0, question + "\n")

                self.preview.configure(state="disabled")  # prevents any external changes to the preview

                self.question_textbox.delete(0.0, "end")
                self.answer_textbox.delete(0.0, "end")

        def store_question() -> list[str]:
            questions: list[str] = []
            users_input: str = self.question_textbox.get(0.0, "end")

            users_input: list[str] = reversed(users_input.splitlines())  # removes new line character (\n)

            # remove \t characters
            for string in users_input:
                questions.append(string.replace("\t", ""))
            return questions

        def store_answer() -> list[str]:
            answers: list[str] = []
            users_input: str = self.answer_textbox.get(0.0, "end")

            users_input: list[str] = reversed(users_input.splitlines())  # removes new line character (\n)

            # remove \t characters
            for string in users_input:
                answers.append(string.replace("\t", ""))
            return answers

        # Main Frame
        self.configure(fg_color=("#9b9b9b", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.75)
        self.lower()

        # Widgets

        # Questions widget
        self.question_label = ctk.CTkLabel(
            self, text="Question", font=("Arial", 25), text_color=("black", "white")
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
            self, text="Answer", font=("Arial", 25), text_color=("black", "white")
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
            text_color="black"
        )
        self.preview.place(
            relx=0.77, rely=0.5, anchor="center", relwidth=0.4, relheight=0.9
        )
