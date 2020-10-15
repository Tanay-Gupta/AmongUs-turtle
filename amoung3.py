#credits tanaywhocodes
from turtle import *
speed(1)
shape("turtle")
bgcolor("grey")
def belt(): 
    rt(10)
    for i in range(6,17):
        pensize(i)
        fd(3)       
    pensize(12)
    lt(15)
    fd(18)#25
    lt(12)
    fd(22)#25
    
def legs():
    setheading(270)
    fd(45)
    circle(30,180,7)
    fd(45)
    
def  head():
    circle(85,150)
def rightBody():
    setheading(90)
    rt(2)
    fd(125)
    lt(4)
    fd(50)
    
def leftbody():
    fd(50)
    circle(20,90)
    setheading(260)
    fd(40)
    for i in range(6):
        lt(5)
        fd(20) 
        setheading(270)
def eyes():
    fillcolor('cyan')
    begin_fill()
    #speed(-1)
    penup()
    fd(110)
    pendown()
    
    
    rt(87)
    
    fd(40)
    circle(45,175)
    lt(5)
    fd(90)
    circle(37,165)
    for i in range(3):
        rt(1.75)
        fd(14)
    lt(13)
    fd(15)
    end_fill()
    

       
def bag():
    setheading(270)
    for i in range(2):
        lt(90)
        fd(40)
        lt(90)
        if i==1:
            penup()
        fd(140)
    pendown()
   
    
def leftleg():
    fd(18)
    circle(30,180,5)
    fd(21)

color('black','red')
begin_fill()
belt()
legs()
bag()
rightBody()
head()
leftbody()
leftleg()
end_fill()
eyes()
ht()
