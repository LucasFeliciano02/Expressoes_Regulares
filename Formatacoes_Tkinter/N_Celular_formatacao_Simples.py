from tkinter import *


# *  22 99432-4234
def format_tel(event=None):

    text = entry.get().replace(".", "").replace("-", "")[:12]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

        if not text[index] in "0123456789":
            continue
        if index in [1, 2]:
            new_text += text[index] + " "
        elif index == 7:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry.delete(0, "end")
    entry.insert(0, new_text)


screen = Tk()

entry = Entry(screen, font=("Arial", 20))
entry.bind("<KeyRelease>", format_tel)
entry.pack()
screen.mainloop()
