"""Author: Alliya Buchanan, Date: 03/06/24 - 09/09/24, Purpose: To 
improve financial stability among NZ tertiary students aged 18-25.
"""

# Import several modules for the code to run.
"""Allows the tkinter libary to be imported."""
import tkinter as tk
"""Allows the current date to be imported."""
from datetime import date
"""Allows the current time to be imported."""
from datetime import datetime
"""Import basic objects from tkinter."""
from tkinter import (BOTTOM, END, LEFT, NONE, RIGHT, Button, Canvas, Label,
                     Scrollbar, StringVar, Text, Toplevel, Y, font, messagebox,
                     ttk)

"""Manipulates elements of a figure."""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
"""Creates a basic foundation for plotting data."""
from matplotlib.figure import Figure

"""Creates and modifies images."""
from PIL import ImageTk
"""Provides the python intepreter with image editing capabilities."""
from PIL import Image


def open_first_window():
    """Function to open the first window."""
    def popup():
        """Function to ensure the user wants to exit the 
        first_window.
        """
        response = messagebox.askquestion("Exit Programme?","Your progress "
                                          + "will NOT be saved.\nAre you sure "
                                          + "you want to exit the program?",
        icon='warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(first_window,
                                 command = first_window.quit)
            confirm_btn.pack()
            first_window.destroy()

    # Create Log in/sign up window.
    global first_window
    first_window = tk.Tk()
    first_window.geometry("1200x750")
    first_window.title("Log in/Sign up")
    first_window.resizable(False, False)

    # Display label.
    program_title = tk.Label(first_window,
        text = "Tertiary Budget \nTracker             ",
        font = ("Helvetica", 48))
    program_title.place(x = 200, y = 250)

    # Create a coloured box for the top where navigation bar will be.
    canvas = Canvas(first_window,
                    height = 100,
                    width = 1210,
                    bg = "CadetBlue2")

    # Create Sign up, log in, and exit buttons.
    open_signup_btn = tk.Button(first_window,
                                text = "Sign up",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "darkgrey",
                                command = open_signup_window)
    login_btn = tk.Button(first_window,
                          text = "Log in",
                          width = 10,
                          height = 2,
                          fg = "black",
                          bg = "darkgrey",
                          command = open_login_window)
    exit_btn = tk.Button(first_window,
                         text = "exit",
                         width = 10,
                         height = 2,
                         fg = "black",
                         bg = "grey",
                         command = popup)

    # Create a label informing the user about what the program does.
    info_lbl_one = Label(first_window, text = "Enjoy a budget plan tailored " +
                    "\nto your financial wants and needs.\n\nBenefit from " +
                    "helpful tips to\nmanage your money.",
                    font = ("Helvetica", 14))
    info_lbl_two = Label(first_window, text = "Aims to improve financial " +
                        "stability among New Zealand tertiary students " +
                        "aged 18-25.", font = ("Helvetica", 10))
    info_lbl_one.place(x = 800, y = 280)
    info_lbl_two.place(x = 200, y = 400)

    # Add image to the first window.
    image = Image.open("budget_image.png")
    # Resize the image using resize() method.
    resize_image = image.resize((1200, 250))
    img = ImageTk.PhotoImage(resize_image)
    # Create label and add resize image.
    label1 = Label(image = img)
    label1.image = img

    # Place labels, buttons, and images in a position.
    canvas.place(x = 0, y = 20)
    login_btn.place(x = 900, y = 40)
    open_signup_btn.place(x = 990, y = 40)
    exit_btn.place(x = 1110, y = 40)
    label1.place(x = 0, y = 450)

    first_window.mainloop()


def open_signup_window():
    """Funtion to open signup window when button is clicked."""
    def signup():
        """Direct user to building profile page after signing in."""
        def popup():
            """Function to ensure the user wants to exit the
            bp_window.
            """
            response = messagebox.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(bp_window,
                                     command = bp_window.quit)
                confirm_btn.pack()
                bp_window.destroy()

        def tertiary_message():
            """Function to output message when tertiary button is 
            clicked.
            """
            tertiary_status = tertiary_status_var.get()
            if tertiary_status == "1":
                messagebox.showinfo("Note", "Please enjoy this applications "
                                    + "features and resources which are "
                                    + "tailored specifically for tertiary "
                                    + "students like yourself.")
            elif tertiary_status == "2":
                messagebox.showinfo("Note", "Please note that this "
                                    + "application is primarily designed for "
                                    + "tertiary students, and may not meet "
                                    + "your individual needs.")
            else:
                messagebox.showerror("Invalid input", "There are missing "
                                     + "fields.\nPlease select a tertiary "
                                     + "status.")

        def knowledge_message():
            """Function to output message when knowledge button is 
            clicked.
            """
            knowledge = knowledge_var.get()
            if knowledge == "1":
                messagebox.showinfo("Introduction", "A budget is a "
                                    "generated spending plan based off your "
                                    "financial wants and needs. It includes "
                                    "prioritizing and allocating various "
                                    "incomes, ensuring that all expenses "
                                    "are covered without spending more "
                                    "than what is earned. Through this "
                                    "application, budgeting can provide "
                                    "clarity, preparedness and insights "
                                    "around finances, savings goals, and "
                                    "expensive emergencies. Ultimately, "
                                    "budgeting improves financial stability.")
            elif knowledge == "2":
                messagebox.showinfo("Aknowledgement", "Great start to "
                                    "improving your financial "
                                    "stability. \nKeep progressing!")
            elif knowledge == "3":
                messagebox.showinfo("Aknowledgement", "Great progression in "
                                    "your journey to financial stability."
                                    "\nKeep up the great work!")
            else:
                messagebox.showerror("Invalid input", "There are missing "
                                     "fields.\nPlease select a tertiary "
                                     "status.")

        def building_profile_next():
            """Function to validate the user input on building profile 
            page and redirect to homepage.
            """
            birthdate = birthdate_var.get()
            knowledge = knowledge_var.get()
            tertiary_status = tertiary_status_var.get()
            try:
                # Convert the string to a datetime object.
                birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
                # Get todays date.
                today = date.today()
                # Find the difference between today and the date of birth.
                difference = today.year - birthdate.year
                # Find out if today preceeds the date of birth this year.
                today_precedes_dob = (today.month, today.day) < \
                    (birthdate.month, birthdate.day)
                age = difference - today_precedes_dob
            except ValueError:
                # Show an error if the date format is incorrect.
                messagebox.showerror("Invalid input", "Please enter a valid "
                                     "birthdate (dd/mm/yyyy)")
            if age <= 0 or age > 99:
                messagebox.showerror("Invalid input", "Please enter a valid "
                                     "birthdate (dd/mm/yyyy)")
                return False
            elif tertiary_status == "":
                messagebox.showerror("Invalid input", "Please select your "
                                     "current tertiary status.")
                return False
            elif knowledge == "":
                messagebox.showerror("Invalid input", "Please select your "
                                     "level of knowledge.")
                return False
            elif age < 18 or age > 25:
                age_maybe = messagebox.askquestion("Note", "Please note that "
                                                   "this application is "
                                                   "primarily designed for "
                                                   "ages 18-25, and may not "
                                                   "meet your individual "
                                                   "needs.\n\nAre you sure "
                                                   "you want to continue?")
                if age_maybe == "no":
                    return False
            else:
                messagebox.showinfo("Note", "Please enjoy this applications "
                                    "features and resources which are "
                                    "tailored specifically for ages 18-25 "
                                    "like yourself.")
            if tertiary_status == "1":
                tertiary_status_words = "Current student"
            if tertiary_status == "2":
                tertiary_status_words = "Other"
            if knowledge == "1":
                knowledge_words = "Very poor"
            if knowledge == "2":
                knowledge_words = "Average"
            if knowledge == "3":
                knowledge_words = "Excellent"
            with open("existing_users.txt", "a") as file:
                file.write(f"Birthdate: {birthdate} Tertiary status: "
                           f"{tertiary_status_words} Knowledge of budgeting:"
                           f" {knowledge_words}\n\n")
            print(f"Birthdate: {birthdate}")
            print(f"Tertiary status: {tertiary_status_words}")
            print(f"Knowledge of budgeting: {knowledge_words}")
            exit_signup_window()

        first_name = first_name_var.get()
        last_name = last_name_var.get()
        username = username_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        # Validate the user input if all fields are entered.
        if first_name and last_name and username and password and \
            confirm_password:
            try:
                with open("existing_users.txt", "r") as file:
                    usernames = file.read().splitlines()
            except FileNotFoundError:
                usernames = []
            if not username.isalpha() and not username.isnumeric():
                messagebox.showerror("Invalid username", "Please only " +
                                     "enter numbers or letters for username.")
            elif username in usernames:
                messagebox.showerror("Invalid username", "This username " +
                                     "already exists.\nPlease enter a " +
                                     "different username.")
            elif not first_name.isalpha() or not last_name.isalpha():
                messagebox.showerror("Invalid first name/last " +
                                     "name", "Please only enter letters " +
                                     "for first name and last name.")
            elif password != confirm_password:
                messagebox.showerror("Invalid password", "Please check " +
                                     "that your passwords match.")
            else:
                with open("existing_users.txt", "a") as file:
                    file.write(f"{username}\n")
                    file.write(f"Full name: {first_name} {last_name} " +
                               f"Username: {username} Password: {password}\n")

                # Add this user to the recent users file.
                with open("recent_users.txt", "a") as file:
                    file.write(f"{username}\n")
                print("First name: " + first_name)
                print("Last name: " + last_name)
                print("Username: " + username)
                print("Password: " + password)
                print("Confirm password: " + confirm_password)
                first_name_var.set("")
                last_name_var.set("")
                username_var.set("")
                password_var.set("")
                confirm_password_var.set("")
                messagebox.showinfo("Successful", "Sign up successful." +
                                    f"\nWelcome {username}")
                first_window.destroy()

                # Create building profile (bp) page, user will be directed here
                # after signing up.
                global bp_window
                bp_window = tk.Tk()
                bp_window.geometry("300x350")
                bp_window.title("Building profile")
                bp_window.resizable(False, False)

                # Print today's date, neccassary for calculating the users age.
                # Print todays date.
                today = date.today()
                d = today.strftime("%d/%m/%y")
                print(f"Date: {d}")

                # Declaring birthdate, tertiary status, and knowledge as
                # string variables.
                birthdate_var = tk.StringVar()
                tertiary_status_var = StringVar()
                knowledge_var = tk.StringVar()

                # Create window content with labels, canvas, and buttons.
                canvas = Canvas(bp_window,
                                height = 50,
                                width = 350,
                                bg = "CadetBlue2", )
                title_lbl = tk.Label(bp_window,
                                     text = "Building profile:",
                                     font = ("Helvetica", 15),
                                     bg = "CadetBlue2")
                subtitle_lbl = tk.Label(bp_window,
                                       text = "Let's get to know you better!"
                                       "\nPlease enter the following",
                                       font = ("Helvetica", 10))
                exit_btn = tk.Button(bp_window,
                                 text = "Exit",
                                 width = 10,
                                 height = 2,
                                 fg = "black",
                                 bg = "grey",
                                 command = popup)
                next_btn = tk.Button(bp_window,
                                     text = "Next",
                                     width = 7,
                                     height = 1,
                                     fg = "black",
                                     bg = "gold",
                                     command = building_profile_next)
                birthdate_lbl = tk.Label(bp_window,
                                         text = "Birthdate (dd/mm/yyyy):",
                                         font = ("Helvetica", 10, "bold"))
                tertiary_lbl = tk.Label(bp_window,
                                        text = "Tertiary status:",
                                        font = ("Helvetica", 10, "bold"))
                knowledge_lbl = tk.Label(bp_window,
                                        text = "Knowledge of budgeting:",
                                        font = ("Helvetica", 10, "bold"))

                # Entrys.
                birthdate_entry = tk.Entry(bp_window,
                                            textvariable = birthdate_var)

                # Dictionary to create multiple options for tertiary status.
                tertiary_status_dict = {"Current student" : "1",
                                        "Other" : "2"}
                # Use a loop to create multiple radiobuttons for tertiary
                # status.
                x_coord = 20
                for (text, value) in tertiary_status_dict.items():
                    tertiary_status_btn = ttk.Radiobutton(bp_window,
                                                          text = text,
                                                          variable = \
                                                          tertiary_status_var,
                                                          value = value,
                                                          command = \
                                                          tertiary_message)
                    tertiary_status_btn.place(x = x_coord, y = 212.5)
                    x_coord += 112   # Provides distance between buttons.

                # Dictionary to create multiple options for knowledge entry.
                knowledge_dict = {"Very Poor" : "1",
                                  "Average" : "2",
                                  "Excellent" : "3"}

                # Use a loop to create multiple radiobuttons for knowledge.
                x_coord = 20
                for (text, value) in knowledge_dict.items():
                    knowledge_btn = ttk.Radiobutton(bp_window,
                                                    text = text,
                                                    variable = knowledge_var,
                                                    value = value,
                                                    command = \
                                                    knowledge_message)
                    knowledge_btn.place(x = x_coord, y = 270)
                    x_coord += 87

                # Placing the labels and entries.
                canvas.place(x = 0, y = 20)
                title_lbl.place(x = 10, y = 34)
                subtitle_lbl.place(x = 60, y = 80)
                exit_btn.place(x = 200, y = 27)
                next_btn.place(x = 120, y = 315)
                birthdate_lbl.place(x = 20, y = 130)
                birthdate_entry.place(x = 20, y = 155)
                tertiary_lbl.place(x = 20, y = 187.5)
                knowledge_lbl.place(x = 20, y = 245)
                bp_window.mainloop()

        else:
            messagebox.showerror("Invalid input", "There are missing " +
                                 "fields.\nPlease enter all fields.")

    # Create window properties.
    global signup_window
    signup_window = Toplevel(first_window)
    signup_window.title("Sign up")
    signup_window.geometry("300x350")
    signup_window.resizable(False, False)

    # Declaring name and password as string variables.
    first_name_var = tk.StringVar()
    last_name_var = tk.StringVar()
    username_var = tk.StringVar()
    password_var = tk.StringVar()
    confirm_password_var = tk.StringVar()
    # Create window content with labels, canvas, and buttons.
    canvas = Canvas(signup_window,
                    height = 50,
                    width = 350,
                    bg = "CadetBlue2")
    title_lbl = tk.Label(signup_window,
                         text = "Sign up:",
                         font = ("Helvetica", 15),
                         bg = "CadetBlue2")
    subtitle_lbl = tk.Label(signup_window,
                            text = "Create an account",
                            font = ("Helvetica", 15))
    open_login_btn = tk.Button(signup_window,
                               text = "Log in",
                               width = 10,
                               height = 2,
                               fg = "black",
                               bg = "darkgrey",
                               command = open_login_window)
    first_name_lbl = tk.Label(signup_window,
                              text = "First name:",
                              font = ("Helvetica", 10, "bold"))
    last_name_lbl = tk.Label(signup_window,
                             text = "Last name:",
                             font = ("Helvetica", 10, "bold"))
    username_lbl = tk.Label(signup_window,
                            text = "Username:",
                            font = ("Helvetica", 10, "bold"))
    password_lbl = tk.Label(signup_window,
                            text = "Password:",
                            font = ("Helvetica", 10, "bold"))
    confirm_password_lbl = tk.Label(signup_window,
                                    text = "Confirm \nPassword:",
                                    font = ("Helvetica", 10, "bold"))
    signup_btn = tk.Button(signup_window,
                           text = "Sign up",
                           width = 7,
                           height = 1,
                           fg = "black",
                           bg = "gold",
                           command = signup)

    # Entrys.
    first_name_entry = tk.Entry(signup_window,
                                textvariable = first_name_var)
    last_name_entry = tk.Entry(signup_window,
                               textvariable = last_name_var)
    username_entry = tk.Entry(signup_window,
                              textvariable = username_var)
    password_entry=tk.Entry(signup_window,
                            textvariable = password_var,
                            show = "*")
    confirm_password_entry=tk.Entry(signup_window,
                                    textvariable = confirm_password_var,
                                    show = "*")

    # Placing the labels and entries.
    canvas.place(x = 0, y = 20)
    open_login_btn.place(x = 200, y = 27)
    title_lbl.place(x = 10, y = 36)
    subtitle_lbl.place(x = 70, y = 80)

    first_name_lbl.place(x = 20, y = 120)
    first_name_entry.place(x = 100, y = 120)

    last_name_lbl.place(x = 20, y = 160)
    last_name_entry.place(x = 100, y = 160)

    username_lbl.place(x = 20, y = 200)
    username_entry.place(x = 100, y = 200)

    password_lbl.place(x = 20, y = 240)
    password_entry.place(x = 100, y = 240)

    confirm_password_lbl.place(x = 20, y = 280)
    confirm_password_entry.place(x = 100, y = 280)

    signup_btn.place(x = 120, y = 315)
    signup_window.mainloop()


