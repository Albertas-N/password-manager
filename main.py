import customtkinter

# Set the appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def login():
    print("Test")

def setup_gui(root):
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=60, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 34))
    label.pack(pady=12, padx=10)

    username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    username.pack(pady=12, padx=10)

    password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    password.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

if __name__ == "__main__":
    root = customtkinter.CTk()
    root.geometry("800x550")
    setup_gui(root)
    root.mainloop()
