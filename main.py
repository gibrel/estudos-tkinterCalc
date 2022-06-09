import math
from tkinter import *


def clear_trailing(number):
    return ('%f' % number).rstrip('0').rstrip('.')


class Calc:

    num_memory = 0

    def __init__(self):
        self.window = Tk()
        self.window.title("Tkinter Calc")
        self.window.resizable(False, False)
        self.window.config(bg="#1d2f38")

        self.frame_screen = Frame(self.window, bg="#1d2f38")
        self.frame_screen.pack(anchor="e")

        self.screen_operation = Label(self.frame_screen, font="Arial 30 bold", bg="#1d2f38", fg="white", height=1,
                                      width=16, justify=RIGHT, anchor="e")
        self.screen_operation.pack()

        self.screen_numbers = Entry(self.frame_screen, font="Arial 30 bold", bg="#1d2f38", fg="white", width=20,
                                    justify=RIGHT)
        self.screen_numbers.pack(anchor="e")

        self.frame = Frame(self.window, bg="orange")
        self.frame.pack()

        self.button_factorial = Button(self.frame, bg="orange", bd=0, text="!", font="Arial 20 bold",
                                       fg="white", width=5, height=2, command=self.factorial_operator)
        self.button_clear_current = Button(self.frame, bg="orange", bd=0, text="Œ", font="Arial 20 bold",
                                           fg="white", width=5, height=2, command=self.clear_screen)
        self.button_clear_all = Button(self.frame, bg="orange", bd=0, text="C", font="Arial 20 bold",
                                       fg="white", width=5, height=2, command=self.clear_all)
        self.button_backspace = Button(self.frame, bg="orange", bd=0, text="«═", font="Arial 20 bold",
                                       fg="white", width=10, height=2, command=self.clear_last)

        self.button_inverse = Button(self.frame, bg="orange", bd=0, text="¹/x", font="Arial 20 bold",
                                     fg="white", width=5, height=2, command=self.invert_operator)
        self.button_square = Button(self.frame, bg="orange", bd=0, text="x²", font="Arial 20 bold",
                                    fg="white", width=5, height=2, command=self.square_operator)
        self.button_square_root = Button(self.frame, bg="orange", bd=0, text="²√", font="Arial 20 bold",
                                         fg="white", width=5, height=2, command=self.square_root_operator)
        self.button_division = Button(self.frame, bg="orange", bd=0, text="÷", font="Arial 20 bold",
                                      fg="white", width=5, height=2, command=lambda: self.prepare_operation("/"))
        self.button_memory_clear = Button(self.frame, bg="orange", bd=0, text="MC", font="Arial 20 bold",
                                          fg="white", width=5, height=2, command=self.clear_mem)

        self.button_7 = Button(self.frame, bg="orange", bd=0, text="7", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("7"))
        self.button_8 = Button(self.frame, bg="orange", bd=0, text="8", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("8"))
        self.button_9 = Button(self.frame, bg="orange", bd=0, text="9", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("9"))
        self.button_times = Button(self.frame, bg="orange", bd=0, text="×", font="Arial 20 bold",
                                   fg="white", width=5, height=2, command=lambda: self.prepare_operation("*"))
        self.button_memory_recall = Button(self.frame, bg="orange", bd=0, text="MR", font="Arial 20 bold",
                                           fg="white", width=5, height=2, command=self.recall_mem)

        self.button_4 = Button(self.frame, bg="orange", bd=0, text="4", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("4"))
        self.button_5 = Button(self.frame, bg="orange", bd=0, text="5", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("5"))
        self.button_6 = Button(self.frame, bg="orange", bd=0, text="6", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("6"))
        self.button_minus = Button(self.frame, bg="orange", bd=0, text="-", font="Arial 20 bold",
                                   fg="white", width=5, height=2, command=lambda: self.prepare_operation("-"))
        self.button_memory_add = Button(self.frame, bg="orange", bd=0, text="M+", font="Arial 20 bold",
                                        fg="white", width=5, height=2, command=self.add_mem)

        self.button_1 = Button(self.frame, bg="orange", bd=0, text="1", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("1"))
        self.button_2 = Button(self.frame, bg="orange", bd=0, text="2", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("2"))
        self.button_3 = Button(self.frame, bg="orange", bd=0, text="3", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("3"))
        self.button_plus = Button(self.frame, bg="orange", bd=0, text="+", font="Arial 20 bold",
                                  fg="white", width=5, height=2, command=lambda: self.prepare_operation("+"))
        self.button_memory_subtract = Button(self.frame, bg="orange", bd=0, text="M-", font="Arial 20 bold",
                                             fg="white", width=5, height=2, command=self.subtract_mem)

        self.button_PM = Button(self.frame, bg="orange", bd=0, text="±", font="Arial 20 bold",
                                fg="white", width=5, height=2, command=self.change_signal)
        self.button_0 = Button(self.frame, bg="orange", bd=0, text="0", font="Arial 20 bold",
                               fg="white", width=5, height=2, command=lambda: self.touch("0"))
        self.button_dot = Button(self.frame, bg="orange", bd=0, text=".", font="Arial 20 bold",
                                 fg="white", width=5, height=2, command=lambda: self.touch("."))
        self.button_equal = Button(self.frame, bg="orange", bd=0, text="=", font="Arial 20 bold",
                                   fg="white", width=10, height=2, command=self.execute_operation)

        self.button_factorial.grid(row=0, column=0)
        self.button_clear_current.grid(row=0, column=1)
        self.button_clear_all.grid(row=0, column=2)
        self.button_backspace.grid(row=0, column=3, columnspan=2)

        self.button_inverse.grid(row=1, column=0)
        self.button_square.grid(row=1, column=1)
        self.button_square_root.grid(row=1, column=2)
        self.button_division.grid(row=1, column=3)
        self.button_memory_clear.grid(row=1, column=4)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_times.grid(row=2, column=3)
        self.button_memory_recall.grid(row=2, column=4)

        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        self.button_minus.grid(row=3, column=3)
        self.button_memory_add.grid(row=3, column=4)

        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)
        self.button_3.grid(row=4, column=2)
        self.button_plus.grid(row=4, column=3)
        self.button_memory_subtract.grid(row=4, column=4)

        self.button_PM.grid(row=5, column=0)
        self.button_0.grid(row=5, column=1)
        self.button_dot.grid(row=5, column=2)
        self.button_equal.grid(row=5, column=3, columnspan=2)

        self.clear_screen()

        self.window.mainloop()

    def touch(self, num):
        if num != ".":
            input_num = float(num)
            value = self.get_number_from_screen()
            if value == 0 and len(self.screen_numbers.get()) == 1:
                self.screen_numbers.delete(0, END)
                if input_num == 0:
                    self.screen_numbers.insert(0, "0")
                else:
                    self.screen_numbers.insert(END, num)
            else:
                self.screen_numbers.insert(END, num)
        else:
            self.screen_numbers.insert(END, num)

    def clear_all(self):
        self.screen_operation.config(text="")
        self.clear_screen()

    def clear_screen(self):
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, "0")

    def clear_last(self):
        position = len(self.screen_numbers.get()) - 1
        if position > 0:
            self.screen_numbers.delete(position, END)
        else:
            self.clear_screen()

    def prepare_operation(self, operator):
        value = self.get_number_from_screen()
        if operator == "+":
            self.screen_operation.config(text="{} +".format(str(value)))
        elif operator == "-":
            self.screen_operation.config(text="{} -".format(str(value)))
        elif operator == "*":
            self.screen_operation.config(text="{} *".format(str(value)))
        elif operator == "/":
            self.screen_operation.config(text="{} /".format(str(value)))
        self.clear_screen()

    def execute_operation(self):
        operation_screen = self.screen_operation.cget("text")
        if len(operation_screen) > 2:
            value = self.get_number_from_screen()
            operation = "{} {}".format(operation_screen, str(value))
            result = eval(operation)
            self.screen_numbers.delete(0, END)
            self.set_number_on_screen(result)
            self.screen_operation.config(text=str(""))

    def change_signal(self):
        value = self.get_number_from_screen()
        if value != 0:
            self.screen_numbers.delete(0, END)
            self.set_number_on_screen(value * (-1))

    def clear_mem(self):
        self.num_memory = 0

    def add_mem(self):
        self.num_memory += self.get_number_from_screen()

    def subtract_mem(self):
        self.num_memory -= self.get_number_from_screen()

    def recall_mem(self):
        self.set_number_on_screen(self.num_memory)

    def get_number_from_screen(self):
        try:
            value = float(self.screen_numbers.get())
        except ValueError:
            print("ValueError => {}".format(self.screen_numbers.get()))
            value = 0
        return value

    def set_number_on_screen(self, number):
        num_string = clear_trailing(number)
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, num_string)

    def invert_operator(self):
        value = self.get_number_from_screen()
        self.set_number_on_screen(1 / value)

    def square_operator(self):
        value = self.get_number_from_screen()
        self.set_number_on_screen(value*value)

    def square_root_operator(self):
        value = self.get_number_from_screen()
        self.set_number_on_screen(math.sqrt(value))

    def factorial_operator(self):
        try:
            value = int(self.screen_numbers.get())
            self.set_number_on_screen(math.factorial(value))
        except ValueError:
            pass


Calc()
