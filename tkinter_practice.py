#! python3

import tkinter 

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "What's up?\n(Click my button!)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="green",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.fav_color = tkinter.Button(self, text="What's your favorite color?", fg="white", bg="black", command=self.favorite_color)
        self.fav_color.pack(side="top")
        

    def say_hi(self):
        print("Hello there terminal friend!")
        
    def favorite_color(self):
        print("Well, my favorite color is Red.")

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
