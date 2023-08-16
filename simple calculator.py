from tkinter import *

root = Tk()
root.title("Simple Calculator")


terminal = Entry(root, width=60, borderwidth=5)
terminal.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = terminal.get()
    terminal.delete(0,END)
    terminal.insert(0,str(current) + str(number))

def button_clear():
    terminal.delete(0,END)

def button_add():
    first_number = terminal.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    terminal.delete(0,END)
    
def button_subtract():
    first_number = terminal.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    terminal.delete(0,END)

def button_multiply():
    first_number = terminal.get()
    global f_num
    global math
    math = "mulitplication"
    f_num = int(first_number)
    terminal.delete(0,END)


def button_divide():
    first_number = terminal.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    terminal.delete(0,END)
    

def button_equal():
    second_number = terminal.get()
    terminal.delete(0,END)
    if math == "addition":
        terminal.insert(0, f_num + int(second_number))
    if math == "subtraction":
        terminal.insert(0, f_num - int(second_number))
    if math == "mulitplication":
        terminal.insert(0, f_num * int(second_number))
    if math == "division":
        terminal.insert(0, f_num / int(second_number))
    else:
        return "invalid"
    


    
            

button_1 = Button(root, text="1", padx =40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx =40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx =40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx =40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx =40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx =40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx =40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx =40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx =40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx =40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx =39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx =39, pady=20, command=button_subtract)
button_mulitply = Button(root, text="*", padx =39, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx =39, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx =40, pady=20, command=button_equal, bg = "green")
button_clear = Button(root, text="C", padx =40, pady=20, command=button_clear, bg = "red")



button_1.grid(row=3,column=0,sticky="nsew")
button_2.grid(row=3,column=1,sticky="nsew")
button_3.grid(row=3,column=2,sticky="nsew")

button_4.grid(row=2,column=0,sticky="nsew")
button_5.grid(row=2,column=1,sticky="nsew")
button_6.grid(row=2,column=2,sticky="nsew")

button_7.grid(row=1,column=0,sticky="nsew")
button_8.grid(row=1,column=1,sticky="nsew")
button_9.grid(row=1,column=2,sticky="nsew")

button_0.grid(row=4,column=0,sticky="nsew")

button_add.grid(row=1,column=3,sticky="nsew")
button_subtract.grid(row=2,column=3,sticky="nsew")
button_mulitply.grid(row=3,column=3,sticky="nsew")
button_divide.grid(row=4,column=3,sticky="nsew")
button_clear.grid(row=4,column=1,sticky="nsew")
button_equal.grid(row=4,column=2,sticky="nsew")

                
root.mainloop()
