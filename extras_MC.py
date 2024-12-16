import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

Users_Questions: list[str] = []
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


class Start_Quiz(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Results(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)


class Summary(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)