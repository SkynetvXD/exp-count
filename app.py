import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Tempo restante para se tornar mestre: 00:00:00", width=50)
        self.button = tk.Button(self, text="Count", command=self.countdown, width=10)
        '''self.button1 = tk.Button(self, text="Save", command=self.save, width=10)'''
        self.label.pack()
        self.button.pack()
        '''self.button1.pack()'''
        self.s = 0
        self.m = 0
        self.h = 0

    def countdown(self):
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
            self.label.configure(text="Tempo restante para se tornar mestre: 0{}:0{}:0{}"
                                 .format(self.h, self.m, self.s))
            if self.s >= 10:
                self.label.configure(text="Tempo restante para se tornar mestre: 0{}:0{}:{}"
                                     .format(self.h, self.m, self.s))
            self.s = self.s + 1
            self.after(1000, self.countdown)
    '''def save (self):'''

if __name__ == "__main__":
    app = ExampleApp()
    app.title("Experience Count")
    app.mainloop()