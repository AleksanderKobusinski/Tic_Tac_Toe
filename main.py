from tkinter import *
from tkinter import messagebox


def messageWindow(root):
    top = Toplevel()
    top.lift(root)
    top.title('Players')
    top.geometry('225x100')
    top.config(padx=50, pady=10)
    message = "How many players?"
    askQuestion = Label(top, text=message)
    askQuestion.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
    button1 = Button(top, text='1 player', state="disabled")
    button1.grid(column=0, row=1, padx=5, pady=5)
    button2 = Button(top, text='2 players', command=top.destroy)
    button2.grid(column=1, row=1, padx=5, pady=5)


def check_end(state):
    global round
    for i in range(3):
        if state[i*3] == state[i*3+1] == state[i*3+2] and state[i*3]!=" ":
            return 0
        if state[i] == state[i+3] == state[i+6] and state[i]!=" ":
            return 0
    if state[0] == state[4] == state[8] and state[4]!=" ":
        return 0
    if state[2] == state[4] == state[6] and state[4]!=" ":
        return 0
    if round == 10:
        round += 1
        return 0
    return 1


def button_clicked(number):
    global round
    global state
    global buttons
    if round%2==1:
        buttons[number].config(text="X", state="disabled")
        state[number]='X'
    else:
        buttons[number].config(text="O", state="disabled")
        state[number]='O'
    round+=1
    if check_end(state)==0:
        for button in buttons:
            button.config(state="disabled")
        if round==11:
            messagebox.showinfo(title="Draw!", message="Draw!")
        else:
            if round%2==0:
                messagebox.showinfo(title="Winner!", message="Player X is a winner!")
            else:
                messagebox.showinfo(title="Winner!", message="Player O is a winner!")

window = Tk()
window.title("Tic Tac Toe")

buttons=[]
row=0
column=0
state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
round = 1

messageWindow(window) 

for i in range(9):
    buttons.append(Button(text=" ",command=lambda i=i:button_clicked(i), padx=5, pady=5, font=("Helvetica", 15, "bold"), width=5, height=3))
    buttons[i].grid(column=column, row=row, padx=5, pady=5)
    column=(column+1)%3
    if column==0:
        row+=1

window.mainloop()