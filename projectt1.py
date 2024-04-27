import tkinter as tk
from tkinter import messagebox
from PyBrowser import PyBrowser # type: ignore

class PyBrowserUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PyBrowser")
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self.master, text="URL:")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(self.master, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2)

        self.method_label = tk.Label(self.master, text="Method:")
        self.method_label.grid(row=1, column=0)
        self.method_var = tk.StringVar()
        self.method_var.set("GET")
        self.method_option = tk.OptionMenu(self.master, self.method_var, "GET", "POST")
        self.method_option.grid(row=1, column=1)

        self.send_button = tk.Button(self.master, text="Send Request", command=self.send_request)
        self.send_button.grid(row=2, column=1)

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()
        browser = PyBrowser()
        response = browser.send_request(method, url)
        messagebox.showinfo("Response", f"Status Code: {response.status_code}\nResponse Body: {response.text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PyBrowserUI(root)
    root.mainloop()


