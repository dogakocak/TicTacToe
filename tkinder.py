from tkinter import *
import tkinter.messagebox

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = '0'
computer = 'X'
computerCanPlay = True
root = Tk()
root.iconbitmap("favicon.ico")
root.title("Tic Tac Toe - Doğa Koçak")

root.resizable(False, False)

click = True

count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file='X.png')
oPhoto = PhotoImage(file='O.png')

button1 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#dd8ce3', textvariable=btn1,
                 command=lambda: press(1, 0, 0, True))
button2 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#dd8ce3', textvariable=btn2,
                 command=lambda: press(2, 0, 1, True))
button3 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#dd8ce3', textvariable=btn3,
                 command=lambda: press(3, 0, 2, True))
button4 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#c247cb', textvariable=btn4,
                 command=lambda: press(4, 1, 0, True))
button5 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#c247cb', textvariable=btn5,
                 command=lambda: press(5, 1, 1, True))
button6 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#c247cb', textvariable=btn6,
                 command=lambda: press(6, 1, 2, True))
button7 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#931e9b', textvariable=btn7,
                 command=lambda: press(7, 2, 0, True))
button8 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#931e9b', textvariable=btn8,
                 command=lambda: press(8, 2, 1, True))
button9 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#931e9b', textvariable=btn9,
                 command=lambda: press(9, 2, 2, True))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)



def press(num, r, c, human):
    global click, count
    if human:
        labelPhoto = Label(root, image=oPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('O')
            insLetter('O', 1)
            computerMove()
        if num == 2:
            btn2.set('O')
            insLetter('O', 2)
            computerMove()
        if num == 3:
            btn3.set('O')
            insLetter('O', 3)
            computerMove()
        if num == 4:
            btn4.set('O')
            insLetter('O', 4)
            computerMove()
        if num == 5:
            btn5.set('O')
            insLetter('O', 5)
            computerMove()
        if num == 6:
            btn6.set('O')
            insLetter('O', 6)
            computerMove()
        if num == 7:
            btn7.set('O')
            insLetter('O', 7)
            computerMove()
        if num == 8:
            btn8.set('O')
            insLetter('O', 8)
            computerMove()
        if num == 9:
            btn9.set('O')
            insLetter('O', 9)
            computerMove()
    else:
        print("Bot is playing")
        labelPhoto = Label(root, image=xPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('X')
            insLetter('X', 1)
        if num == 2:
            btn2.set('X')
            insLetter('X', 2)
        if num == 3:
            btn3.set('X')
            insLetter('X', 3)
        if num == 4:
            btn4.set('X')
            insLetter('X', 4)
        if num == 5:
            btn5.set('X')
            insLetter('X', 5)
        if num == 6:
            btn6.set('X')
            insLetter('X', 6)
        if num == 7:
            btn7.set('X')
            insLetter('X', 7)
        if num == 8:
            btn8.set('X')
            insLetter('X', 8)
        if num == 9:
            btn9.set('X')
            insLetter('X', 9)
        count += 1





def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insLetter(letter, position):
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    row = 0
    col = 0
    if spaceIsFree(position):
        buttons[position - 1].set(letter)
        if(letter == 'X'):
            if(position == 2):
                row = 0
                col = 1
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 3):
                row = 0
                col = 2
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 4):
                row = 1
                col = 0
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 5):
                row = 1
                col = 1
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 6):
                row = 1
                col = 2
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 7):
                row = 2
                col = 0
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 8):
                row = 2
                col = 1
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

            if (position == 9):
                row = 2
                col = 2
            labelPhoto = Label(root, image=xPhoto)
            labelPhoto.grid(row=row, column=col)

        board[position] = letter
        if checkDraw():
            print("Draw!")

        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                tkinter.messagebox.showinfo(title="Bot wins!", message="You lose ha ha :)")
                exit()
            else:
                print("Player wins!")
                tkinter.messagebox.showinfo(title="You win!", message="Congratulations!")
                exit()

            return


def checkWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[4] == board[1] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def computerMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    press(bestMove,0,0,False)
    return


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[4] == board[1] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


computerMove()
root.mainloop()