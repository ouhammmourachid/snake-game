import tkinter as tk
import numpy as np
from time import sleep
import random
def L():
    return [[i,j]for i in range(100) for j in range(60)]
score=-1
s=1
p=1
b=True
class Food:
    New_food=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Food.New_food=self

class Squire_Food(tk.Canvas):
    New_Squire=0
    def __init__(self,x,y):
        tk.Canvas.__init__(self,width=10,height=10,bg="red")
        self.place(x=x*10,y=y*10)
        Food(x,y)
        Squire_Food.New_Squire=self

class Node:
    all=[None]
    def __init__(self,x:int,y:int,next=None):
        self.x=x
        self.y=y
        self.next=Node.all[-1]
        Node.all.append(self)
    def change(self,new_x,new_y):
        Node.all.remove(self)
        self.x=new_x
        self.y=new_y
        Node.all.append(self)

class snake(tk.Canvas):
    all=[]
    def __init__(self,x_position,y_position):
        tk.Canvas.__init__(self,width=10,height=10,bg="black")
        self.place(x=x_position*10,y=y_position*10)
        Node(x_position,y_position)
        snake.all.append(self)
    def change_position(self):
        snake.all.remove(self)
        self.place(x=Node.all[-1].x*10,y=Node.all[-1].y*10)
        snake.all.append(self)


def Forward(event):
    global s
    global p
    if s!=0 and Node.all[-1].x!=Node.all[-2].x-1:
        Node.all[1].change((Node.all[-1].x+1)%100,(Node.all[-1].y)%60)
        snake.all[0].change_position()
        s=0
    if s==0 and Node.all[-1].x==Food.New_food.x-1 and Node.all[-1].y==Food.New_food.y:
        Squire_Food.New_Squire.destroy()
        snake(Food.New_food.x,Food.New_food.y)
        p=1
def Backward(event):
    global s
    global p
    if  s!=1 and Node.all[-1].x!=Node.all[-2].x+1:
        Node.all[1].change((Node.all[-1].x-1)%100,(Node.all[-1].y)%60)
        snake.all[0].change_position()
        s=1
    if s==1 and Node.all[-1].x==Food.New_food.x+1 and Node.all[-1].y==Food.New_food.y:
        Squire_Food.New_Squire.destroy()
        snake(Food.New_food.x,Food.New_food.y)
        p=1
def Up(event):
    global s
    global p
    if  s!=2 and Node.all[-1].y!=Node.all[-2].y+1:
        Node.all[1].change((Node.all[-1].x)%100,(Node.all[-1].y-1)%60)
        snake.all[0].change_position()
        s=2
    if s==2 and Node.all[-1].x==Food.New_food.x and Node.all[-1].y==Food.New_food.y+1:
        Squire_Food.New_Squire.destroy()
        snake(Food.New_food.x,Food.New_food.y)
        p=1
def Down(event):
    global s
    global p
    if s!=3 and Node.all[-1].y!=Node.all[-2].y-1:
        Node.all[1].change((Node.all[-1].x)%100,(Node.all[-1].y+1)%60)
        snake.all[0].change_position()
        s=3
    if s==3 and Node.all[-1].x==Food.New_food.x and Node.all[-1].y==Food.New_food.y-1:
        Squire_Food.New_Squire.destroy()
        snake(Food.New_food.x,Food.New_food.y)
        p=1
def animation():
    global S
    global p
    global b
    global score
    while b :
        sleep(0.3)
        if p==1:
            score+=1
            C=[]
            F=[]
            for n in Node.all:
                if n!=None:
                    F+=[[n.x,n.y]]
            C=random.choice([i for i in L() if i not in F ])
            Squire_Food(C[0],C[1])
            p=0
        if s==0:
            Node.all[1].change((Node.all[-1].x+1)%100,(Node.all[-1].y)%60)
            snake.all[0].change_position()
            snake.all[0].update()    
        elif s==1:
            Node.all[1].change((Node.all[-1].x-1)%100,(Node.all[-1].y)%60)
            snake.all[0].change_position()
            snake.all[0].update()
        elif s==2:
            Node.all[1].change((Node.all[-1].x)%100,(Node.all[-1].y-1)%60)
            snake.all[0].change_position()
            snake.all[0].update()

        else:
            Node.all[1].change((Node.all[-1].x)%100,(Node.all[-1].y+1)%60)
            snake.all[0].change_position()
            snake.all[0].update()
        slab=tk.Label(text=score,bg="blue")
        slab.place(x=980,y=580)
        if s==0 and Node.all[-1].x==Food.New_food.x-1 and Node.all[-1].y==Food.New_food.y:
            Squire_Food.New_Squire.destroy()
            snake(Food.New_food.x,Food.New_food.y)
            p=1
        if s==1 and Node.all[-1].x==Food.New_food.x+1 and Node.all[-1].y==Food.New_food.y:
            Squire_Food.New_Squire.destroy()
            snake(Food.New_food.x,Food.New_food.y)
            p=1
        if s==2 and Node.all[-1].x==Food.New_food.x and Node.all[-1].y==Food.New_food.y+1:
            Squire_Food.New_Squire.destroy()
            snake(Food.New_food.x,Food.New_food.y)
            p=1
        if s==3 and Node.all[-1].x==Food.New_food.x and Node.all[-1].y==Food.New_food.y-1:
            Squire_Food.New_Squire.destroy()
            snake(Food.New_food.x,Food.New_food.y)
            p=1
        for n in Node.all:
            if n!=None:
                if (s==0 and Node.all[-1].x==n.x-1 and Node.all[-1].y==n.y) or (s==1 and Node.all[-1].x==n.x+1 and Node.all[-1].y==n.y) or (s==2 and Node.all[-1].x==n.x and Node.all[-1].y==n.y+1)or(s==3 and Node.all[-1].x==n.x and Node.all[-1].y==n.y-1 ):
                    b=False
                    break
    lab=tk.Label(root,text="GAME OVER",font=50,bg="red")
    lab.place(x=350,y=250,width=300,height=100)

def create():
    F=[]
    for n in Node.all:
        if n!=None:
            F+=[[n.x,n.y]]
    return random.choice([i for i in L() if i not in F ])


s=0
root=tk.Tk()
root.geometry("1000x600")
root.resizable(False,False)
root.config(bg="white")
root.title("snake game")
for i in range(40):
    snake(i,0)
root.bind("<Right>",Forward)
root.bind("<Left>",Backward)
root.bind("<Up>",Up)
root.bind("<Down>",Down)
animation()
#annime()
root.mainloop()



