import customtkinter as ctk
from PIL import Image
from extras import Make_Questions, Start_Quiz
import extras


def change_theme():
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


def segmented_button_callback(event):
    users_choice = make_start_buttons.get()

    if users_choice == "Make\nQuestions":
        for widget in main_frame.winfo_children():
            widget.destroy()
        instructions.destroy()
        Make_Questions(main_frame)
    else:
        for widget in main_frame.winfo_children():
            widget.destroy()
        instructions.destroy()
        Start_Quiz(main_frame)


def disable_enable():
    if extras.get_pressed():
        make_start_buttons.configure(state="disabled")
    else:
        make_start_buttons.configure(state="normal")


root = ctk.CTk()
root.geometry("750x500")

change_theme_icon = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/light_to_dark.png"),
    dark_image=Image.open("./icons_and_images/dark_to_light.png"),
)

down_arrows = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/black_down_arrow.png"),
    dark_image=Image.open("./icons_and_images/white_down_arrow.png"),
)

up_arrows = ctk.CTkImage(
    light_image=Image.open("./icons_and_images/black_to_white_up_arrow.png"),
    dark_image=Image.open("./icons_and_images/white_to_black_up_arrow.png"),
)

change_theme_btn = ctk.CTkButton(
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
change_theme_btn.place(relx=0.085, rely=0.95, relwidth=0.15, anchor="center")

instructions = ctk.CTkLabel(
    root,
    text="Welcome to my program😁\nFeel free to explore.\n Hope you enjoy it!",
    font=("Arial", 50, "bold"),
)
instructions.place(relx=0.5, rely=0.5, anchor="center")


class DropdownAnimation(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)
        global dropdown_button

        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos

        # animation logic
        self.position = start_pos
        self.in_start_pos = True

        # layout
        self.configure(
            fg_color="transparent",
        )
        self.place(
            relx=0.5, rely=start_pos, anchor="center", relwidth=0.32, relheight=0.25
        )

    def animate(self, event):
        if self.in_start_pos:
            self.animate_down()
        else:
            self.animate_up()

    def animate_down(self):
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
            dropdown_button.configure(image=up_arrows)
        else:
            self.in_start_pos = False

    def animate_up(self):
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
            dropdown_button.configure(image=down_arrows)
        else:
            self.in_start_pos = True


dropdown_frame = DropdownAnimation(root, start_pos=-0.035, end_pos=0.15)
main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.75)
main_frame.lower()

segmented_btn_frame = ctk.CTkFrame(
    dropdown_frame,
    height=75,
    fg_color="transparent",
    border_width=2,
    border_color=("black", "gray41"),
    corner_radius=10,
)
segmented_btn_frame.place(
    relx=0.5, rely=0.33, relwidth=1, relheight=0.65, anchor="center"
)

make_start_buttons = ctk.CTkSegmentedButton(
    segmented_btn_frame,
    values=["Make\nQuestions", "Start\nQuiz"],
    dynamic_resizing=False,
    height=50,
    font=("Helvetica", 15, "bold"),
    border_width=5,
    fg_color=("#ebebeb", "#242424"),
    command=segmented_button_callback,
)
make_start_buttons.place(
    relx=0.5, rely=0.5, relwidth=0.88, relheight=0.6, anchor="center"
)
# Sets the width of the buttons in make_start_buttons
for button in make_start_buttons._buttons_dict.values():
    button.configure(
        width=200,
        corner_radius=10,
        text_color=("black", "white"),
        fg_color=("#c0c0c0", "#c0c0c0"),
    )  # Both buttons have equal width

dropdown_button = ctk.CTkButton(
    dropdown_frame,
    image=down_arrows,
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
