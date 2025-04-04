import customtkinter as ctk
from PIL import Image
from extras import Make_Questions, Start_Quiz
import extras


def change_theme():
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


def what_user_chose(event):
    users_choice = Make_Start_buttons.get()

    if users_choice == "Make\nQuestions":
        for widget in main_frame.winfo_children():  # Destroys any widget inside main_frame
            widget.destroy()

        greeting_message.destroy()
        Make_Questions(main_frame)

    else:
        for widget in main_frame.winfo_children():
            widget.destroy()

        greeting_message.destroy()
        Start_Quiz(main_frame)


def disable_enable():
    if extras.get_start_button_pressed():
        Make_Start_buttons.configure(state="disabled")
    else:
        Make_Start_buttons.configure(state="normal")


root = ctk.CTk()
root.geometry("750x500")

change_theme_icon = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/light_to_dark.png"),
    dark_image=Image.open("./icons_and_images/dark_to_light.png"),
)

down_arrow = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/black_down_arrow.png"),
    dark_image=Image.open("./icons_and_images/white_down_arrow.png"),
)

up_arrow = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/black_to_white_up_arrow.png"),
    dark_image=Image.open("./icons_and_images/white_to_black_up_arrow.png"),
)

# WIDGETS
change_theme_button = ctk.CTkButton(
    root,
    image=change_theme_icon,
    text="Change\nTheme",
    compound="left",
    text_color=("black", "white"),
    command=change_theme,
    corner_radius=10,
    border_width=2,
    border_color="black",
)
change_theme_button.place(relx=0.085, rely=0.95, relwidth=0.15, anchor="center")

greeting_message = ctk.CTkLabel(
    root,
    text="Welcome to my program😁\nFeel free to explore.\n Hope you enjoy it!",
    font=("Arial", 50, "bold"),
)
greeting_message.place(relx=0.5, rely=0.5, anchor="center")


class DropdownAnimation(ctk.CTkFrame):
    def __init__(self, parent, start_position, end_position):
        super().__init__(master=parent)
        global dropdown_button

        # GENERAL ATTRIBUTES
        self.start_pos = start_position
        self.end_pos = end_position

        # animation logic
        self.position = start_position
        self.in_start_position = True  # to know if there is a change of position

        # layout of the frame
        self.configure(fg_color="transparent")
        self.place(relx=0.5, rely=start_position, anchor="center", relwidth=0.32, relheight=0.25)

    def animate(self, event):  # allows the frame to move up or down when dropdown_button is pressed
        if self.in_start_position:
            self.animate_down()
        else:
            self.animate_up()

    def animate_down(self):  # frame will go down till its destination
        if self.position < self.end_pos:

            self.position += 0.01
            self.place(
                relx=0.5,
                rely=self.position,
                anchor="center",
                relwidth=0.32,
                relheight=0.25,
            )
            self.after(15, self.animate_down)
            dropdown_button.configure(image=up_arrow)

        else:
            self.in_start_position = False

    def animate_up(self):  # frame will go back to its original position.
        if self.position > self.start_pos:

            self.position -= 0.01
            self.place(
                relx=0.5,
                rely=self.position,
                anchor="center",
                relwidth=0.32,
                relheight=0.25,
            )
            self.after(15, self.animate_up)
            dropdown_button.configure(image=down_arrow)

        else:
            self.in_start_position = True


# FRAMES
dropdown_frame = DropdownAnimation(root, start_position=-0.035, end_position=0.15)  # holds the segmented buttons

main_frame = ctk.CTkFrame(root, fg_color="transparent")  # frame that holds Make_Questions and Start_Quiz
main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.75)
main_frame.lower()

segmented_button_frame = ctk.CTkFrame(
    dropdown_frame,
    height=75,
    fg_color="transparent",
    border_width=2,
    border_color=("black", "gray41"),
    corner_radius=10,
)
segmented_button_frame.place(
    relx=0.5, rely=0.33, relwidth=1, relheight=0.65, anchor="center"
)

Make_Start_buttons = ctk.CTkSegmentedButton(
    segmented_button_frame,
    values=["Make\nQuestions", "Start\nQuiz"],
    dynamic_resizing=False,
    height=50,
    font=("Helvetica", 15, "bold"),
    border_width=5,
    fg_color=("#ebebeb", "#242424"),
    command=what_user_chose,
)
Make_Start_buttons.place(
    relx=0.5, rely=0.5, relwidth=0.88, relheight=0.6, anchor="center"
)
# Sets the width of the buttons in Make_Start_buttons
for button in Make_Start_buttons._buttons_dict.values():  # Accesses the dictionary and we get the buttons.
    button.configure(  # This is why we can configure both buttons. The buttons are from values()
        width=200,
        corner_radius=10,
        text_color=("black", "white"),
        fg_color=("#c0c0c0", "#c0c0c0"),
    )  # Both buttons have equal width

dropdown_button = ctk.CTkButton(
    dropdown_frame,
    image=down_arrow,
    text="",
    fg_color="transparent",
    hover_color=("#cccccc", "#1d1d1d"),
    border_color=("black", "gray41"),
    border_spacing=4,
    corner_radius=0,
    border_width=2,
    command=disable_enable
)
dropdown_button.place(relx=0.5, rely=0.91, relwidth=0.25, relheight=0.27, anchor="s")
dropdown_button.bind("<Button-1>", dropdown_frame.animate)

root.mainloop()
