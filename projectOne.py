#Kamden B, Shashank A
from random import randint
from ssl import Options
import tkinter #used to generate a random number
import turtle as trtl #used to draw

#creates background
wn = trtl.Screen()

trtl.hideturtle() #hides the turtle icon so people won't see it
trtl.speed(0) #makes the turtle fast

wn.setup() #creates the screen
wn.bgpic("donut_shop.gif") #sets background image

#all variables to be used
donutSize = 20 #how big the donut is by default
holeSize = donutSize/2 #how big the hole in the donut will be

#location variables
donutX = -220 #x coordinate of the donut
donutY = -150 #y coordinate of the donut
holeX = donutX #x coordinate of donut hole
holeY = donutY + (donutSize/2) #places the hole in the center of the donut
sprinkleX = donutX #sets sprinkles to be on the same spot as the donut
sprinkleY = donutY #sprinkles will move around each donut for each individual sprinkle
boxX = -240 #default x coordinate
boxY = -110 #default y coordinate, goes up if a new row is made

#donut variables
donutsTotal = 0 #amount of donuts to be created
donutsMade = 0 #amount of donuts created so far
donutFrosting = 'brown' #color of the frosting, defaults to brown until user changes
donutsFrosted = 0 #amount of donuts that have been frosted
donutsSprinkled = 0 #amount of donuts that have been sprinkled

#sprinkle variables
sprinklesColor = '' #color of the sprinkles
addSprinkles= '' #if the user wants sprinkles or not
sprinklesMade = 0 #amount of sprinkles made per donut, will reset for each donut
sprinklesWidth = 2 #how wide the sprinkles are
sprinklesLength = 5 #how long the sprinkles are
xIncrease = 0 #how much sprinkles will shift on the x axis
yIncrease = 0 #how much sprinkles will shift on the y axis

#box variables
wantsBox = ""
boxLength=0 #how long the box will be, increases with each donut
boxWidth=50 #how wide the box will be, increases if it starts a new row

#prompt user for amount of donuts wanted
donutsTotal = trtl.numinput("Donuts", "How many donuts would you like? (1-12) ", minval=1, maxval=12)

#add blank donuts with nothing on them, possible animations
while(donutsMade < donutsTotal):

  #makes donut outline
  trtl.penup()
  trtl.goto(donutX,donutY)
  trtl.pendown()
  trtl.fillcolor(donutFrosting)
  trtl.begin_fill()
  trtl.circle(donutSize)
  trtl.end_fill()
  trtl.penup()

  #makes donut hole
  trtl.goto(holeX, holeY)
  trtl.pendown()
  trtl.fillcolor('white')
  trtl.begin_fill()
  trtl.circle(holeSize)
  trtl.end_fill()

  #shift each donut to the right
  donutX = donutX + (donutSize + 20)
  holeX = donutX

  #increases donut made count by one
  donutsMade=donutsMade+1

  #if at half of donuts made, puts new donuts on a separate row
  if(donutsMade==int(donutsTotal/2)):
    donutX = -220
    donutY = donutY+45
    holeX = donutX
    holeY = donutY + (donutSize/2)
    boxWidth=100
    boxY = -50

#prompt user for frosting, add list of available frostings
donutFrosting = trtl.textinput("Frosting", "Choose a frosting: Chocolate, Vanilla, Strawberry, or none. ")
donutFrosting = donutFrosting.lower()
#checks to make sure they choose a valid frosting option
while(donutFrosting!="chocolate" and donutFrosting!="vanilla" and donutFrosting!="strawberry" and donutFrosting!='none'):
  donutFrosting = trtl.textinput("Frosting", "Please enter a frosting from our list: Chocolate, Vanilla, Strawberry, or none. ")
  donutFrosting = donutFrosting.lower()
#changes color to valid turtle color
if(donutFrosting == "chocolate"):
  donutFrosting = "chocolate4"
if(donutFrosting == "vanilla"):
  donutFrosting = "AntiqueWhite"
if(donutFrosting == "strawberry"):
  donutFrosting = "DeepPink"


#reset positioning to the first donut
donutX = -220
donutY = -150
holeX = donutX
holeY = donutY + (donutSize/2)

#add frostings on top of the donuts, every donut available gets frosting
while(donutsFrosted < donutsTotal and donutFrosting != 'none'):

  #recolors donut outline to frosting color
  trtl.penup()
  trtl.goto(donutX,donutY)
  trtl.pendown()
  trtl.fillcolor(donutFrosting)
  trtl.begin_fill()
  trtl.circle(donutSize)
  trtl.end_fill()
  trtl.penup()

  #remakes donut hole
  trtl.goto(holeX, holeY)
  trtl.pendown()
  trtl.fillcolor('white')
  trtl.begin_fill()
  trtl.circle(holeSize)
  trtl.end_fill()

  #move over to the next donut
  donutX = donutX + (donutSize + 20)
  holeX = donutX

  #increases donut made count by one
  donutsFrosted=donutsFrosted+1

  #if at half of donuts frosted, moves to the next row
  if(donutsFrosted==int(donutsTotal/2)):
    donutX = -220
    donutY = donutY+45
    holeX = donutX
    holeY = donutY + (donutSize/2)

