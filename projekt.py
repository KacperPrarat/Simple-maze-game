import turtle
import math
import random

key_counter=0

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("maze")
wn.bgpic("cave.gif")
wn.tracer(0)
screenTk = wn.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)



images=["key.gif","wall.gif","knight.gif",
"gargoyle.gif","chest.gif","gate.gif","end.gif","gameover.gif"]

for image in images:
    turtle.register_shape(image)



class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wall.gif")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("knight.gif")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor() + 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor() - 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x,move_to_y) not in  walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return  True
        else:
            return  False


class Gate(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("gate.gif")
        self.penup()
        self.speed(0)
        self.goto(x,y)

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("chest.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class   Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("gargoyle.gif")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx=0
            dy=24
        elif self.direction == "down":
            dx=0
            dy= -24
        elif self.direction == "left":
            dx= -24
            dy=0
            self.shape("gargoyle.gif")
        elif self.direction == "right":
            dx= 24
            dy= 0
            self.shape("gargoyle.gif")
        else:
            dx=0
            dy=0

        if self.id_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x=self.xcor() + dx
        move_to_y=self.ycor() + dy
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])

        turtle.ontimer(self.move,t =random.randint(100,300))

    def id_close(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


levels = [""]
walls = []

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXXXXXXXXXX         XXX",
    "X  XXXXXXX XXXXXXX  XXXXXXXXXXXX    XXX   XXX",
    "X       XX XXXXXXX                 XXXX    XX",
    "X       XX XXX        E          XXXXXX    XX",
    "XXXXXX  XX XXX        TXXXXXXX   XXXXXXT   XX",
    "XXXXXX  XX          XXXXXXXXXX   XXXXXX    XX",
    "XXXXXX  XX   XXXX   XXXXXXXXXX       XX    XX",
    "X  XXX       XXXX   XXXXXXXXXXXXX       E  XX",
    "X EXXX  XXXXXXXXXXXXXXXXXXXXXXXXX          XX",
    "X              XXXXXX                     XXX",
    "XXXXXXXXXXXXX  XXXXXX  XXXXXXXXXXXXXXX     XX",
    "XXXXXXXXXXXXX   XXXXX  XXXXXXXXXXXXXXXT    XX",
    "XXX XXXXXXXXX           XXXXXXXXXXXXXX     XX",
    "XXX E                   XXXXXXXXXXXXXX     XX",
    "XXX   XXXXXXXXXXXX                T         X",
    "XXX   XXXXXXXXXXXX                          X",
    "XXG   XXXXXX          XXXXXXXXXX     XX    TX",
    "XX    XXXXXXX         XXXXXXXXXX     XX     X",
    "XX    XXXXXXXXXXXX   XXXXXXXXXXX           XX",
    "XXXX  XXXXXXXXXXXX   XXXXXXXXXXX        XXXXX",
    "XXXX     XXXXX       XXXXXXXXXXX  EXXXXXXXXXX",
    "XXXX    EXXXXX                    XXXXXXXXXXX",
    "XXX        T          XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]
gates=[]
treasures = []
enemies=[]
levels.append(level_1)


def setup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

            if character == "E":
                enemies.append((Enemy(screen_x,screen_y)))
            if character ==  "G":
                gates.append(Gate(screen_x,screen_y))

pen=Pen()
player = Player()
setup(levels[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

is_finished = False

for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)
while True:
    if key_counter >= 4 :
        for gate in gates: 
           if player.is_collision(gate) and not  is_finished:
            wn.clear()
            wn.bgcolor("black")
            wn.bgpic("end.gif")
            is_finished = True
    if not is_finished:
        for treasure in treasures:
            if player.is_collision(treasure):
                player.gold += treasure.gold
                key_counter += 1
                treasure.destroy()
                treasures.remove(treasure)
        for enemy in enemies:
            if player.is_collision(enemy)  and not is_finished:
                wn.clear()
                wn.bgcolor("black")
                wn.bgpic("gameover.gif")
                is_finished=True
    wn.update()