def open_login_window():
    """Function to open log in window when button is clicked."""
    def login():
        """Function to validate user input and check the user exists in
        file.
        """
        username = username_var.get()
        password = password_var.get()

        if username and password:
            try:
                with open("existing_users.txt", "r") as file:
                    lines = file.read().splitlines()
                    # Check if a line has username and password.
                    user_exists = any(f"Username: {username}" in line and \
                                      f"Password: {password}" in line for \
                                        line in lines)
                if user_exists:
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    username_var.set("")
                    password_var.set("")
                    messagebox.showinfo("Successful", "Log in successful." +
                                        f"\nWelcome back {username}")
                    # Write the users username in recent users file.
                    with open("recent_users.txt", "a") as file:
                        file.write(f"{username}\n")
                    exit_login_window()
                elif not user_exists:
                    messagebox.showerror("Unsuccessful", "You have entered " +
                                     "an invalid username or password. " +
                                     "Please try again or sign up.")
            except FileNotFoundError:
                messagebox.showerror("Unsuccessful", "You have entered " +
                                     "an invalid username or password. " +
                                     "Please try again or sign up.")
        else:
            messagebox.showerror("Invalid input", "There are missing " +
                                 "fields.\nPlease enter all fields.")

    # Create window properties.
    global login_window
    login_window = Toplevel(first_window)
    login_window.title("Log in")
    login_window.geometry("300x350")
    login_window.resizable(False, False)

    # Declaring username and password as string variables.
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    # Create window content with labels, canvas, and buttons.
    canvas = Canvas(login_window,
                    height = 50,
                    width = 350,
                    bg = "CadetBlue2")
    title_lbl = tk.Label(login_window,
                         text = "Log in:",
                         font = ("Helvetica", 15),
                         bg = "CadetBlue2")
    subtitle_lbl = tk.Label(login_window,
                         text = "Log in to your account",
                         font = ("Helvetica", 15))
    open_signup_btn = tk.Button(login_window,
                                text = "Sign up",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "darkgrey",
                                command = open_signup_window)

    username_lbl = tk.Label(login_window,
                            text = "Username:",
                            font=("Helvetica", 10, "bold"))
    password_lbl = tk.Label(login_window,
                            text = "Password:",
                            font = ("Helvetica", 10, "bold"))
    login_btn = tk.Button(login_window,
                          text = "Log in",
                          width = 7,
                          height = 1,
                          fg = "black",
                          bg = "gold",
                          command = login)

    # Create entries
    username_entry = tk.Entry(login_window,
                              textvariable = username_var)
    password_entry = tk.Entry(login_window,
                              textvariable = password_var,
                              show = "*")

    # Place the labels and entries.
    canvas.place(x = 0, y = 20)
    open_signup_btn.place(x = 200, y = 27)
    title_lbl.place(x = 10, y = 36)
    subtitle_lbl.place(x = 60, y = 80)
    username_lbl.place(x = 20, y = 160)
    username_entry.place(x = 100, y = 160)
    password_lbl.place(x = 20, y = 200)
    password_entry.place(x = 100, y = 200)
    login_btn.place(x = 120, y = 315)


def signout():
    """Function to sign the user out and redirect them to the first 
    window.
    """
    response = messagebox.askquestion("Signout?","Your progress will "
                                        "NOT be saved.\nAre you sure you want "
                                        "to signout?",
    icon = 'warning')
    print(response)
    if response == "yes":
        home_window.destroy()
        open_first_window()


def exit_login_window():
    """Function to exit the log in window and go to the main code."""
    if 'first_window' in globals():
        first_window.destroy()
    open_main_code()


def exit_signup_window():
    """Function to exit the sign up window and go to the main code."""
    if 'bp_window' in globals():
        bp_window.destroy()
    open_main_code()


