import Tkinter
import random


class Square:
    def __init__(self, x, y, bomb):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.button = None

    def set_button(self, button):
        self.button = button


class Field:
    def __init__(self):
        pass

    @staticmethod
    def generate(w, h, bombcount):
        area = []
        for y in range(0, h):
            row = []
            for x in range(0, w):
                bomb = (random.randint(0, (w*h/bombcount)) == 1)
                s = Square(x, y, bomb)
                button = Tkinter.Button(top, text="", command=lambda: button_callback(s)).grid(row=x, column=y)
                s.set_button(button)
                row.append(s)
            area.append(row)
        return area


top = Tkinter.Tk()


def button_callback(square):
    print("test: " + str(square.x) + str(square.y))


f = Field()
f.generate(20, 20, 5)

top.mainloop()
