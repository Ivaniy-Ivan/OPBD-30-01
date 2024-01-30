import tkinter as tk
from tkinter import messagebox
import customtkinter

class LoginApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login App")
        self.geometry("300x150")

        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.pack(padx=20, pady=20)

        self.username_label = customtkinter.CTkLabel(self.login_frame, text="Username:")
        self.username_label.pack()

        self.username_entry = customtkinter.CTkEntry(self.login_frame)
        self.username_entry.pack(pady=10)

        self.password_label = customtkinter.CTkLabel(self.login_frame, text="Password:")
        self.password_label.pack()

        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.withdraw()  # Hide the login window
            self.main_window = MainApp(self)  # Create the main window
        else:
            messagebox.showerror("Error", "Invalid username or password")

class MainApp(customtkinter.CTk):
    def __init__(self, login_app):
        super().__init__()

        self.login_app = login_app
        self.title("Main App")
        self.geometry("600x400")


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()