def open_main_code():
    """Function where the main code is."""
    def open_help_window():
        """Function to open help window."""
        def exit_help_window():
            """Function to ensure the user wants to exit the 
            help_window.
            """
            response = messagebox.askquestion("Exit Programme?","Your progress"
                                              " will NOT be saved.\nAre you "
                                              "sure you want to exit the "
                                              "program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(help_window,
                                    command = help_window.quit)
                confirm_btn.pack()
                help_window.destroy()

        # Create help page.
        global help_window
        help_window = tk.Tk()
        help_window.geometry("1200x750")
        help_window.title("Help: User Manual")
        help_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        canvas = Canvas(help_window,
                        height = 100,
                        width = 1210,
                        bg = "CadetBlue2")
        home_btn = tk.Button(help_window,
                             text = "Home",
                             width = 10,
                             height = 2,
                             bg = "darkgrey",
                             command = help_to_main)
        open_about_btn = tk.Button(help_window,
                                   text = "About",
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey",
                                   command = help_to_about)
        open_budget_btn = tk.Button(help_window,
                                    text = "My Budget",
                                    width = 10,
                                    height = 2,
                                    fg = "black",
                                    bg = "darkgrey",
                                    command = help_to_income)
        open_tips_btn = tk.Button(help_window,
                                  text = "Tips",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = tips_message)
        open_help_btn = tk.Button(help_window,
                                  text = "Help",
                                  font = underlined_font,
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey")
        profile_btn = tk.Button(help_window,
                                text = "Profile",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "grey",
                                command = open_profile)
        exit_btn = tk.Button(help_window,
                         text = "Exit",
                         width = 10,
                         height = 2,
                         fg = "black",
                         bg = "grey",
                         command = exit_help_window)
        # Create user manual file.
        user_manual_file = open("user_manual.txt","rb")
        user_manual = user_manual_file.read()

        # Create a vertical scrollbar where the user manual is displayed.
        scrollbar = Scrollbar(help_window)
        text_box = Text(help_window,
                        width = 120,
                        height = 37,
                        wrap = NONE,
                        yscrollcommand = scrollbar.set)
        text_box.insert(END, user_manual)
        scrollbar.config(command = text_box.yview)

        # Place labels, buttons, and images in a position.
        canvas.place(x = 0, y = 20)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit_btn.place(x = 1110, y = 40)
        scrollbar.pack(side = RIGHT, fill = Y)
        text_box.pack(side = BOTTOM)

        help_window.mainloop()

    def open_income_window():
        """Function to open my income page."""
        def exit_income_window():
            """Function to ensure the user wants to exit the 
            help_window.
            """
            response = messagebox.askquestion("Exit Programme?","Your progress"
                                              " will NOT be saved.\nAre you "
                                              "sure you want to exit the "
                                              "program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(income_window,
                                    command = income_window.quit)
                confirm_btn.pack()
                income_window.destroy()

        def create_table():
            """Function to create income table."""
            def clear():
                """Function to clear all user input."""
                income_choice.set("Weekly")
                type_1.set("")
                type_2.set("")
                type_3.set("")
                type_4.set("")
                type_5.set("")
                type_6.set("")
                type_7.set("")
                total_income.set("")

            def calculate_total_income():
                """Functiton to calculate total income."""
                try:
                    result = float(type_1.get()) + float(type_2.get()) \
                            + float(type_3.get()) + float(type_4.get()) \
                            + float(type_5.get()) + float(type_6.get()) \
                            + float(type_7.get())
                except ValueError:
                    result = messagebox.showerror("Invalid input", "Please "
                                                  + "enter all fields using "
                                                  + "number 0 and/or "
                                                  + "positive numbers that "
                                                  + "represent your income.")
                total_income.set(f"{result:.2f}")

            def income_next():
                """Function to save the user income, validate their 
                entries, and redirect to expenses page.
                """
                calculate_total_income()
                income_period = income_choice.get()
                income_info = (f"{type_1.get()}\n{type_2.get()}\n"
                               + f"{type_3.get()}\n{type_4.get()}\n"
                               + f"{type_5.get()}\n{type_6.get()}\n"
                               + f"{type_7.get()}\n{total_income.get()}\n\n")
                with open("user_finance_info.txt", "a") as file:
                    file.write(f"Income ({income_period}):\n{income_info}")
                messagebox.showinfo("Save successfull", "Your income has "
                                    "successfully been saved.")
                income_to_expenses()

            income_lbl = tk.Label(income_window,
                            text = "Income type:",
                            font = ("Helevitica", 15, "bold"))

            # income_type_var = tk.StringVar()
            income_choice = ttk.Combobox(income_window,
                                         width = 17,
                                         state = "readonly")
                                        #  textvariable = income_type_var)

            # Adding combobox drop down list
            income_choice["values"] = ("Weekly",
                                       "Fortnightly",
                                       "Four-weekly",
                                       "Monthly",
                                       "Yearly")

            # Shows weekly as a default value
            income_choice.current(0)

            # Create labels for each of the income types and the total income.
            type_1_lbl = tk.Label(income_window,
                                  text = "Ongoing employment:",
                                  font=("Helvetica", 15, "bold"))
            type_2_lbl = tk.Label(income_window,
                                  text = "Study link loan/student allowance:",
                                  font=("Helvetica", 15, "bold"))
            type_3_lbl = tk.Label(income_window,
                                  text = "Holiday/work savings:",
                                  font=("Helvetica", 15, "bold"))
            type_4_lbl = tk.Label(income_window,
                                  text = "Grants/scholarships:",
                                  font=("Helvetica", 15, "bold"))
            type_5_lbl = tk.Label(income_window,
                                  text = "Family:",
                                  font = ("Helvetica", 15, "bold"))
            type_6_lbl = tk.Label(income_window,
                                  text = "One off jobs:",
                                  font = ("Helvetica", 15, "bold"))
            type_7_lbl = tk.Label(income_window,
                                  text = "Other income:",
                                  font = ("Helvetica", 15, "bold"))
            calc_income_btn = tk.Button(income_window,
                                        text = "Calculate total income:",
                                        font = ("Helvetica", 15, "bold"),
                                        bg = "gold",
                                        command = calculate_total_income)
            # Display a dollar sign button for every entry that is evenly
            # spaced.
            y_coord = 353
            for _ in range(1, 8):
                dollar_sign = ttk.Label(income_window,
                                        text = "$",
                                        font = ("Helvetica", 10))
                dollar_sign.place(x = 650, y = y_coord)
                y_coord += 40
            dollar_8_lbl = tk.Label(income_window,
                                    text = "$",
                                    font = ("Helvetica", 10))
            clear_btn = tk.Button(income_window,
                                  text = "Clear all",
                                  width = 10,
                                  height = 2,
                                  bg = "firebrick1",
                                  command = clear)
            next_btn = tk.Button(income_window,
                                 text = "Next",
                                 width = 10,
                                 height = 2,
                                 fg = "black",
                                 bg = "gold",
                                 command = income_next)

            # Declare income type as string variables.
            type_1 = tk.StringVar()
            type_2 = tk.StringVar()
            type_3 = tk.StringVar()
            type_4 = tk.StringVar()
            type_5 = tk.StringVar()
            type_6 = tk.StringVar()
            type_7 = tk.StringVar()
            total_income = tk.StringVar()

            # Create entries for each income type.
            type_1_entry = tk.Entry(income_window,
                                    textvariable = type_1)
            type_2_entry = tk.Entry(income_window,
                                    textvariable = type_2)
            type_3_entry = tk.Entry(income_window,
                                    textvariable = type_3)
            type_4_entry = tk.Entry(income_window,
                                    textvariable = type_4)
            type_5_entry = tk.Entry(income_window,
                                    textvariable = type_5)
            type_6_entry = tk.Entry(income_window,
                                    textvariable = type_6)
            type_7_entry = tk.Entry(income_window,
                                    textvariable = type_7)
            total_income_entry = tk.Entry(income_window,
                                          textvariable = total_income)

            # Place the labels.
            income_lbl.place(x = 300, y = 300)
            income_choice.place(x = 660, y = 305)
            type_1_lbl.place(x = 300, y = 350)
            type_1_entry.place(x = 660, y = 355)
            type_2_lbl.place(x = 300, y = 390)
            type_2_entry.place(x = 660, y = 395)
            type_3_lbl.place(x = 300, y = 430)
            type_3_entry.place(x = 660, y = 435)
            type_4_lbl.place(x = 300, y = 470)
            type_4_entry.place(x = 660, y = 475)
            type_5_lbl.place(x = 300, y = 510)
            type_5_entry.place(x = 660, y = 515)
            type_6_lbl.place(x = 300, y = 550)
            type_6_entry.place(x = 660, y = 555)
            type_7_lbl.place(x = 300, y = 590)
            type_7_entry.place(x = 660, y = 595)
            calc_income_btn.place(x = 295, y = 630)
            total_income_entry.place(x = 660, y = 645)
            dollar_8_lbl.place(x = 650, y = 643)
            clear_btn.place(x = 150, y = 630)
            next_btn.place(x = 1110, y = 700)

        def insights_message():
            """Function to tell the user to enter their income and 
            expenses in order to see insights.
            """
            messagebox.showerror("No input", "Please enter your income "
                                 + "and expenses so that insights can be "
                                 + "made. \nThen click next to continue.")

        def expenses_message():
            """Function to tell the user to enter their income and 
            expenses.
            """
            messagebox.showerror("No input", "Please enter your income "
                                 + "before continuing with expenses. \n"
                                 + "Then click next to continue.")

        # Create my income page.
        global income_window
        income_window = tk.Tk()
        income_window.geometry("1200x750")
        income_window.title("My income")
        income_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(income_window,
                         text = "My income:",
                         font = ("Helvetica", 40))
        description_lbl = tk.Label(income_window,
                                   text = "Please enter your amount to " +
                                          "budget (income) below, you can " +
                                          "choose weekly, fortnightly, " +
                                          "four-weekly, monthly or yearly " +
                                          "amounts.\nThis program will " +
                                          "calculate the total income for " +
                                          "you.",
                                   justify = LEFT)
        canvas = Canvas(income_window,
                        height = 100,
                        width = 1210,
                        bg = "CadetBlue2")
        home_btn = tk.Button(income_window,
                             text = "Home",
                             width = 10,
                             height = 2,
                             bg = "darkgrey",
                             command = income_to_main)
        open_about_btn = tk.Button(income_window,
                                   text = "About",
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey",
                                   command = income_to_about)
        open_budget_btn = tk.Button(income_window,
                                   text = "My Budget",
                                   font = underlined_font,
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey")
        open_tips_btn = tk.Button(income_window,
                                  text = "Tips",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                        command = tips_message)
        open_help_btn = tk.Button(income_window,
                                  text = "Help",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = income_to_help)
        profile_btn = tk.Button(income_window,
                                text = "Profile",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "grey",
                                command = open_profile)
        exit_btn = tk.Button(income_window,
                         text = "Exit",
                         width = 10,
                         height = 2,
                         fg = "black",
                         bg = "grey",
                         command = exit_income_window)
        back_btn = tk.Button(income_window,
                             text = "Back",
                             width = 10,
                             height = 2,
                             fg = "black",
                             bg = "grey",
                             command = income_to_main)
        # Create progress bar on the side.
        side_bar = Canvas(income_window,
                         height = 900,
                         width = 140,
                         bg = "CadetBlue2")
        income_btn = tk.Button(income_window,
                               text = "My Income",
                               font = underlined_font)
        expense_btn = tk.Button(income_window,
                                text = "My expenses",
                                command = expenses_message)
        insights_btn = tk.Button(income_window,
                                text = "My insights",
                                command = insights_message)
        # Income image.
        image = Image.open("income_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        income_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        income_image.image = img

        # Expense image.
        image = Image.open("expense_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        expense_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        expense_image.image = img

        # Insights image.
        image = Image.open("insights_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        insights_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        insights_image.image = img

        # Add income table.
        create_table()

        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        description_lbl.place(x = 200, y = 220)
        canvas.place(x = 0, y = 20)
        side_bar.place(x = 0, y = 122)
        income_btn.place(x = 40, y = 250)
        income_image.place(x = 50, y = 190)
        expense_btn.place(x = 40, y = 415)
        expense_image.place(x = 50, y = 355)
        insights_btn.place(x = 40, y = 580)
        insights_image.place(x = 50, y = 520)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit_btn.place(x = 1110, y = 40)
        back_btn.place(x = 150, y = 700)

        income_window.mainloop()

    def open_expenses_window():
        """Function to open my expenses page."""
        def exit_expenses_window():
            """Function to ensure the user wants to exit the
            expenses_window.
            """
            response = messagebox.askquestion("Exit Programme?","Your progress"
                                              " will NOT be saved.\nAre you "
                                              "sure you want to exit the "
                                              "program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(expenses_window,
                                    command = expenses_window.quit)
                confirm_btn.pack()
                expenses_window.destroy()

        def update_scrollregion(event):
            """Configure the canvas and scrollable content frame"""
            # The 'event' parameter is required by the event handler but is
            # not used.
            canvas.configure(scrollregion = canvas.bbox("all"))

        def create_table():
            """Function to create household and living expenses 
            table.
            """
            def clear():
                """Function to clear all user input."""
                a_expenses_choice.set("Weekly")
                a_type_1.set("")
                a_type_2.set("")
                a_type_3.set("")
                a_type_4.set("")
                a_type_5.set("")
                a_type_6.set("")
                a_type_7.set("")
                a_type_8.set("")
                a_type_9.set("")
                a_type_10.set("")
                a_type_11.set("")
                a_type_12.set("")
                b_expenses_choice.set("Weekly")
                b_type_1.set("")
                b_type_2.set("")
                b_type_3.set("")
                b_type_4.set("")
                b_type_5.set("")
                b_type_6.set("")
                c_expenses_choice.set("Weekly")
                c_type_1.set("")
                c_type_2.set("")
                c_type_3.set("")
                d_expenses_choice.set("Weekly")
                d_type_1.set("")
                d_type_2.set("")
                d_type_3.set("")
                d_type_4.set("")
                e_expenses_choice.set("Weekly")
                e_type_1.set("")
                e_type_2.set("")
                e_type_3.set("")
                f_expenses_choice.set("Weekly")
                f_type_1.set("")
                f_type_2.set("")
                f_type_3.set("")
                f_type_4.set("")
                f_type_5.set("")
                f_type_6.set("")
                f_type_7.set("")
                f_type_8.set("")
                f_type_9.set("")

                a_total_expenses.set("")
                b_total_expenses.set("")
                c_total_expenses.set("")
                d_total_expenses.set("")
                e_total_expenses.set("")
                f_total_expenses.set("")

            def a_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    a_result = float(a_type_1.get()) + float(a_type_2.get()) \
                            + float(a_type_3.get()) + float(a_type_4.get()) \
                            + float(a_type_5.get()) + float(a_type_6.get()) \
                            + float(a_type_7.get()) + float(a_type_8.get()) \
                            + float(a_type_9.get()) + float(a_type_10.get()) \
                            + float(a_type_11.get()) + float(a_type_12.get())

                except ValueError:
                    a_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                a_total_expenses.set(f"{a_result:.2f}")

            def b_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    b_result = float(b_type_1.get()) + float(b_type_2.get()) \
                               + float(b_type_3.get()) \
                               + float(b_type_4.get()) \
                               + float(b_type_5.get()) \
                               + float(b_type_6.get())

                except ValueError:
                    b_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                b_total_expenses.set(f"{b_result:.2f}")

            def c_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    c_result = float(c_type_1.get()) + float(c_type_2.get()) \
                               + float(c_type_3.get())

                except ValueError:
                    c_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                c_total_expenses.set(f"{c_result:.2f}")

            def d_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    d_result = float(d_type_1.get()) + float(d_type_2.get()) \
                               + float(d_type_3.get()) + float(d_type_4.get())

                except ValueError:
                    d_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                d_total_expenses.set(f"{d_result:.2f}")

            def e_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    e_result = float(e_type_1.get()) + float(e_type_2.get()) \
                               + float(e_type_3.get())

                except ValueError:
                    e_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                e_total_expenses.set(f"{e_result:.2f}")

            def f_calculate_total_expenses():
                """Functiton to calculate total expenses."""
                try:
                    f_result = float(f_type_1.get()) + float(f_type_2.get()) \
                            + float(f_type_3.get()) + float(f_type_4.get()) \
                            + float(f_type_5.get()) + float(f_type_6.get()) \
                            + float(f_type_7.get()) + float(f_type_8.get()) \
                            + float(f_type_9.get())

                except ValueError:
                    f_result = messagebox.showerror("Invalid input", "Please "
                                                    "enter all fields using "
                                                    "number 0 and/or "
                                                    "positive numbers that "
                                                    "represent your expenses.")
                f_total_expenses.set(f"{f_result:.2f}")

            def expenses_next():
                """Function to save the user expenses, validate their 
                entries, and redirect to expenses page.
                """
                def get_income_period():
                    """Read the user information from user finance info 
                    and find the income period which is in brackets.
                    """
                    with open("user_finance_info.txt", "r") as file:
                        for line in file:
                            if "Income" in line:
                                start_idx = line.find('(')
                                end_idx = line.find(')')

                                if start_idx != -1 and end_idx != -1 and \
                                    end_idx > start_idx:
                                    income_period = line\
                                    [start_idx + 1:end_idx].strip()

                                    return income_period

                def get_total_income():
                    """Read user finance info file and get total 
                    income.
                    """
                    with open("user_finance_info.txt", "r") as file:
                        lines = file.readlines()
                        for i, line in enumerate(lines):
                            if "Income" in line:
                                total_income = float(lines[i + 8].strip())

                                return total_income

                def monthly_to_weekly(monthly_expenditure):
                    """Convert monthly expenditure to weekly 
                    expenditure.
                    """
                    average_weeks_per_month = 4.345
                    weekly_expenditure = float(monthly_expenditure) / \
                                        average_weeks_per_month

                    return weekly_expenditure

                def fortnightly_to_weekly(fortnightly_expenditure):
                    """Convert fortnightly expenditure to weekly
                    expenditure.
                    """
                    weekly_expenditure = float(fortnightly_expenditure) / 2

                    return weekly_expenditure

                def fourweekly_to_weekly(fourweekly_expenditure):
                    """Convert four-weekly expenditure to weekly
                    expenditure.
                    """
                    weekly_expenditure = float(fourweekly_expenditure) / 4

                    return weekly_expenditure

                def yearly_to_weekly(yearly_expenditure):
                    """Convert yearly expenditure to weekly 
                    expenditure.
                    """
                    weekly_expenditure = float(yearly_expenditure) / 52

                    return weekly_expenditure

                a_calculate_total_expenses()
                b_calculate_total_expenses()
                c_calculate_total_expenses()
                d_calculate_total_expenses()
                e_calculate_total_expenses()
                f_calculate_total_expenses()
                a_expenses_period = a_expenses_choice.get()
                b_expenses_period = b_expenses_choice.get()
                c_expenses_period = c_expenses_choice.get()
                d_expenses_period = d_expenses_choice.get()
                e_expenses_period = e_expenses_choice.get()
                f_expenses_period = f_expenses_choice.get()
                income_period = get_income_period()
                total_income = get_total_income()

                # Initialize all weekly expenses.
                weekly_total_income = total_income
                weekly_a_expenses = float(a_total_expenses.get())
                weekly_b_expenses = float(b_total_expenses.get())
                weekly_c_expenses = float(c_total_expenses.get())
                weekly_d_expenses = float(d_total_expenses.get())
                weekly_e_expenses = float(e_total_expenses.get())
                weekly_f_expenses = float(f_total_expenses.get())

                # Convert FORTNIGHTLY payments to weekly.
                if income_period == "Fortnightly":
                    fortnightly_expenditure = float(total_income)
                    weekly_total_income = fortnightly_to_weekly\
                                         (fortnightly_expenditure)
                elif a_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(a_total_expenses.get())
                    weekly_a_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)
                elif b_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(b_total_expenses.get())
                    weekly_b_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)
                elif c_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(c_total_expenses.get())
                    weekly_c_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)
                elif d_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(d_total_expenses.get())
                    weekly_d_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)
                elif e_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(e_total_expenses.get())
                    weekly_e_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)
                elif f_expenses_period == "Fortnightly":
                    fortnightly_expenditure = float(f_total_expenses.get())
                    weekly_f_expenses = fortnightly_to_weekly\
                                        (fortnightly_expenditure)

                # Convert FOUR-WEEKLY payments to weekly.
                elif income_period == "Four-weekly":
                    fourweekly_expenditure = float(total_income)
                    weekly_total_income = fourweekly_to_weekly\
                                        (fourweekly_expenditure)
                elif a_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(a_total_expenses.get())
                    weekly_a_expenses = fourweekly_to_weekly\
                                     (fourweekly_expenditure)
                elif b_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(b_total_expenses.get())
                    weekly_b_expenses = fourweekly_to_weekly\
                                        (fourweekly_expenditure)
                elif c_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(c_total_expenses.get())
                    weekly_c_expenses = fourweekly_to_weekly\
                                        (fourweekly_expenditure)
                elif d_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(d_total_expenses.get())
                    weekly_d_expenses = fourweekly_to_weekly\
                                        (fourweekly_expenditure)
                elif e_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(e_total_expenses.get())
                    weekly_e_expenses = fourweekly_to_weekly\
                                        (fourweekly_expenditure)
                elif f_expenses_period == "Four-weekly":
                    fourweekly_expenditure = float(f_total_expenses.get())
                    weekly_f_expenses = fourweekly_to_weekly\
                                        (fourweekly_expenditure)

                # Convert MONTHLY payments to weekly.
                elif income_period == "Monthly":
                    monthly_expenditure = float(total_income)
                    weekly_total_income = monthly_to_weekly\
                        (monthly_expenditure)
                elif a_expenses_period == "Monthly":
                    monthly_expenditure = float(a_total_expenses.get())
                    weekly_a_expenses = monthly_to_weekly\
                        (monthly_expenditure)
                elif b_expenses_period == "Monthly":
                    monthly_expenditure = float(b_total_expenses.get())
                    weekly_b_expenses = monthly_to_weekly\
                        (monthly_expenditure)
                elif c_expenses_period == "Monthly":
                    monthly_expenditure = float(c_total_expenses.get())
                    weekly_c_expenses = monthly_to_weekly\
                        (monthly_expenditure)
                elif d_expenses_period == "Monthly":
                    monthly_expenditure = float(d_total_expenses.get())
                    weekly_d_expenses = monthly_to_weekly\
                        (monthly_expenditure)
                elif e_expenses_period == "Monthly":
                    monthly_expenditure = float(e_total_expenses.get())
                    weekly_e_expenses = monthly_to_weekly\
                        (monthly_expenditure)
                elif f_expenses_period == "Monthly":
                    monthly_expenditure = float(f_total_expenses.get())
                    weekly_f_expenses = monthly_to_weekly\
                        (monthly_expenditure)

                # Convert YEARLY payments to weekly.
                elif income_period == "Yearly":
                    yearly_expenditure = float(total_income)
                    weekly_total_income = yearly_to_weekly\
                        (yearly_expenditure)
                elif a_expenses_period == "Yearly":
                    yearly_expenditure = float(a_total_expenses.get())
                    weekly_a_expenses = yearly_to_weekly\
                        (yearly_expenditure)
                elif b_expenses_period == "Yearly":
                    yearly_expenditure = float(b_total_expenses.get())
                    weekly_b_expenses = yearly_to_weekly\
                        (yearly_expenditure)
                elif c_expenses_period == "Yearly":
                    yearly_expenditure = float(c_total_expenses.get())
                    weekly_c_expenses = yearly_to_weekly\
                        (yearly_expenditure)
                elif d_expenses_period == "Yearly":
                    yearly_expenditure = float(d_total_expenses.get())
                    weekly_d_expenses = yearly_to_weekly\
                        (yearly_expenditure)
                elif e_expenses_period == "Yearly":
                    yearly_expenditure = float(e_total_expenses.get())
                    weekly_e_expenses = yearly_to_weekly\
                        (yearly_expenditure)
                elif f_expenses_period == "Yearly":
                    yearly_expenditure = float(f_total_expenses.get())
                    weekly_f_expenses = yearly_to_weekly\
                        (yearly_expenditure)

                # Add all the expenses together.
                weekly_total_expenses = float(weekly_a_expenses
                                         + weekly_b_expenses
                                         + weekly_c_expenses
                                         + weekly_d_expenses
                                         + weekly_e_expenses
                                         + weekly_f_expenses)

                difference = float(weekly_total_income - weekly_total_expenses)
                print("The difference between income and expenses is: "
                      + f"{difference:.2f}")

                # Put all the users expense info in a file.
                with open("user_finance_info.txt", "a") as file:
                    file.write(f"Weekly total income: {weekly_total_income}\n"
                               + "Weekly total expenses: "
                               + f"{weekly_total_expenses}\n"
                               + f"Weekly a expenses: {weekly_a_expenses}\n"
                               + f"Weekly b expenses: {weekly_b_expenses}\n"
                               + f"Weekly c expenses: {weekly_c_expenses}\n"
                               + f"Weekly d expenses: {weekly_d_expenses}\n"
                               + f"Weekly e expenses: {weekly_e_expenses}\n"
                               + f"Weekly f expenses: {weekly_f_expenses}\n"
                               + f"Difference: {difference}\n\n")
                messagebox.showinfo("Save successfull", "Your expenses has "
                                    + "successfully been saved.")
                expenses_to_insights()

            def on_mousewheel(event):
                """Bind the Canvas to Mousewheel Events."""
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

            canvas.bind_all("<MouseWheel>", on_mousewheel)

            # Create titles for each expense category.
            a_expenses_lbl = tk.Label(content_frame,
                                      text = "1. Household and Living "
                                      "Expenses:",
                                      font = ("Helevitica", 15, "bold"))
            b_expenses_lbl = tk.Label(content_frame,
                                      text = "2. Vehicle Related Expenses:",
                                      font = ("Helevitica", 15, "bold"))
            c_expenses_lbl = tk.Label(content_frame,
                                      text = "3. University Related Expenses:",
                                      font = ("Helevitica", 15, "bold"))
            d_expenses_lbl = tk.Label(content_frame,
                                      text = "4. Debt:",
                                      font = ("Helevitica", 15, "bold"))
            e_expenses_lbl = tk.Label(content_frame,
                                      text = "5. Pet Related Expenses:",
                                      font = ("Helevitica", 15, "bold"))
            f_expenses_lbl = tk.Label(content_frame,
                                      text = "6. Wants/Flexible Expenses:",
                                      font = ("Helevitica", 15, "bold"))
            a_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")
            b_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")
            c_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")
            d_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")
            e_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")
            f_expenses_choice = ttk.Combobox(content_frame,
                                             width = 17,
                                             state = "readonly")

            # Adding combobox drop down list for all the expense categories.
            a_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")
            b_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")
            c_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")
            d_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")
            e_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")
            f_expenses_choice["values"] = ("Weekly",
                                           "Fortnightly",
                                           "Four-weekly",
                                           "Monthly",
                                           "Yearly")

            # Shows weekly as a default value.
            a_expenses_choice.current(0)
            b_expenses_choice.current(0)
            c_expenses_choice.current(0)
            d_expenses_choice.current(0)
            e_expenses_choice.current(0)
            f_expenses_choice.current(0)

            # Create content for household and living expenses (a).
            a_type_1_lbl = tk.Label(content_frame,
                                    text = "Rent/board:",
                                    font=("Helvetica", 15, "bold"))
            a_type_2_lbl = tk.Label(content_frame,
                                    text = "Power:",
                                    font=("Helvetica", 15, "bold"))
            a_type_3_lbl = tk.Label(content_frame,
                                    text = "Internet:",
                                    font=("Helvetica", 15, "bold"))
            a_type_4_lbl = tk.Label(content_frame,
                                    text = "Water:",
                                    font=("Helvetica", 15, "bold"))
            a_type_5_lbl = tk.Label(content_frame,
                                    text = "Gas:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_6_lbl = tk.Label(content_frame,
                                    text = "Phone plan:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_7_lbl = tk.Label(content_frame,
                                    text = "Insurance",
                                    font = ("Helvetica", 15, "bold"))
            a_type_8_lbl = tk.Label(content_frame,
                                    text = "Groceries:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_9_lbl = tk.Label(content_frame,
                                    text = "Medical costs:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_10_lbl = tk.Label(content_frame,
                                    text = "Gym:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_11_lbl = tk.Label(content_frame,
                                    text = "Transport fare:",
                                    font = ("Helvetica", 15, "bold"))
            a_type_12_lbl = tk.Label(content_frame,
                                    text = "Other required costs:",
                                    font = ("Helvetica", 15, "bold"))
            a_calc_expenses_btn = tk.Button(content_frame,
                                    text = "Calculate total expenses:",
                                    font = ("Helvetica", 15, "bold"),
                                    bg = "gold",
                                    command = a_calculate_total_expenses)
            #  # Display dollar sign buttons for every entry.
            for i in range(3, 16):
                a_dollar_sign = ttk.Label(content_frame,
                                         text = "$",
                                         font = ("Helvetica", 10))
                a_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            dollar_13_lbl = tk.Label(content_frame,
                                     text = "$",
                                     font = ("Helvetica", 10))

            # Create content for vehicle related expenses (b).
            b_type_1_lbl = tk.Label(content_frame,
                                    text = "Gas:",
                                    font=("Helvetica", 15, "bold"))
            b_type_2_lbl = tk.Label(content_frame,
                                    text = "Parking:",
                                    font=("Helvetica", 15, "bold"))
            b_type_3_lbl = tk.Label(content_frame,
                                    text = "Vehicle insurance:",
                                    font=("Helvetica", 15, "bold"))
            b_type_4_lbl = tk.Label(content_frame,
                                    text = "Warrant of fitness (WOF):",
                                    font=("Helvetica", 15, "bold"))
            b_type_5_lbl = tk.Label(content_frame,
                                    text = "Vehicle registration:",
                                    font = ("Helvetica", 15, "bold"))
            b_type_6_lbl = tk.Label(content_frame,
                                    text = "Vehicle repairs:",
                                    font = ("Helvetica", 15, "bold"))
            b_calc_expenses_btn = tk.Button(content_frame,
                                    text = "Calculate total expenses:",
                                    font = ("Helvetica", 15, "bold"),
                                    bg = "gold",
                                    command = b_calculate_total_expenses)
            # Display dollar sign buttons for every entry.
            for i in range(24, 30):
                b_dollar_sign = ttk.Label(content_frame,
                                         text = "$",
                                         font = ("Helvetica", 10))
                b_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            b_dollar_lbl = tk.Label(content_frame,
                                     text = "$",
                                     font = ("Helvetica", 10))

            # Create content for university related expenses (c).
            c_type_1_lbl = tk.Label(content_frame,
                                    text = "Supplies (e.g. Textbooks, "
                                  "laboratory gear):",
                                    font=("Helvetica", 15, "bold"))
            c_type_2_lbl = tk.Label(content_frame,
                                    text = "Photocopying/printing:",
                                    font=("Helvetica", 15, "bold"))
            c_type_3_lbl = tk.Label(content_frame,
                                    text = "Other (e.g. Fees):",
                                    font=("Helvetica", 15, "bold"))
            c_calc_expenses_btn = tk.Button(content_frame,
                                            text = "Calculate total "
                                            "expenses:",
                                            font = ("Helvetica", 15, "bold"),
                                            bg = "gold",
                                            command = \
                                            c_calculate_total_expenses)
            for i in range(45, 48):
                c_dollar_sign = ttk.Label(content_frame,
                                         text = "$",
                                         font = ("Helvetica", 10))
                c_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            c_dollar_lbl = tk.Label(content_frame,
                                     text = "$",
                                     font = ("Helvetica", 10))

            # Create content for debt (d).
            d_type_1_lbl = tk.Label(content_frame,
                                    text = "Hire purchase (e.g. Afterpay):",
                                    font=("Helvetica", 15, "bold"))
            d_type_2_lbl = tk.Label(content_frame,
                                    text = "Credit card:",
                                    font=("Helvetica", 15, "bold"))
            d_type_3_lbl = tk.Label(content_frame,
                                    text = "Debt repaymemt "
                                    "(e.g. Student loan):",
                                    font=("Helvetica", 15, "bold"))
            d_type_4_lbl = tk.Label(content_frame,
                                    text = "Fines:",
                                    font=("Helvetica", 15, "bold"))
            d_calc_expenses_btn = tk.Button(content_frame,
                                        text = "Calculate total expenses:",
                                        font = ("Helvetica", 15, "bold"),
                                        bg = "gold",
                                        command = d_calculate_total_expenses)
            for i in range(66, 70):
                d_dollar_sign = ttk.Label(content_frame,
                                          text = "$",
                                          font = ("Helvetica", 10))
                d_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            d_dollar_lbl = tk.Label(content_frame,
                                    text = "$",
                                    font = ("Helvetica", 10))

            # Create content for university related expenses (c).
            e_type_1_lbl = tk.Label(content_frame,
                                    text = "Pet registration:",
                                    font=("Helvetica", 15, "bold"))
            e_type_2_lbl = tk.Label(content_frame,
                                    text = "Pet food:",
                                    font=("Helvetica", 15, "bold"))
            e_type_3_lbl = tk.Label(content_frame,
                                    text = "Vet:",
                                    font=("Helvetica", 15, "bold"))
            e_calc_expenses_btn = tk.Button(content_frame,
                                        	text = "Calculate total "
                                                    "expenses:",
                                            font = ("Helvetica", 15, "bold"),
                                            bg = "gold",
                                            command =
                                            e_calculate_total_expenses)
            for i in range(87, 90):
                e_dollar_sign = ttk.Label(content_frame,
                                         text = "$",
                                         font = ("Helvetica", 10))
                e_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            e_dollar_lbl = tk.Label(content_frame,
                                     text = "$",
                                     font = ("Helvetica", 10))

            # Create content for wants/flexible expenses (f).
            f_type_1_lbl = tk.Label(content_frame,
                                    text = "Savings:",
                                    font=("Helvetica", 15, "bold"))
            f_type_2_lbl = tk.Label(content_frame,
                                    text = "Holidays/trips home:",
                                    font=("Helvetica", 15, "bold"))
            f_type_3_lbl = tk.Label(content_frame,
                                    text = "Shopping (e.g. Clothing, "
                                    "cosmetics):",
                                    font=("Helvetica", 15, "bold"))
            f_type_4_lbl = tk.Label(content_frame,
                                    text = "Entertainment (e.g. Concerts, "
                                    "eating out):",
                                    font=("Helvetica", 15, "bold"))
            f_type_5_lbl = tk.Label(content_frame,
                                    text = "Parties/alcohol:",
                                    font = ("Helvetica", 15, "bold"))
            f_type_6_lbl = tk.Label(content_frame,
                                    text = "Hair cuts:",
                                    font = ("Helvetica", 15, "bold"))
            f_type_7_lbl = tk.Label(content_frame,
                                    text = "Presents/gifts",
                                    font = ("Helvetica", 15, "bold"))
            f_type_8_lbl = tk.Label(content_frame,
                                    text = "Subscriptions (e.g.; Netflix, "
                                    "spotify):",
                                    font = ("Helvetica", 15, "bold"))
            f_type_9_lbl = tk.Label(content_frame,
                                    text = "Other (e.g. Vape products):",
                                    font = ("Helvetica", 15, "bold"))
            f_calc_expenses_btn = tk.Button(content_frame,
                                    text = "Calculate total expenses:",
                                    font = ("Helvetica", 15, "bold"),
                                    bg = "gold",
                                    command = f_calculate_total_expenses)
            for i in range(108, 117):
                f_dollar_sign = ttk.Label(content_frame,
                                         text = "$",
                                         font = ("Helvetica", 10))
                f_dollar_sign.grid(row=i,
                                   column = 0,
                                   padx = (10, 0),
                                   pady = 5,
                                   sticky = "e")
            f_dollar_lbl = tk.Label(content_frame,
                                     text = "$",
                                     font = ("Helvetica", 10))

            # Other conent that is outside the content frame.
            clear_btn = tk.Button(expenses_window,
                                  text = "Clear all",
                                  width = 10,
                                  height = 2,
                                  bg = "firebrick1",
                                  command = clear)
            next_btn = tk.Button(expenses_window,
                                 text = "Next",
                                 width = 10,
                                 height = 2,
                                 fg = "black",
                                 bg = "gold",
                                 command = expenses_next)

            # Declare a, b, c, d, e, and f expenses types as string variables.
            a_type_1 = tk.StringVar()
            a_type_2 = tk.StringVar()
            a_type_3 = tk.StringVar()
            a_type_4 = tk.StringVar()
            a_type_5 = tk.StringVar()
            a_type_6 = tk.StringVar()
            a_type_7 = tk.StringVar()
            a_type_8 = tk.StringVar()
            a_type_9 = tk.StringVar()
            a_type_10 = tk.StringVar()
            a_type_11 = tk.StringVar()
            a_type_12 = tk.StringVar()
            a_total_expenses = tk.StringVar()
            b_type_1 = tk.StringVar()
            b_type_2 = tk.StringVar()
            b_type_3 = tk.StringVar()
            b_type_4 = tk.StringVar()
            b_type_5 = tk.StringVar()
            b_type_6 = tk.StringVar()
            b_total_expenses = tk.StringVar()
            c_type_1 = tk.StringVar()
            c_type_2 = tk.StringVar()
            c_type_3 = tk.StringVar()
            c_total_expenses = tk.StringVar()
            d_type_1 = tk.StringVar()
            d_type_2 = tk.StringVar()
            d_type_3 = tk.StringVar()
            d_type_4 = tk.StringVar()
            d_total_expenses = tk.StringVar()
            e_type_1 = tk.StringVar()
            e_type_2 = tk.StringVar()
            e_type_3 = tk.StringVar()
            e_total_expenses = tk.StringVar()
            f_type_1 = tk.StringVar()
            f_type_2 = tk.StringVar()
            f_type_3 = tk.StringVar()
            f_type_4 = tk.StringVar()
            f_type_5 = tk.StringVar()
            f_type_6 = tk.StringVar()
            f_type_7 = tk.StringVar()
            f_type_8 = tk.StringVar()
            f_type_9 = tk.StringVar()
            f_total_expenses = tk.StringVar()

            # Create entries for each a, b, c, d, e, and f expenses type.
            a_type_1_entry = tk.Entry(content_frame,
                                      textvariable = a_type_1)
            a_type_2_entry = tk.Entry(content_frame,
                                      textvariable = a_type_2)
            a_type_3_entry = tk.Entry(content_frame,
                                      textvariable = a_type_3)
            a_type_4_entry = tk.Entry(content_frame,
                                      textvariable = a_type_4)
            a_type_5_entry = tk.Entry(content_frame,
                                      textvariable = a_type_5)
            a_type_6_entry = tk.Entry(content_frame,
                                      textvariable = a_type_6)
            a_type_7_entry = tk.Entry(content_frame,
                                      textvariable = a_type_7)
            a_type_8_entry = tk.Entry(content_frame,
                                      textvariable = a_type_8)
            a_type_9_entry = tk.Entry(content_frame,
                                      textvariable = a_type_9)
            a_type_10_entry = tk.Entry(content_frame,
                                      textvariable = a_type_10)
            a_type_11_entry = tk.Entry(content_frame,
                                      textvariable = a_type_11)
            a_type_12_entry = tk.Entry(content_frame,
                                       textvariable = a_type_12)
            a_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = a_total_expenses)
            b_type_1_entry = tk.Entry(content_frame,
                                      textvariable = b_type_1)
            b_type_2_entry = tk.Entry(content_frame,
                                      textvariable = b_type_2)
            b_type_3_entry = tk.Entry(content_frame,
                                      textvariable = b_type_3)
            b_type_4_entry = tk.Entry(content_frame,
                                      textvariable = b_type_4)
            b_type_5_entry = tk.Entry(content_frame,
                                      textvariable = b_type_5)
            b_type_6_entry = tk.Entry(content_frame,
                                      textvariable = b_type_6)
            b_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = b_total_expenses)
            c_type_1_entry = tk.Entry(content_frame,
                                      textvariable = c_type_1)
            c_type_2_entry = tk.Entry(content_frame,
                                      textvariable = c_type_2)
            c_type_3_entry = tk.Entry(content_frame,
                                      textvariable = c_type_3)
            c_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = c_total_expenses)
            d_type_1_entry = tk.Entry(content_frame,
                                      textvariable = d_type_1)
            d_type_2_entry = tk.Entry(content_frame,
                                      textvariable = d_type_2)
            d_type_3_entry = tk.Entry(content_frame,
                                      textvariable = d_type_3)
            d_type_4_entry = tk.Entry(content_frame,
                                      textvariable = d_type_4)
            d_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = d_total_expenses)
            e_type_1_entry = tk.Entry(content_frame,
                                      textvariable = e_type_1)
            e_type_2_entry = tk.Entry(content_frame,
                                      textvariable = e_type_2)
            e_type_3_entry = tk.Entry(content_frame,
                                      textvariable = e_type_3)
            e_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = e_total_expenses)
            f_type_1_entry = tk.Entry(content_frame,
                                      textvariable = f_type_1)
            f_type_2_entry = tk.Entry(content_frame,
                                      textvariable = f_type_2)
            f_type_3_entry = tk.Entry(content_frame,
                                      textvariable = f_type_3)
            f_type_4_entry = tk.Entry(content_frame,
                                      textvariable = f_type_4)
            f_type_5_entry = tk.Entry(content_frame,
                                      textvariable = f_type_5)
            f_type_6_entry = tk.Entry(content_frame,
                                      textvariable = f_type_6)
            f_type_7_entry = tk.Entry(content_frame,
                                      textvariable = f_type_7)
            f_type_8_entry = tk.Entry(content_frame,
                                      textvariable = f_type_8)
            f_type_9_entry = tk.Entry(content_frame,
                                      textvariable = f_type_9)
            f_total_expenses_entry = tk.Entry(content_frame,
                                              textvariable = f_total_expenses)

            # Place all the a, b, c, d, e, and f table content and other.
            a_expenses_lbl.grid(row = 0,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            a_expenses_choice.grid(row = 0,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            a_type_1_lbl.grid(row = 3,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_1_entry.grid(row = 3,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_2_lbl.grid(row = 4,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_2_entry.grid(row = 4,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_3_lbl.grid(row = 5,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_3_entry.grid(row = 5,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_4_lbl.grid(row = 6,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_4_entry.grid(row = 6,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_5_lbl.grid(row = 7,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_5_entry.grid(row = 7,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_6_lbl.grid(row = 8,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_6_entry.grid(row = 8,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_7_lbl.grid(row = 9,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_7_entry.grid(row = 9,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_8_lbl.grid(row = 10,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_8_entry.grid(row = 10,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_9_lbl.grid(row = 11,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            a_type_9_entry.grid(row = 11,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            a_type_10_lbl.grid(row = 12,
                               column = 0,
                               padx = 10,
                               pady = 5,
                               sticky = "w")
            a_type_10_entry.grid(row = 12,
                                 column = 1,
                                 padx = 10,
                                 pady = 5,
                                 sticky = "w")
            a_type_11_lbl.grid(row = 13,
                               column = 0,
                               padx = 10,
                               pady = 5,
                               sticky = "w")
            a_type_11_entry.grid(row = 13,
                                 column = 1,
                                 padx = 10,
                                 pady = 5,
                                 sticky = "w")
            a_type_12_lbl.grid(row = 14,
                               column = 0,
                               padx = 10,
                               pady = 5,
                               sticky = "w")
            a_type_12_entry.grid(row = 14,
                                 column = 1,
                                 padx = 10,
                                 pady = 5,
                                 sticky = "w")
            a_calc_expenses_btn.grid(row = 15,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            a_total_expenses_entry.grid(row = 15,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            dollar_13_lbl.grid(row = 15,
                               column = 1,
                               padx = 10,
                               pady = 10)

            b_expenses_lbl.grid(row = 21,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            b_expenses_choice.grid(row = 21,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            b_type_1_lbl.grid(row = 24,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            b_type_1_entry.grid(row = 24,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            b_type_2_lbl.grid(row = 25,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            b_type_2_entry.grid(row = 25,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            b_type_3_lbl.grid(row = 26,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            b_type_3_entry.grid(row = 26,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            b_type_4_lbl.grid(row = 27,
                              column = 0,
                              padx = 10, pady = 5,
                              sticky = "w")
            b_type_4_entry.grid(row = 27,
                                column = 1,
                                padx = 10, pady = 5,
                                sticky = "w")
            b_type_5_lbl.grid(row = 28,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            b_type_5_entry.grid(row = 28,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            b_type_6_lbl.grid(row = 29,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            b_type_6_entry.grid(row = 29,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            b_calc_expenses_btn.grid(row = 36,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            b_total_expenses_entry.grid(row = 36,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            b_dollar_lbl.grid(row = 36,
                              column = 1,
                              padx = 10,
                              pady = 10)

            c_expenses_lbl.grid(row = 42,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            c_expenses_choice.grid(row = 42,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            c_type_1_lbl.grid(row = 45,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            c_type_1_entry.grid(row = 45,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            c_type_2_lbl.grid(row = 46,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            c_type_2_entry.grid(row = 46,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            c_type_3_lbl.grid(row = 47,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            c_type_3_entry.grid(row = 47,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            c_calc_expenses_btn.grid(row = 54,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            c_total_expenses_entry.grid(row = 54,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            c_dollar_lbl.grid(row = 54,
                              column = 1,
                              padx = 10,
                              pady = 10)

            d_expenses_lbl.grid(row = 63,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            d_expenses_choice.grid(row = 63,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            d_type_1_lbl.grid(row = 66,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            d_type_1_entry.grid(row = 66,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            d_type_2_lbl.grid(row = 67,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            d_type_2_entry.grid(row = 67,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            d_type_3_lbl.grid(row = 68,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            d_type_3_entry.grid(row = 68,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            d_type_4_lbl.grid(row = 69,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            d_type_4_entry.grid(row = 69,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            d_calc_expenses_btn.grid(row = 76,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            d_total_expenses_entry.grid(row = 76,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            d_dollar_lbl.grid(row = 76,
                              column = 1,
                              padx = 10,
                              pady = 10)

            e_expenses_lbl.grid(row = 84,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            e_expenses_choice.grid(row = 84,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            e_type_1_lbl.grid(row = 87,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            e_type_1_entry.grid(row = 87,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            e_type_2_lbl.grid(row = 88,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            e_type_2_entry.grid(row = 88,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            e_type_3_lbl.grid(row = 89,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            e_type_3_entry.grid(row = 89,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            e_calc_expenses_btn.grid(row = 96,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            e_total_expenses_entry.grid(row = 96,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            e_dollar_lbl.grid(row = 96,
                              column = 1,
                              padx = 10,
                              pady = 10)

            f_expenses_lbl.grid(row = 105,
                                column = 0,
                                padx = 10,
                                pady = 10,
                                sticky = "w")
            f_expenses_choice.grid(row = 105,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = "w")
            f_type_1_lbl.grid(row = 108,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_1_entry.grid(row = 108,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_2_lbl.grid(row = 109,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_2_entry.grid(row = 109,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_3_lbl.grid(row = 110,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_3_entry.grid(row = 110,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_4_lbl.grid(row = 111,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_4_entry.grid(row = 111,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_5_lbl.grid(row = 112,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_5_entry.grid(row = 112,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_6_lbl.grid(row = 113,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_6_entry.grid(row = 113,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_7_lbl.grid(row = 114,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_7_entry.grid(row = 114,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_8_lbl.grid(row = 115,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_8_entry.grid(row = 115,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_type_9_lbl.grid(row = 116,
                              column = 0,
                              padx = 10,
                              pady = 5,
                              sticky = "w")
            f_type_9_entry.grid(row = 116,
                                column = 1,
                                padx = 10,
                                pady = 5,
                                sticky = "w")
            f_calc_expenses_btn.grid(row = 123,
                                     column = 0,
                                     padx = 10,
                                     pady = (10, 5),
                                     sticky = "w")
            f_total_expenses_entry.grid(row = 123,
                                        column = 1,
                                        padx = 10,
                                        pady = 10)
            f_dollar_lbl.grid(row = 123,
                              column = 1,
                              padx = 10,
                              pady = 10)

            clear_btn.place(x = 150, y = 630)
            next_btn.place(x = 1110, y = 700)

        def insights_message():
            """Function to tell the user to enter their income and 
            expenses in order to see insights.
            """
            messagebox.showerror("No input", "Please enter your income "
                                 + "and expenses so that insights can be "
                                 + "made.")

        # Create my income page.
        global expenses_window
        expenses_window = tk.Tk()
        expenses_window.geometry("1200x750")
        expenses_window.title("My expenses")
        expenses_window.resizable(False, False)

        # Create a Frame for Grid Layout.
        frame = ttk.Frame(expenses_window)
        frame.place(x = 290, y = 290)

        # Create a Canvas and Scrollbar.
        canvas = tk.Canvas(frame,
                            width = 600,
                            height=400)
        scrollbar = ttk.Scrollbar(frame,
                                  orient = "vertical",
                                  command = canvas.yview)
        canvas.configure(yscrollcommand = scrollbar.set)

        # Create a Frame for Scrollable Content.
        content_frame = ttk.Frame(canvas)
        content_frame.bind("<Configure>", update_scrollregion)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(expenses_window,
                         text = "My expenses:",
                         font = ("Helvetica", 40))
        description_lbl = tk.Label(expenses_window,
                                   text = "Please enter the amount you spend "
                                   + "(expenses) below in the six different "
                                   + "categories, you can choose weekly, "
                                   + "fortnightly, four-weekly, monthly or "
                                   + "yearly amounts.\nThis program will "
                                   + "calculate your total expenses per "
                                   + "category. Please scroll down to view "
                                   + "more expenses.",
                                   justify = LEFT)
        header_canvas = Canvas(expenses_window,
                              height = 100,
                              width = 1210,
                              bg = "CadetBlue2")
        home_btn = tk.Button(expenses_window,
                             text = "Home",
                             width = 10,
                             height = 2,
                             bg = "darkgrey",
                             command = expenses_to_main)
        open_about_btn = tk.Button(expenses_window,
                             text = "About",
                             width = 10,
                             height = 2,
                             fg = "black",
                             bg = "darkgrey",
                             command = expenses_to_about)
        open_budget_btn = tk.Button(expenses_window,
                                    text = "My Budget",
                                    font = underlined_font,
                                    width = 10,
                                    height = 2,
                                    fg = "black",
                                    bg = "darkgrey")
        open_tips_btn = tk.Button(expenses_window,
                                  text = "Tips",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = tips_message)
        open_help_btn = tk.Button(expenses_window,
                                  text = "Help",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = expenses_to_help)
        profile_btn = tk.Button(expenses_window,
                                text = "Profile",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "grey",
                                command = open_profile)
        exit_btn = tk.Button(expenses_window,
                         text = "Exit",
                         width = 10,
                         height = 2,
                         fg = "black",
                         bg = "grey",
                         command = exit_expenses_window)
        back_btn = tk.Button(expenses_window,
                             text = "Back",
                             width = 10,
                             height = 2,
                             fg = "black",
                             bg = "grey",
                             command = expenses_to_income)
        # Create progress bar on the side.
        side_bar = Canvas(expenses_window,
                          height = 900,
                          width = 140,
                          bg = "CadetBlue2")
        income_btn = tk.Button(expenses_window,
                               text = "My Income",
                               command = expenses_to_income)
        expense_btn = tk.Button(expenses_window,
                                text = "My expenses",
                                font = underlined_font)
        insights_btn = tk.Button(expenses_window,
                                text = "My insights",
                                command = insights_message)
        # Income image.
        image = Image.open("income_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        income_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        income_image.image = img

        # Expense image.
        image = Image.open("expense_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        expense_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        expense_image.image = img

        # Insights image.
        image = Image.open("insights_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        insights_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        insights_image.image = img

        # Create expenses table.
        create_table()

        # Create Window Resizing Configuration.
        expenses_window.columnconfigure(0, weight=1)
        expenses_window.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # Pack Widgets onto the Window.
        canvas.create_window((0, 0), window = content_frame, anchor = "nw")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        description_lbl.place(x = 200, y = 220)
        header_canvas.place(x = 0, y = 20)
        side_bar.place(x = 0, y = 122)
        income_btn.place(x = 40, y = 250)
        income_image.place(x = 50, y = 190)
        expense_btn.place(x = 40, y = 415)
        expense_image.place(x = 50, y = 355)
        insights_btn.place(x = 40, y = 580)
        insights_image.place(x = 50, y = 520)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit_btn.place(x = 1110, y = 40)
        back_btn.place(x = 150, y = 700)

        expenses_window.mainloop()

    def open_insights_window():
        """Function to open the insights window."""
        def exit_insights_window():
            """Function to ensure the user wants to exit the 
            insight_window.
            """
            response = messagebox.askquestion("Exit Programme?","Your "
                                              "progress will NOT be saved."
                                              "\nAre you sure you want to "
                                              "exit the program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                insights_window.destroy()

        def surplus_message():
            """Function to display income surplus message."""
            message = tk.Label(insights_window,
                               text = "\n\nCongragulations, you have an income"
                                   + " surplus. An income surplus, "
                                   + "indicated by green font, is when "
                                   + "incoming money exceeds your expenses, \n"
                                   + "meaning you have more money to assign "
                                   + "and can reach your goals quicker."
                                   + "Consider investing more in savings or "
                                   + "making extra payments towards debt.",
                                justify = LEFT)
            message.place(x = 200, y = 220)

        def equal_message():
            """Function to display equal income and expenses message."""
            message = tk.Label(insights_window,
                               text = "\n\nGreat job, your incoming money is "
                               + "equal to your expenses! This means you have "
                               + "allocated your income to expenses "
                               + "responsibly, however this may \nalso mean "
                               + "your budget is a bit too tight. "
                               + "Consider reducing expenses in areas "
                               + "where it is not essential.",
                               justify = LEFT)
            message.place(x = 200, y = 220)

        def deficit_message():
            """Function to display income defict message."""
            message = tk.Label(insights_window,
                               text = "\n\nNot quite, there is room for "
                                   + "improvement, you have an income deficit!"
                                   + " An income deficit, indicated by red "
                                   + "font, is when your "
                                   + "expenses exceed your income, meaning "
                                   + "you need more \nincoming money to meet "
                                   + "all your expenses or cut back in "
                                   + "wants/flexible expenses. Consider "
                                   + "reducing expenses in areas where it is "
                                   + "not essential.",
                                justify = LEFT)
            message.place(x = 200, y = 220)

        def get_finance_info():
            """Get the user's finance info"""
            weekly_total_income = None
            weekly_total_expenses = None
            weekly_a_expenses = None
            weekly_b_expenses = None
            weekly_c_expenses = None
            weekly_d_expenses = None
            weekly_e_expenses = None
            weekly_f_expenses = None
            difference = None
            with open("user_finance_info.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "Weekly total income: " in line:
                        parts = line.split(':', 1)
                        weekly_total_income = parts[1].strip()
                    elif "Weekly total expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_total_expenses = parts[1].strip()
                    elif "Weekly a expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_a_expenses = parts[1].strip()
                    elif "Weekly b expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_b_expenses = parts[1].strip()
                    elif "Weekly c expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_c_expenses = parts[1].strip()
                    elif "Weekly d expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_d_expenses = parts[1].strip()
                    elif "Weekly e expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_e_expenses = parts[1].strip()
                    elif "Weekly f expenses: " in line:
                        parts = line.split(':', 1)
                        weekly_f_expenses = parts[1].strip()
                    elif "Difference: " in line:
                        parts = line.split(':', 1)
                        difference = parts[1].strip()

            return ((float(weekly_total_income)),
                    (float(weekly_total_expenses)),
                    (float(weekly_a_expenses)),
                    (float(weekly_b_expenses)),
                    (float(weekly_c_expenses)),
                    (float(weekly_d_expenses)),
                    (float(weekly_e_expenses)),
                    (float(weekly_f_expenses)),
                    (float(difference)))

        # Create my income page.
        global insights_window
        insights_window = tk.Tk()
        insights_window.geometry("1200x750")
        insights_window.title("My Insights")
        insights_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(insights_window,
                         text = "My insights:",
                         font = ("Helvetica", 40))
        description_lbl = tk.Label(insights_window,
                                   text = "Here you can gain insights from "
                                   + "your income and expenses for the purpose"
                                   + " of reviewing your budget and making "
                                   + "adjustments.",
                                   justify = LEFT)
        header_canvas = Canvas(insights_window,
                               height = 100,
                               width = 1210,
                               bg = "CadetBlue2")
        home_btn = tk.Button(insights_window,
                             text = "Home",
                             width = 10,
                             height = 2,
                             bg = "darkgrey",
                             command = insights_to_main)
        open_about_btn = tk.Button(insights_window,
                                   text = "About",
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey",
                                   command = insights_to_about)
        open_budget_btn = tk.Button(insights_window,
                                    text = "My Budget",
                                    font = underlined_font,
                                    width = 10,
                                    height = 2,
                                    fg = "black",
                                    bg = "darkgrey")
        open_tips_btn = tk.Button(insights_window,
                                  text = "Tips",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = tips_message)
        open_help_btn = tk.Button(insights_window,
                                  text = "Help",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = insights_to_help)
        profile_btn = tk.Button(insights_window,
                                text = "Profile",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "grey",
                                command = open_profile)
        exit_btn = tk.Button(insights_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_insights_window)
        back_btn = tk.Button(insights_window,
                             text = "Back",
                             width = 10,
                             height = 2,
                             fg = "black",
                             bg = "grey",
                             command = insights_to_expenses)
        # Create progress bar on the side.
        side_bar = Canvas(insights_window,
                          height = 900,
                          width = 140,
                          bg = "CadetBlue2")
        income_btn = tk.Button(insights_window,
                               text = "My Income",
                               command = insights_to_income)
        expense_btn = tk.Button(insights_window,
                                text = "My expenses",
                                command = insights_to_expenses)
        insights_btn = tk.Button(insights_window,
                                 text = "My insights",
                                 font = underlined_font)
        # Income image.
        image = Image.open("income_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        income_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        income_image.image = img

        # Expense image.
        image = Image.open("expense_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        expense_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        expense_image.image = img

        # Insights image.
        image = Image.open("insights_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        insights_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        insights_image.image = img

        # Get the users finance info.
        weekly_total_income, weekly_total_expenses, weekly_a_expenses, \
        weekly_b_expenses, weekly_c_expenses, weekly_d_expenses, \
        weekly_e_expenses, weekly_f_expenses, difference = get_finance_info()

        # Tell the user their insights.
        if difference > 0:
            surplus_message()
            difference_lbl = tk.Label(insights_window,
                                      text = f"Difference ${difference:.2f}",
                                      font = ("Helvetica", 15),
                                      fg = "green")
        elif difference < 0:
            deficit_message()
            difference_lbl = tk.Label(insights_window,
                                      text = f"Difference ${difference:.2f}",
                                      font = ("Helvetica", 15),
                                      fg = "red")
        elif difference == 0:
            equal_message()
            difference_lbl = tk.Label(insights_window,
                                      text = f"Difference ${difference:.2f}",
                                      font = ("Helvetica", 15))
        outcome_lbl = tk.Label(insights_window,
                               text = "Weekly Totals:\n- Income $"
                               + f"{weekly_total_income:.2f}\n- Expenses "
                               + f"${weekly_total_expenses:.2f}",
                               font = ("Helvetica", 15),
                               justify = LEFT)

        # Create pie chart to display expenses.
        expense_categories = ["Household and Living", "Vehicle Related",
                              "University Related", "Debt", "Pet Related",
                              "Wants/Flexible"]
        data = [weekly_a_expenses, weekly_b_expenses, weekly_c_expenses,
                weekly_d_expenses, weekly_e_expenses, weekly_f_expenses]
        # Create a figure and a subplot.
        fig = Figure(figsize=(7, 4), dpi=100)
        ax = fig.add_subplot(111)
        # Create the pie chart.
        ax.pie(data,
               labels = expense_categories,
               autopct = '%1.1f%%',
               startangle = 140)
        ax.axis('equal')
        # Embed the plot in the Tkinter window.
        canvas = FigureCanvasTkAgg(fig,
                                   master = insights_window)
        canvas.draw()

        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        description_lbl.place(x = 200, y = 220)
        outcome_lbl.place(x = 200, y = 300)
        difference_lbl.place(x = 200, y = 390)
        header_canvas.place(x = 0, y = 20)
        side_bar.place(x = 0, y = 122)
        income_btn.place(x = 40, y = 250)
        income_image.place(x = 50, y = 190)
        expense_btn.place(x = 40, y = 415)
        expense_image.place(x = 50, y = 355)
        insights_btn.place(x = 40, y = 580)
        insights_image.place(x = 50, y = 520)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit_btn.place(x = 1110, y = 40)
        back_btn.place(x = 150, y = 700)
        canvas.get_tk_widget().place(x = 390, y = 300)

        insights_window.mainloop()

    # Function to ensure the user wants to exit the home_window.
    def popup():
        response = messagebox.askquestion("Exit Programme?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to exit the program?",
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(home_window,
                                command = home_window.quit)
            confirm_btn.pack()
            home_window.destroy()

    def tips_message():
        """Function to inform the user that the tips page is 
        unavailable.
        """
        messagebox.showerror("Error", "Page not found. Sorry, financial " +
                             "tips are currently unavailable. :(")

    def open_profile():
        """Function to show the user their profile and allow them to
        sign out.
        """
        def exit_profile():
            """Function to exit profile page."""
            response = messagebox.askquestion("Exit Programme?","Your progress"
                                          " will NOT be saved.\nAre you sure "
                                          "you want to exit the profile?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(profile_window,
                                    command = profile_window.quit)
                confirm_btn.pack()
                profile_window.destroy()

        def read_recent_users():
            """Reads and returns the most recent line from a file."""
            with open("recent_users.txt", "r") as file:
                lines = file.readlines()
                return lines[-1].strip()

        def get_user_info():
            """Read the user information from existing users and 
            reassign it to its original belonging variables.
            """
            with open("existing_users.txt", "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if username in line:
                        basic_user_info = lines[i + 1].strip()
                        additional_user_info = lines[i + 2].strip()

                        # Assign the user information thats in these lines
                        # to variables.
                        basic_parts = basic_user_info.split()
                        additional_parts = additional_user_info.split()
                        first_name = basic_parts[2]
                        last_name = basic_parts[3]
                        birthdate_str = additional_parts[1]
                        tertiary_status_words = additional_parts[5]
                        knowledge_words = additional_parts[9]

                        # Formatt the birthdate as (dd/mm/yyyy).
                        birthdate = datetime.strptime\
                                    (birthdate_str, "%Y-%m-%d")
                        formatted_birthdate = birthdate.strftime("%d/%m/%Y")

                        return first_name, last_name, formatted_birthdate, \
                        tertiary_status_words, knowledge_words

        # Create profile page.
        global profile_window
        profile_window = tk.Toplevel()
        profile_window.geometry("300x350")
        profile_window.title("Profile")
        profile_window.resizable(False, False)

        username = read_recent_users()
        first_name, last_name, formatted_birthdate, tertiary_status_words, \
        knowledge_words = get_user_info()

        # Create widow content.
        canvas = Canvas(profile_window,
                        height = 50,
                        width = 350,
                        bg = "CadetBlue2")
        title_lbl = tk.Label(profile_window,
                            text = "Profile:",
                            font = ("Helvetica", 15),
                            bg = "CadetBlue2")
        exit_btn = tk.Button(profile_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_profile)
        first_name_lbl = tk.Label(profile_window,
                                  text = (f"First name: "
                                                    f"{first_name}"),
                                  font = ("Helvetica", 11))
        last_name_lbl = tk.Label(profile_window,
                                 text = (f"Last name: {last_name}"),
                                 font = ("Helvetica", 11))
        username_lbl = tk.Label(profile_window,
                                text = (f"Username: {username}"),
                                font = ("Helvetica", 11))
        birthdate_lbl = tk.Label(profile_window,
                                 text = (f"Birthdate: "
                                                    f"{formatted_birthdate}"),
                                 font = ("Helvetica", 11))
        tertiary_status_lbl = tk.Label(profile_window,
                                       text = (f"Tertiary status: "
                                                f"{tertiary_status_words}"),
                                       font = ("Helvetica", 11))
        knowledge_lbl = tk.Label(profile_window,
                                 text = (f"Knowledge of budgeting: "
                                                    f"{knowledge_words}"),
                                 font = ("Helvetica", 11))
        signout_btn = tk.Button(profile_window,
                                text = "Signout",
                                width = 7,
                                height = 1,
                                fg = "black",
                                bg = "firebrick1",
                                command = signout)

        # Place window content.
        canvas.place(x = 0, y = 20)
        title_lbl.place(x = 10, y = 34)
        exit_btn.place(x = 200, y = 27)
        signout_btn.place(x = 120, y = 315)
        first_name_lbl.place(x = 20, y = 100)
        last_name_lbl.place(x = 20, y = 130)
        username_lbl.place(x = 20, y = 160)
        birthdate_lbl.place(x = 20, y = 190)
        tertiary_status_lbl.place(x = 20, y = 220)
        knowledge_lbl.place(x = 20, y = 250)

    def open_about_window():
        """Function to open the about window."""

        def exit_about():
            """Function to exit profile page."""
            response = messagebox.askquestion("Exit Programme?","Your progress"
                                          " will NOT be saved.\nAre you sure "
                                          "you want to exit the program?",
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(about_window,
                                    command = about_window.quit)
                confirm_btn.pack()
                about_window.destroy()

        # Create about page.
        global about_window
        about_window = tk.Tk()
        about_window.geometry("1200x750")
        about_window.title("About")
        about_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(about_window,
                         text = "About this program:",
                         font = ("Helvetica", 40))
        canvas = Canvas(about_window,
                        height = 100,
                        width = 1210,
                        bg = "CadetBlue2")
        home_btn = tk.Button(about_window,
                            text = "Home",
                            width = 10,
                            height = 2,
                            bg = "darkgrey",
                            command = about_to_main)
        open_about_btn = tk.Button(about_window,
                                   text = "About",
                                   font = underlined_font,
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey")
        open_budget_btn = tk.Button(about_window,
                                   text = "My Budget",
                                   width = 10,
                                   height = 2,
                                   fg = "black",
                                   bg = "darkgrey",
                                   command = about_to_income)
        open_tips_btn = tk.Button(about_window,
                                  text = "Tips",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = tips_message)
        open_help_btn = tk.Button(about_window,
                                  text = "Help",
                                  width = 10,
                                  height = 2,
                                  fg = "black",
                                  bg = "darkgrey",
                                  command = about_to_help)
        profile_btn = tk.Button(about_window,
                                text = "Profile",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "grey",
                                command = open_profile)
        exit_btn = tk.Button(about_window,
                         text = "Exit",
                         width = 10,
                         height = 2,
                         fg = "black",
                         bg = "grey",
                         command = exit_about)

        # Create window content.
        intro_label = tk.Label(about_window,
                               text = "Introduction: A budget is a "
                                    "generated spending plan based off your "
                                    "financial wants and needs. \nIt includes "
                                    "prioritizing and allocating various "
                                    "incomes, ensuring that all expenses "
                                    "are covered without spending more "
                                    "than what is earned. \nThrough this "
                                    "application, budgeting can provide "
                                    "clarity, preparedness and insights "
                                    "around finances, savings goals, and "
                                    "expensive emergencies. \nUltimately, "
                                    "budgeting improves financial stability.",
                                    justify = LEFT)
        about_lbl = tk.Label(about_window,
                             text = "What this programme does:\nThis "
                             + "programme aims to improve financial stability "
                             + "among New Zealand tertiary students aged "
                             + "18-25. This application offers \ninsights to "
                             + "your budget and helpful financial tips. You "
                             + "may be asking 'What do I have to do', the "
                             + "answer is basically nothing, \nyou've already "
                             + "created an account, now just enter your "
                             + "income, expenses, and lay back while the "
                             + "programme performs calculations and prepares "
                             + "your insights.",
                             justify = LEFT)
        process_lbl = tk.Label(about_window,
                               text = "The steps in this programme are as "
                               + "outlined below:\n\nStep 1: Record your "
                               + "income:\nOpen the budgeting page via the "
                               + "'My budget' button in the navigational bar "
                               + "or the 'Get started' button via the home "
                               + "page.\nChoose an income frequency, either "
                               + "weekly, fortnightly, four-weekly, monthly, "
                               + "or yearly. Now, simply enter your income "
                               + "and click the calculate income button.\n"
                               + "To save your input and continue, click the "
                               + "next button.\n\nStep 2: Choose an expense "
                               + "frequency and enter your expenses per the "
                               + "six different categories. Then click the "
                               + "calculate button and next to continue to "
                               + "insights.\n\nStep 3: See wether you got an "
                               + "income defict or surplus, then review your "
                               + "budget to make adjustments based off your "
                               + "insights.\n\nStep 4: See finanical tips to "
                               + "benefit from, this can be accessed via the "
                               + "'Tips' button in the navigational bar.\n\n"
                               + "Step 5: Enjoy the programme!!",
                               justify = LEFT)

        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        intro_label.place(x = 200, y = 250)
        about_lbl.place(x = 200, y = 350)
        process_lbl.place(x = 200, y = 450)
        canvas.place(x = 0, y = 20)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit_btn.place(x = 1110, y = 40)
        start_btn.place(x = 800, y = 290)

        about_window.mainloop()

    def home_to_help():
        """Function to take the user from home page to help page."""
        home_window.destroy()
        open_help_window()

    def home_to_income():
        """Function to take the user from home page to income page."""
        home_window.destroy()
        open_income_window()

    def home_to_about():
        """Function to take the user from home page to about page."""
        home_window.destroy()
        open_about_window()

    def about_to_help():
        """Function to take the user from about page to help page."""
        about_window.destroy()
        open_help_window()

    def about_to_income():
        """Function to take the user from about page to income page."""
        about_window.destroy()
        open_income_window()

    def help_to_income():
        """Function to take the user from help page to income page."""
        help_window.destroy()
        open_income_window()

    def insights_to_expenses():
        """Function to take the user from insights page to expenses 
        page.
        """
        insights_window.destroy()
        open_expenses_window()

    def insights_to_income():
        """Function to take the user from insights page to income 
        page.
        """
        insights_window.destroy()
        open_income_window()

    def help_to_about():
        """Function to take the user from help page to about page."""
        help_window.destroy()
        open_about_window()

    def income_to_help():
        """Function to take the user from income page to help page."""
        response = messagebox.askquestion("Exit Programme?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to exit the help page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(income_window,
                                command = income_window.quit)
            confirm_btn.pack()
            income_window.destroy()
            open_help_window()

    def income_to_about():
        """Function to take the user from income page to about page."""
        response = messagebox.askquestion("Exit income?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to exit the about page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(income_window,
                                command = income_window.quit)
            confirm_btn.pack()
            income_window.destroy()
            open_about_window()

    def expenses_to_income():
        """Function to take the user from expenses page to income 
        page.
        """
        expenses_window.destroy()
        open_income_window()

    def expenses_to_insights():
        """Function to take the user from expenses page to insights 
        page.
        """
        expenses_window.destroy()
        open_insights_window()

    def income_to_expenses():
        """Function to take the user from income page to expenses 
        page.
        """
        income_window.destroy()
        open_expenses_window()

    def expenses_to_about():
        """Function to take the user from expenses page to about 
        page.
        """
        response = messagebox.askquestion("Exit my income?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go about page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            expenses_window.destroy()
            open_about_window()

    def expenses_to_help():
        """Function to take the user from expenses page to help page."""
        response = messagebox.askquestion("Exit my income?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go about page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            expenses_window.destroy()
            open_help_window()

    def insights_to_about():
        """Function to take the user from insights page to about 
        page.
        """
        response = messagebox.askquestion("Exit my insights?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go about page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            insights_window.destroy()
            open_about_window()

    def insights_to_help():
        """Function to take the user from insights page to help page."""
        response = messagebox.askquestion("Exit my insights?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go help page?",
        icon = 'warning')
        print(response)
        if response == "yes":
            insights_window.destroy()
            open_help_window()

    # Create home page.
    global home_window
    home_window = tk.Tk()
    home_window.geometry("1200x750")
    home_window.title("Home")
    home_window.resizable(False, False)

    underlined_font = font.Font(size = 9, underline = True)

    # Create window content.
    program_title = tk.Label(home_window,
                             text = "Tertiary Budget \nTracker             ",
                             font = ("Helvetica", 48))
    canvas = Canvas(home_window,
                    height = 100,
                    width = 1210,
                    bg = "CadetBlue2")
    home_btn = tk.Button(home_window,
                         text = "Home",
                         font = underlined_font,
                         width = 10,
                         height = 2,
                         bg = "darkgrey")
    open_about_btn = tk.Button(home_window,
                               text = "About",
                               width = 10,
                               height = 2,
                               fg = "black",
                               bg = "darkgrey",
                               command = home_to_about)
    open_budget_btn = tk.Button(home_window,
                                text = "My Budget",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "darkgrey",
                                command = home_to_income)
    open_tips_btn = tk.Button(home_window,
                              text = "Tips",
                              width = 10,
                              height = 2,
                              fg = "black",
                              bg = "darkgrey",
                              command = tips_message)
    open_help_btn = tk.Button(home_window,
                              text = "Help",
                              width = 10,
                              height = 2,
                              fg = "black",
                              bg = "darkgrey",
                              command = home_to_help)
    start_btn = tk.Button(home_window,
                          text = "Get started!",
                          width = 15,
                          height = 2,
                          font = ("Helvetica", 20),
                          bg = "gold",
                          command = home_to_income)
    profile_btn = tk.Button(home_window,
                            text = "Profile",
                            width = 10,
                            height = 2,
                            fg = "black",
                            bg = "grey",
                            command = open_profile)
    exit_btn = tk.Button(home_window,
                     text = "Exit",
                     width = 10,
                     height = 2,
                     fg = "black",
                     bg = "grey",
                     command = popup)
    image = Image.open("budget_image.png")
    resize_image = image.resize((1200, 250))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(image = img)
    label1.image = img

    # Place labels, buttons, and images in a position.
    program_title.place(x = 200, y = 250)
    canvas.place(x = 0, y = 20)
    label1.place(x = 0, y = 450)
    home_btn.place(x = 50, y = 40)
    open_about_btn.place(x = 244, y = 40)
    open_budget_btn.place(x = 438, y = 40)
    open_tips_btn.place(x = 632, y = 40)
    open_help_btn.place(x = 826, y = 40)
    profile_btn.place(x = 1020, y = 40)
    exit_btn.place(x = 1110, y = 40)
    start_btn.place(x = 800, y = 290)

    home_window.mainloop()


def help_to_main():
    """Function to redirect user to the main code via help window."""
    help_window.destroy()
    open_main_code()


def income_to_main():
    """Function to redirect user to the main code via income window."""
    income_window.destroy()
    open_main_code()


def about_to_main():
    """Function to redirect user to the main code via about window."""
    about_window.destroy()
    open_main_code()


def expenses_to_main():
    """Function to redirect user to the main code via expenses 
    window.
    """
    response = messagebox.askquestion("Exit my expenses?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go home page?",
    icon = 'warning')
    print(response)
    if response == "yes":
        expenses_window.destroy()
        open_main_code()


def insights_to_main():
    """Function to redirect user to the main code via insights 
    window.
    """
    response = messagebox.askquestion("Exit my insights?","Your progress "
                                          "will NOT be saved.\nAre you sure "
                                          "you want to go home page?",
    icon = 'warning')
    print(response)
    if response == "yes":
        insights_window.destroy()
        open_main_code()

# Start the application.
open_first_window()
first_window = tk.Tk()
