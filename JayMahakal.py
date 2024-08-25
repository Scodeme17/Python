from turtle import *
speed(2)
setup(800,600)
bgcolor('#f6eec0')
title('Jay Mahakal')

def my_goto(x,y):
    pencolor('#4682B4')
    penup()
    goto(x,y)
    pendown()

def rectangle(center_x,center_y, width,height,cornersize):
    penup()    
    goto(center_x-width/2+cornersize,center_y-height/2)
    pendown()
    for _ in range(2):
        fillcolor('#242124')
        begin_fill()
        forward(width-2*cornersize)
        circle(cornersize,90)
        forward(height-2*cornersize)
        circle(cornersize,90)
        end_fill()

def rectangle(center_x,center_y,width,height,cornersize):
    penup()    
    goto(center_x-width/2+cornersize,center_y-height/2)
    pendown()
    for _ in range(2):
        pencolor("Black")
        fillcolor('Black')
        begin_fill()
        forward(width-2*cornersize)
        circle(cornersize,90)
        forward(height-2*cornersize)
        circle(cornersize,90)
        end_fill()

rectangle(0,0,200,300,80)        

fillcolor('#4682B4')
begin_fill()

goto(-35,40)
penup()
fillcolor('orange')
begin_fill()
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

goto(-35,80)
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

goto(-35,60)
forward(80)
left(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
left(90)

pendown()
end_fill()

fillcolor('red')
begin_fill()
goto(5,50)
penup()
r=15
circle(r)
pendown()
end_fill()

penup()
goto(-150,-175)
pencolor('#4682B4')
fillcolor('#4682B4')
begin_fill()

rectangle(90,-111,600,70,37)
rectangle(90,-160,600,70,37)

# Adjusted y-coordinate for "Happy Maha Shivratri" text
penup()
goto(0, 220)
pendown()
speed(1)
color('Black')
style=('Courier',30, 'bold')
write('Happy Maha Shivratri', font=style, align='center', move=True)
penup()
goto(0, 160) 
pendown() 
pencolor('Black')
style=('Preeti', 20, 'normal')  
write(' ॐ नमः शिवाय', font=style, align='center', move=True)

done()
