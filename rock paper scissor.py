from tkinter import *
import random
import pygame


root = Tk()
root.title("Game")
root.geometry("900x700")
root.config(bg="white")
root.resizable(False, False)

global com_score
global play_score

com_score = 0
play_score = 0

list = [101, 202, 303]

pygame.mixer.init()

# 101 = paper
# 202 = rock
# 303 = scissor


global p1
global p2
global p3

global l1
global l2
global l3

global cl1
global cl2
global cl3

global cp1
global cp2
global cp3


def paper():
    global l1
    global p1
    global cl1
    global cl2
    global cl3
    global cp1
    global cp2
    global cp3
    global com_score
    global play_score


    p1 = PhotoImage(file='paper.png')
    l1 = Label(frame, image=p1, height=300, width=300).place(x=550, y=60)

    pygame.mixer.music.load("beepwrong.mp3")
    pygame.mixer.music.play()

    num = random.choice(list)

    if num == 101:
        cp1 = PhotoImage(file='paper.png')
        cl1 = Label(frame, image=cp1, height=300, width=300).place(x=40, y=60)

        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()


    elif num == 202:
        cp2 = PhotoImage(file='rock.png')
        cl2 = Label(frame, image=cp2, height=300, width=300).place(x=40, y=60)

        play_score = play_score + 1
        Label(frame, text=play_score, font=("calibri", 15), bg="grey").place(x=775, y=20)
        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()


    elif num == 303:
        cp3 = PhotoImage(file='scissor.png')
        cl3 = Label(frame, image=cp3, height=300, width=300).place(x=40, y=60)

        com_score = com_score + 1
        Label(frame, text=com_score, font=("calibri", 15), bg="grey").place(x=245, y=20)
        pygame.mixer.music.load("beepwrong.mp3")
        pygame.mixer.music.play()


def rock():
    global p2
    global l2
    global cl1
    global cl2
    global cl3
    global cp1
    global cp2
    global cp3
    global com_score
    global play_score


    p2 = PhotoImage(file='rock.png')
    l2 = Label(frame, image=p2, height=300, width=300).place(x=550, y=60)



    num = random.choice(list)

    if num == 101:
        cp1 = PhotoImage(file='paper.png')
        cl1 = Label(frame, image=cp1, height=300, width=300).place(x=40, y=60)

        com_score = com_score + 1
        Label(frame, text=com_score, font=("calibri", 15), bg="grey").place(x=245, y=20)
        pygame.mixer.music.load("beepwrong.mp3")
        pygame.mixer.music.play()

    elif num == 202:
        cp2 = PhotoImage(file='rock.png')
        cl2 = Label(frame, image=cp2, height=300, width=300).place(x=40, y=60)

        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()

    elif num == 303:
        cp3 = PhotoImage(file='scissor.png')
        cl3 = Label(frame, image=cp3, height=300, width=300).place(x=40, y=60)

        play_score = play_score + 1
        Label(frame, text=play_score, font=("calibri", 15), bg="grey").place(x=775, y=20)
        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()


def scissor():
    global p3
    global l3
    global cl1
    global cl2
    global cl3
    global cp1
    global cp2
    global cp3
    global com_score
    global play_score


    p3 = PhotoImage(file='scissor.png')
    l3 = Label(frame, image=p3, height=300, width=300).place(x=550, y=60)

    pygame.mixer.music.load("beepwrong.mp3")
    pygame.mixer.music.play()

    num = random.choice(list)

    if num == 101:
        cp1 = PhotoImage(file='paper.png')
        cl1 = Label(frame, image=cp1, height=300, width=300).place(x=40, y=60)

        play_score = play_score + 1
        Label(frame, text=play_score, font=("calibri", 15), bg="grey").place(x=775, y=20)
        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()


    elif num == 202:
        cp2 = PhotoImage(file='rock.png')
        cl2 = Label(frame, image=cp2, height=300, width=300).place(x=40, y=60)

        com_score = com_score + 1
        Label(frame, text=com_score, font=("calibri", 15), bg="grey").place(x=245, y=20)
        pygame.mixer.music.load("beepwrong.mp3")
        pygame.mixer.music.play()


    elif num == 303:
        cp3 = PhotoImage(file='scissor.png')
        cl3 = Label(frame, image=cp3, height=300, width=300).place(x=40, y=60)

        pygame.mixer.music.load("beepclick.mp3")
        pygame.mixer.music.play()


rock = Button(root,text="rock",font=("calibri",18),height=2,width=10,bg="black",fg="white",command=rock).place(x=100, y=550)

paper = Button(root,text="paper",font=("calibri",18),height=2,width=10,bg="black",fg="white",command=paper).place(x=350, y=550)

scissor = Button(root,text="scissor",font=("calibri",18),height=2,width=10,bg="black",fg="white",command=scissor).place(x=600, y=550)


frame = Frame(root,height=500,width=880,bg="grey",borderwidth=4).place(x=10,y=10)

score1 = Label(frame,text="COMPUTER SCORE:",font=("calibri",15),bg="grey").place(x=75,y=20)

score2 = Label(frame,text="YOUR SCORE: ",font=("calibri",15),bg="grey").place(x=650,y=20)

c_score = Label(frame,text=com_score,font=("calibri",15),bg="grey").place(x=245,y=20)
p_score = Label(frame,text=play_score,font=("calibri",15),bg="grey").place(x=775,y=20)

Label(frame,text="YOU",font=("algerian",25),relief="sunken",bg="black",fg="red",width=12).place(x=580,y=400)
Label(frame,text="COMPUTER",font=("algerian",25),relief="sunken",bg="black",fg="red",width=12).place(x=60,y=400)

root.mainloop()