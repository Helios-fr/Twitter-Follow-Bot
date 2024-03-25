import tkinter as tk
from tkinter import filedialog, ttk
from utils import Manager

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.proxies = []
        self.use_proxies = tk.BooleanVar()
        self.create_widgets()
        # add text to the log
        self.log_text.config(state='normal')
        self.log_text.insert('end', "Welcome, Application Logs will appear here during execution\n")
        self.log_text.config(state='disabled')

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Twitter Follow Bot", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        self.username_label = ttk.Label(self, text="Usernames to follow (separator: ', ')")
        self.username_label.grid(row=1, column=0, padx=5, pady=5)

        self.username_entry = ttk.Entry(self, width=50)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self, text=f"Amount (max: {len(Manager().accounts)})")
        self.amount_label.grid(row=2, column=0, padx=5, pady=5)

        vcmd = (self.register(self.validate), '%P')
        self.amount_entry = ttk.Entry(self, validate='key', style='Accent.TEntry', validatecommand=vcmd, width=50)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        self.proxy_checkbutton = ttk.Checkbutton(self, text="Use proxy", variable=self.use_proxies)
        self.proxy_checkbutton.grid(row=3, column=0, padx=5, pady=5)

        self.proxy_entry = ttk.Entry(self, width=50)
        self.proxy_entry.grid(row=3, column=1, padx=5, pady=5)

        self.log_text = tk.Text(self, height=12, state='disabled')  # ttk does not have a Text widget
        self.log_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.follow_button = ttk.Button(self, text="Follow", command=self.follow)
        self.follow_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def load_proxies(self):
        filename = filedialog.askopenfilename()
        with open(filename, 'r') as f:
            self.proxies = f.read().splitlines()

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
        if self.use_proxies.get():
            self.manager = Manager(proxy={'http://': f"http://{self.proxy_entry.get()}", 'https://': f"http://{self.proxy_entry.get()}"})
        else:
            self.manager = Manager(proxy=None)

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
        
        self.log_text.config(state='normal')  # enable the widget
        self.log_text.insert('end', 'Finished following all users.\n')
        self.log_text.config(state='disabled')

root = tk.Tk()
root.geometry("400x700")
root.minsize(700, 450)
root.maxsize(700, 450)
root.title("Twitter Follow Bot by @qHelios")
root.iconbitmap("icon.ico")
root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')
app = Application(master=root)
app.mainloop()