#prompt user for sprinkles
addSprinkles = trtl.textinput("Sprinkles", "Would you like sprinkles with your donuts? ")
addSprinkles = addSprinkles.lower()
if(addSprinkles == "yes" or addSprinkles == "y"): #if they say yes to sprinkles
  #asks what color they want sprinkles to be
  sprinklesColor = trtl.textinput("Sprinkles", "What kind of sprinkles would you like: blue, red, orange, black, or gold? ")
  sprinklesColor = sprinklesColor.lower()
  #checks which color they selected and changes to appropriate valid turtle color
  while(sprinklesColor!="blue2" and sprinklesColor!="red2" and sprinklesColor!="DarkOrange2" and sprinklesColor!="gold1" and sprinklesColor!="black"):
    if(sprinklesColor == "blue"):
      sprinklesColor = "blue2"
    elif(sprinklesColor == "red"):
      sprinklesColor = "red2"
    elif(sprinklesColor == "orange"):
      sprinklesColor = "DarkOrange2"
    elif(sprinklesColor == "gold"):
      sprinklesColor = "gold1"
    #if not a color from the select, asks to input again and goes through loop until it's a proper color
    else:
      sprinklesColor = trtl.textinput("Sprinkles", "Please select a valid sprinkle color: blue, red, orange, black, or gold. ")
  
  #reset position back to the first donut
  donutX = -220
  donutY = -150

  #start making sprinkles on each donut
  trtl.pensize(sprinklesWidth) #changes to the size of the sprinkles
  trtl.pencolor(sprinklesColor)
  #while not every donut has been sprinkled
  while(donutsSprinkled < donutsTotal):
    #while not every sprinkle has been placed
    while(sprinklesMade < 12):
      
      if(sprinklesMade < 3): #first set of sprinkles shift right and up
        xIncrease = xIncrease + 5
        yIncrease = yIncrease + 6
        trtl.setheading(randint(0,90)) #goes from 0-90 to make sure sprinkles don't go off of donut
      
      elif(sprinklesMade < 6): #next set of sprinkles shift  left and up
        xIncrease = xIncrease - 5
        yIncrease = yIncrease + 6
        trtl.setheading(randint(270,360)) #goes from 90-180 so sprinkles don't go off of donut
      
      elif(sprinklesMade < 9): #next set of sprinkles shift left and down
        xIncrease = xIncrease - 5
        yIncrease = yIncrease - 6
        trtl.setheading(randint(180,270)) #180-270 to ensure sprinkles don't go off of donut
      
      else: #last set shift right and down
        xIncrease = xIncrease + 5
        yIncrease = yIncrease - 6
        trtl.setheading(randint(90,180)) #270-360 to ensure sprinkles don't of off of donut
      
      trtl.penup()
      sprinkleX = donutX + xIncrease #x-cord of sprinkle location
      sprinkleY = donutY + yIncrease + 2 #y-cord of sprinkle location, give some space so sprinkles don't go out of donut
      trtl.goto(sprinkleX, sprinkleY)
      trtl.pendown()
      trtl.forward(sprinklesLength)
      sprinklesMade = sprinklesMade + 1 #increments sprinkles made every loop

    donutX = donutX + (donutSize + 20) #moves location to the next donut
    donutsSprinkled = donutsSprinkled + 1 #increments how many donuts have been sprinkled

    if(donutsSprinkled==int(donutsTotal/2)): #if it reaches half of donuts sprinkled it shifts to next row
      donutX = -220
      donutY = donutY+45
    
    sprinklesMade = 0 #resets sprinkles made count

#asks if user wants a box
wantsBox = trtl.textinput("Box", "Would you like your donuts in a box?")
#if they want a box, puts them in a box
if(wantsBox == 'y' or wantsBox == 'yes'):

  boxLength = donutsTotal*20
  if(donutsTotal==1):
    boxLength=boxLength*2 #makes it cover the whole donut
  #creates the shape of the box and fills
  trtl.penup()
  trtl.setheading(0)
  trtl.pencolor('black')
  trtl.fillcolor('white')
  trtl.begin_fill()
  trtl.goto(boxX, boxY)
  trtl.pendown()
  trtl.forward(boxLength)
  trtl.right(90)
  trtl.forward(boxWidth)
  trtl.right(90)
  trtl.forward(boxLength)
  trtl.right(90)
  trtl.forward(boxWidth)
  trtl.end_fill()

  #goes to center of the box and writes shop name
  trtl.penup()
  trtl.goto((boxX + (boxLength/2)), (boxY - (boxWidth/2) - 20)) #writes the text in the center of the box
  trtl.pendown()
  trtl.write("Donut Shop", align="center", font=("Arial", int(donutsTotal*2), "normal"))

tkinter.messagebox.showinfo(title="The End", message = "Thanks for making donuts with us!")

wn.mainloop() #keeps screen showing
