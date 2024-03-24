import tkinter as tk
from tkinter import filedialog, ttk
from utils import Manager
import sv_ttk

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.manager = Manager(proxy=None)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Twitter Follow Bot", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        self.username_label = ttk.Label(self, text="Usernames to follow (separator: ', ')")
        self.username_label.grid(row=1, column=0, padx=5, pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self, text=f"Amount (max: {len(self.manager.accounts)})")
        self.amount_label.grid(row=2, column=0, padx=5, pady=5)

        vcmd = (self.register(self.validate), '%P')
        self.amount_entry = ttk.Entry(self, validate='key', validatecommand=vcmd)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        self.log_text = tk.Text(self, height=12, state='disabled')  # ttk does not have a Text widget
        self.log_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.follow_button = ttk.Button(self, text="Follow", command=self.follow)
        self.follow_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            return True
        try:
            value = int(new_text)
            if 1 <= value <= 100:  # check if the value is in the range
                return True
            else:
                return False
        except ValueError:
            return False

    def follow(self):
        usernames = self.username_entry.get().split(', ')
        amount = int(self.amount_entry.get())
        for username in usernames:
            self.log_text.config(state='normal')  # enable the widget
            self.log_text.insert('end', f'Following {username}...\n')
            self.log_text.config(state='disabled')  # disable the widget
            self.update()
            accounts = {}
            for i in range(amount):
                from random import sample
                s = sample(sorted(self.manager.secrets), amount)
                accounts = {k: self.manager.secrets[k] for k in s}
            for account in self.manager.accounts.values():
                self.log_text.config(state='normal')
                self.log_text.insert('end', self.manager.follow_with_account(account, username))
                self.log_text.config(state='disabled')
            self.log_text.config(state='normal')  # enable the widget
            self.log_text.insert('end', f'Finished following {username}.\n')
            self.log_text.config(state='disabled')  # disable the widget
            self.update()

root = tk.Tk()
root.geometry("400x700")
root.minsize(700, 400)
root.maxsize(700, 400)
sv_ttk.set_theme("dark")
app = Application(master=root)
app.mainloop()