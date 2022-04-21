from tkinter import *
from PIL import Image,ImageTk
from random import randint
root = Tk()
root.title("rock Scissor Paper")
root.configure(background="purple")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert
comp_label = Label(root,image=scissor_img_comp,bg="purple")
user_label = Label(root,image=scissor_img,bg="purple")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
user_scores=Label(root,text=0,font=100,bg="purple",fg="white")
comp_scores=Label(root,text=0,font=100,bg="purple",fg="white")
user_scores.grid(row=1,column=3)
comp_scores.grid(row=1,column=1)

#indicator
user_indicator=Label(root,text="USER",font=80)
comp_indicator=Label(root,text="COMPUTER",font=80)
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
msg = Label(root,font=50,bg="purple",fg="white")
msg.grid(row=3,column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(user_scores["text"])
    score += 1
    user_scores["text"] = str(score)

def updateCompScore():
    score = int(comp_scores["text"])
    score +=1
    comp_scores["text"] =str(score)

def check_Win(player,computer):
    if player == computer:
        updateMessage("Its a Tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass

choices = ["rock","paper","scissor"]

def updateChoice(x):
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image= rock_img_comp)
    elif compChoice == "scissor":
        comp_label.configure(image=scissor_img_comp)
    else:
        comp_label.configure(image=paper_img_comp)

    if x == "rock":
        user_label.configure(image= rock_img)
    elif x == "scissor":
        user_label.configure(image=scissor_img)
    else:
        user_label.configure(image=paper_img)

    check_Win(x,compChoice)
        
        
        
    
    


#button
rock_button=Button(root,text="ROCK",width=20,height=2,command=lambda:updateChoice("rock"),bg="orange",fg="white").grid(row=2,column=1)
scissor_button=Button(root,text="SCISSOR",width=20,height=2,command=lambda:updateChoice("scissor"),bg="orange",fg="white").grid(row=2,column=2)
paper_button=Button(root,text="PAPER",width=20,height=2,command=lambda:updateChoice("paper"),bg="orange",fg="white").grid(row=2,column=3)






root.mainloop()
