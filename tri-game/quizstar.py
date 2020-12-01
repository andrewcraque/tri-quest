import json
import tkinter
import pygame as pg
from tkinter import *
import random

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

perguntas = [v for v in data[0].values()]
respostas_escolhas = [v for v in data[1].values()]

respostas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reposta_usuario = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 10:
        x = random.randint(0, 39)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 30:
        img = PhotoImage(file="bomdmais.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Você mandou bem !!")
    elif (score >= 20 and score < 30):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Quase lá !!")
    else:
        img = PhotoImage(file="ruim.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Estude mais !!")


def calc():
    global indexes, reposta_usuario, respostas
    x = 0
    score = 0
    for i in indexes:
        if reposta_usuario[x] == respostas[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, reposta_usuario
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    reposta_usuario.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=perguntas[indexes[ques]])
        r1['text'] = respostas_escolhas[indexes[ques]][0]
        r2['text'] = respostas_escolhas[indexes[ques]][1]
        r3['text'] = respostas_escolhas[indexes[ques]][2]
        r4['text'] = respostas_escolhas[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=perguntas[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=respostas_escolhas[indexes[0]][0],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=respostas_escolhas[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=respostas_escolhas[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=respostas_escolhas[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Tri-Quest")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="Tri-Quest",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Leia as regras e \nClique em Start se você estiver preparado!!",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 100))

lblRules = Label(
    root,
    text="Esse quiz contém 10 perguntas\nVocê terá 20 segundos para resolver uma questão\nDepois de selecionar um botão de opção, essa será a escolha final\nPense antes de selecionar",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.pack()

#musica

pg.init()

#...
#mixer.music.load('musica_menu.wav')

#mixer.music.play(-1)

root.mainloop()
