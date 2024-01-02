from tkinter import *

window = Tk()
window.title("Tic Tac Toe")
window.geometry("650x900")
window.configure(bg='grey')

cells = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
win = -1
turn = 0

def check():
    global win
    global cells
    if cells[0][0] == cells[0][1] and cells[0][0] == cells[0][2] and not cells[0][0] == -1:
        win = cells[0][0]
    elif cells[1][0] == cells[1][1] and cells[1][0] == cells[1][2] and not cells[1][0] == -1:
        win = cells[1][0]
    elif cells[2][0] == cells[2][1] and cells[2][0] == cells[2][2] and not cells[2][0] == -1:
        win = cells[2][0]
    elif cells[0][0] == cells[1][0] and cells[0][0] == cells[2][0] and not cells[0][0] == -1:
        win = cells[0][0]
    elif cells[0][1] == cells[1][1] and cells[0][1] == cells[2][1] and not cells[0][1] == -1:
        win = cells[0][1]
    elif cells[0][2] == cells[1][2] and cells[0][2] == cells[2][2] and not cells[0][2] == -1:
        win = cells[0][2]
    elif cells[0][0] == cells[1][1] and cells[0][0] == cells[2][2] and not cells[0][0] == -1:
        win = cells[0][0]
    elif cells[0][2] == cells[1][1] and cells[0][2] == cells[2][0] and not cells[0][2] == -1:
        win = cells[0][2]
    else:
        win =- 1

def place(r,c):
    global cells
    global turn
    global window
    global labels_s
    if cells[r][c] == -1:
        cells[r][c] = turn
        labels_s[r][c].set(f"{'X' if turn == 0 else 'O'}")
        check()
        if win == 1:
            textVar.set(f"O Wins!")
        elif win == 0:
            textVar.set(f"X Wins!")
        else:
            if cells[0].count(0)+cells[1].count(0)+cells[2].count(0) == 5:
                textVar.set(f"Game Drawn!")
            else:
                turn = 1 if turn == 0 else 0
                textVar.set(f"{'X' if turn == 0 else 'O'}'s Turn")

textVar = StringVar()
textVar.set(f"{'X' if turn == 0 else 'O'}'s Turn")
turnLabel = Label(window, textvariable=textVar, bg='grey', fg='white', font='Courier 45').place(x = 200, y = 50)

cell1 = Button(window, command = lambda: place(0,0), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 20, y=250)
l1_s = StringVar()
label1 = Label(window, textvariable = l1_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=70,y=285)

cell2 = Button(window, command = lambda: place(0,1), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 240, y=250)
l2_s = StringVar()
label2 = Label(window, textvariable = l2_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=290,y=285)

cell3 = Button(window, command = lambda: place(0,2), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 460, y=250)
l3_s = StringVar()
label3 = Label(window, textvariable = l3_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=510,y=285)

cell4 = Button(window, command = lambda: place(1,0), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 20, y=470)
l4_s = StringVar()
label4 = Label(window, textvariable = l4_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=70,y=505)

cell5 = Button(window, command = lambda: place(1,1), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 240, y=470)
l5_s = StringVar()
label5 = Label(window, textvariable = l5_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=290,y=505)

cell6 = Button(window, command = lambda: place(1,2), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 460, y=470)
l6_s = StringVar()
label6 = Label(window, textvariable = l6_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=510,y=505)

cell7 = Button(window, command = lambda: place(2,0), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 20, y=690)
l7_s = StringVar()
label7 = Label(window, textvariable = l7_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=70,y=725)

cell8 = Button(window, command = lambda: place(2,1), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 240, y=690)
l8_s = StringVar()
label8 = Label(window, textvariable = l8_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=290,y=725)

cell9 = Button(window, command = lambda: place(2,2), bg = 'lightgrey',bd=10, width=21,height=10).place(x = 460, y=690)
l9_s = StringVar()
label9 = Label(window, textvariable = l9_s, font="Helvetica 70",bg='lightgrey',fg='blue').place(x=510,y=725)

labels_s = [[l1_s,l2_s,l3_s],[l4_s,l5_s,l6_s],[l7_s,l8_s,l9_s]]

window.mainloop()