from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('400x500+100+100')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget
        self.entry = Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation, bd=5, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=5, pady=10)

        # Button layout (row, column)
        buttons = [
            ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('C', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('⌫', 6, 0),  # Backspace
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = Button(master, text=text, width=10, height=3, bg='lightgreen', command=self.solve)
            elif text == 'C':
                btn = Button(master, text=text, width=10, height=3, bg='salmon', command=self.clear)
            elif text == '⌫':
                btn = Button(master, text=text, width=43, height=3, bg='lightgray', command=self.backspace)
                btn.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
                continue
            else:
                btn = Button(master, text=text, width=10, height=3, command=lambda t=text: self.show(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            expression = self.entry_value.replace('%', '/100')
            result = eval(expression)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
