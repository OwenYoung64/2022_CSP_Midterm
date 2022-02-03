'''
Write a turtle program that draws 10 parrallel lines.
* Must use a loop - cannot use 10 turtle draw commands
Each parallel line should be a randomly selected color and randomly selected length.
* Color should be selected randomly from a list
* The length of each line should be generated randomly (you may choose your own method).

Don't forget your imports!!!
'''
import turtle as trtl
import random as rand
line1 = trtl.Turtle()
line1.speed(.5)
line2 = trtl.Turtle()
line2.speed(.5)
line3 = trtl.Turtle()
line3.speed(.5)
line4 = trtl.Turtle()
line4.speed(.5)
line5 = trtl.Turtle()
line5.speed(.5)
line6 = trtl.Turtle()
line6.speed(.5)
line7 = trtl.Turtle()
line7.speed(.5)
line8 = trtl.Turtle()
line8.speed(.5)
line9 = trtl.Turtle()
line9.speed(.5)
line10 = trtl.Turtle()
line10.speed(.5)
colorlist = ["red","blue","green","yellow","orange","black","purple","cyan","pink","lime"]
return_value = colorlist.pop(rand.randint(0, 9))
line1.pencolor(return_value)
line1.penup()
line1.backward(200)
line1.left(90)
line1.pendown()
line1.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 8))
line2.pencolor(return_value)
line2.penup()
line2.backward(150)
line2.left(90)
line2.pendown()
line2.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 7))
line3.pencolor(return_value)
line3.penup()
line3.backward(100)
line3.left(90)
line3.pendown()
line3.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 6))
line4.pencolor(return_value)
line4.penup()
line4.backward(50)
line4.left(90)
line4.pendown()
line4.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 5))
line5.pencolor(return_value)
line5.penup()
line5.backward(0)
line5.left(90)
line5.pendown()
line5.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 4))
line6.pencolor(return_value)
line6.penup()
line6.forward(50)
line6.left(90)
line6.pendown()
line6.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 3))
line7.pencolor(return_value)
line7.penup()
line7.forward(100)
line7.left(90)
line7.pendown()
line7.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 2))
line8.pencolor(return_value)
line8.penup()
line8.forward(150)
line8.left(90)
line8.pendown()
line8.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 1))
line9.pencolor(return_value)
line9.penup()
line9.forward(200)
line9.left(90)
line9.pendown()
line9.forward(rand.randint(50, 100))

return_value = colorlist.pop(rand.randint(0, 0))
line10.pencolor(return_value)
line10.penup()
line10.forward(250)
line10.left(90)
line10.pendown()
line10.forward(rand.randint(50, 100))


wn = trtl.Screen()
wn.mainloop()