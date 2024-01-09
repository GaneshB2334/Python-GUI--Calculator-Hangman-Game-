from tkinter import *

class Calculator():
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.config(background='Black')
        self.root.resizable(0,0)

        self.display = Label(root,fg='white',bg='black',width=16,height=2,padx=3)
        self.display.grid(column=0, row=0, columnspan=4, pady=(20,10), sticky='w')
        self.display.config(font=('Arial',30,'bold'))
        
        self.btn7 = Button(root,text='7',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(7))
        self.btn7.grid(column=0,row=1,pady=5,padx=5)
        self.btn7.config(font=('UBUNTU',14))

        self.btn8 = Button(root,text='8',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(8))
        self.btn8.grid(column=1,row=1,pady=5,padx=5)
        self.btn8.config(font=('UBUNTU',14))

        self.btn9 = Button(root,text='9',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(9))
        self.btn9.grid(column=2,row=1,pady=5,padx=5)
        self.btn9.config(font=('UBUNTU',14))

        self.btnplus = Button(root,text='+',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval('+'))
        self.btnplus.grid(column=3,row=1,pady=5,padx=5)
        self.btnplus.config(font=('UBUNTU',14))

        self.btn4 = Button(root,text='4',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(4))
        self.btn4.grid(column=0,row=2,pady=5,padx=5)
        self.btn4.config(font=('UBUNTU',14))

        self.btn5 = Button(root,text='5',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(5))
        self.btn5.grid(column=1,row=2,pady=5,padx=5)
        self.btn5.config(font=('UBUNTU',14))

        self.btn6 = Button(root,text='6',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(6))
        self.btn6.grid(column=2,row=2,pady=5,padx=5)
        self.btn6.config(font=('UBUNTU',14))

        self.btnmin = Button(root,text='-',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval('-'))
        self.btnmin.grid(column=3,row=2,pady=5,padx=5)
        self.btnmin.config(font=('UBUNTU',14))

        self.btn1 = Button(root,text='1',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(1))
        self.btn1.grid(column=0,row=3)
        self.btn1.config(font=('UBUNTU',14))

        self.btn2 = Button(root,text='2',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(2))
        self.btn2.grid(column=1,row=3)
        self.btn2.config(font=('UBUNTU',14))

        self.btn3 = Button(root,text='3',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval(3))
        self.btn3.grid(column=2,row=3,pady=5,padx=5)
        self.btn3.config(font=('UBUNTU',14))

        self.btnmul = Button(root,text='*',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval('*'))
        self.btnmul.grid(column=3,row=3,pady=5,padx=5)
        self.btnmul.config(font=('UBUNTU',14))

        self.btndiv = Button(root,text='/',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval('/'))
        self.btndiv.grid(column=3,row=4,pady=5,padx=5)
        self.btndiv.config(font=('UBUNTU',14))

        self.btn0 = Button(root,text='0',fg='white',bg='gray',width=5,height=3,command=lambda : self.getval('0'))
        self.btn0.grid(column=1,row=4,pady=5,padx=5)
        self.btn0.config(font=('UBUNTU',14))

        self.btnequal = Button(root,text='=',fg='white',bg='gray',width=5,height=3,command=lambda : self.get_result())
        self.btnequal.grid(column=2,row=4,pady=5,padx=5)
        self.btnequal.config(font=('UBUNTU',14))

        self.btnc = Button(root,text='C',fg='white',bg='gray',width=5,height=3,command=lambda : self.clear())
        self.btnc.grid(column=0,row=4,pady=5,padx=5)
        self.btnc.config(font=('UBUNTU',14))
        self.expression = ""

    def getval(self,digit):
        self.expression += str(digit)
        self.display.config(text=self.expression)

    def get_result(self):
        try:
            result = eval(self.expression)
            self.display.config(text=str(result))
        except:
            self.display.config(text="Error")

    def clear(self):
        self.expression = ''
        self.display.config(text='')
        
if __name__ == "__main__":
    root = Tk()
    calcy = Calculator(root)
    root.mainloop()
