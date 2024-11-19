import customtkinter as ctk
from PIL import Image

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

class Make_Statements(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        def stores_and_displays():
            ...

        def store_question() -> list[str]:
            ...

        def store_answer() -> list[str]:
            ...

        # Frame's configuration
        self.configure(fg_color=("#ebebeb", "#808080"))
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # WIDGETS
        # Where you enter your questions
        self.question_textbox_label = ctk.CTkLabel(
            self,
            text="Questions",
            font=("Arial", 25),
            text_color=("black", "white"),
        )
        self.question_textbox_label.place(relx=0.25, rely=0.15, anchor="center")

        self.question_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.question_textbox.place(relx=0.26, rely=0.3, anchor="center", relwidth=0.35, relheight=0.2)

        # Where you enter the answers to the questions
        self.answer_textbox_label = ctk.CTkLabel(
            self,
            text="Answers",
            font=("Arial", 25),
            text_color=("black", "white"),
        )
        self.answer_textbox_label.place(relx=0.25, rely=0.5, anchor="center")

        self.answer_textbox = ctk.CTkTextbox(
            self,
            font=("Helvetica", 15),
            fg_color="white",
            border_color="black",
            border_width=3,
            wrap="word",
            text_color="black"
        )
        self.answer_textbox.place(relx=0.26, rely=0.65, anchor="center", relwidth=0.35, relheight=0.2)

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
            # command=stores_and_displays
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