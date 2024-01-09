from tkinter import *

class Calculator():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.config(background='black')
        self.root.resizable(0, 0)

        self.display = Label(root, fg='white', bg='black', width=16, height=2)
        self.display.grid(column=0, row=0, columnspan=4, pady=(20, 10), sticky='w')
        self.display.config(font=('Arial', 20, 'bold'))

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '=', '/'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = Button(root, text=button, fg='white', bg='gray', width=5, height=2, command=lambda: self.get_result())
            elif button == 'C':
                btn = Button(root, text=button, fg='white', bg='gray', width=5, height=2, command=lambda: self.clear())
            else:
                btn = Button(root, text=button, fg='white', bg='gray', width=5, height=2, command=lambda b=button: self.getnum(b))

            btn.grid(column=col_val, row=row_val, pady=5, padx=5)
            btn.config(font=('Ubuntu', 14))

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.expression = ""

    def getnum(self, digit):
        self.expression += str(digit)
        self.display.config(text=self.expression)

    def get_result(self):
        try:
            result = eval(self.expression)
            self.display.config(text=str(result))
        except:
            self.display.config(text="Error")

    def clear(self):
        self.expression = ""
        self.display.config(text="")


if __name__ == "__main__":
    root = Tk()
    calcy = Calculator(root)
    root.mainloop()
