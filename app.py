import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=50)
        self.button = tk.Button(self, text="Count", width = 10)
        self.label.pack()
        self.button.pack()
        self.s = 0
        self.m = 0
        self.h = 0
        self.countdown(0)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.s = remaining
        if self.s == 59:
            self.label.configure(text="{}:{}:{}".format(self.h, self.m, self.s))
            self.m = self.m + 1
            self.s = 0
            self.after(1000, self.countdown)
        if self.m == 59:
            self.label.configure(text="{}:{}:{}".format(self.h, self.m, self.s))
            self.h = self.h + 1
            self.m = 0
            self.after(1000, self.countdown)
        else:
            self.label.configure(text="Tempo restante para se tornar mestre: {}:{}:{}".format(self.h, self.m, self.s))
            self.s = self.s + 1
            self.after(1000, self.countdown)


if __name__ == "__main__":
    app = ExampleApp()
    app.title("Experience Count")
    app.mainloop()