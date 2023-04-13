import turtle
turtle.bgcolor('black')
turtle.title("New year")
screen= turtle.Screen()
screen.setup(650,580)
s = turtle.Turtle()
s.speed(4)
s.right(90)
s.pu()
s.forward(180)
s.left(90)
s.pd()
s.fillcolor("white")
s.begin_fill()
s.forward(160)
s.left(40)  
s.circle(250,280)
s.left(40)
s.forward(160)
s.end_fill()
#We will start with Radha
s.fillcolor("orange")
s.begin_fill()
# duppata
s.forward(160)
s.left(130)
s.circle(-300,30)
s.forward(95)
# shoulder
s.circle(50,40)
s.right(40)
# head
s.forward(43)
s.circle(80,25)
s.circle(50,30)
s.left(10)
s.circle(35,28)
#krishna's turban
s.right(160)
s.circle(10,100)
s.right(100)
s.circle(10,80)
s.forward(20)
s.left(80)
s.circle(100,15)
s.right(90)
s.forward(6)
s.left(65)
s.circle(60,55)
#morpankh
s.right(160)
s.circle(20,100)
s.forward(10)
s.circle(-20,25)
s.left(170)
s.circle(-20,40)
s.forward(10)
s.circle(20,80)
#done morpankh
s.right(135)
s.circle(60,15)
s.left(70)
s.forward(6)
s.right(110)
s.forward(9)
s.left(80)
s.circle(70,24)
s.right(60)
s.circle(65,30)
s.circle(-5,110)

#right hand of Krishna
s.circle(5,120)
s.right(90)
s.circle(5,60)
s.forward(10)
s.circle(10,5)
s.right(80)
s.forward(15)
s.circle(-5,160)
#first open finger of right hand
s.forward(6)
s.circle(2,180)
s.forward(6)
s.circle(20,30)

# fingers holding bansuri
s.right(140)
s.circle(3,150)
s.right(110)
s.circle(4,80)
s.forward(2)
s.right(100)

#second open finger of krishna
s.forward(6)
s.right(60)
s.forward(9)
s.circle(2,180)
s.forward(10)
s.left(30)
s.forward(15)

#bansuri
s.right(85)
s.forward(40)
s.right(60)
s.circle(5,310)
s.right(80)
s.forward(3)
s.right(90)

#dor on bansuri
s.forward(42)
s.right(30)
s.forward(10)
s.left(90)
s.circle(20,60)
s.left(95)
s.forward(12)
s.right(29)
s.forward(42)

#rest part of bansuri
s.right(90)
s.forward(34)
s.right(85)

#left hand of Krishna
s.forward(2)
s.circle(60,25)

#Krishna's duppata
s.right(80)
s.circle(10,40)
s.forward(45)
s.left(10)
s.forward(130)

#plates of duppata
s.left(90)
s.forward(20)
s.right(90)
s.forward(10)
s.left(90)
s.forward(10)
s.right(90)
s.forward(5)
s.left(90)
s.forward(25)
#duppata
s.left(100)
s.forward(120)

s.right(175)
s.circle(50,50)

#Krishna's dhoti
s.right(80)
s.circle(110,15)
s.forward(75)

#rectangular base  in the beginning
s.left(97)
s.forward(260)
s.end_fill()
#completed drawing Radhe Krishna

s.pu()
s.right(90)
s.forward(100)
s.right(90)
s.forward(420)
#text
s.color("orange")
s.write("HAPPY NEW YEAR 2080 BS", font=("Handwritten",45, "bold"))    
s.hideturtle()
turtle.done()
