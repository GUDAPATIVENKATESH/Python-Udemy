import turn_left()
import move()

def turn_right() :
    turn_left()
    turn_left()
    turn_left()

turn_right

def turn_right() :
    turn_left()
    turn_left()
    turn_left()
    
def turn_around() :    
    turn_right()
    turn_left()
    turn_left()
    

move()
turn_around()
move()
turn_around()
move()
turn_around()
move()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


def jump() :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for j in range(0, 6) :
    jump()

while at_goal() == False  :  
    jump()

#
while not at_goal():
    
    if front_is_clear() :
        move()
    elif wall_in_front() :
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

def jump() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() :
        move()
    elif wall_in_front() :
       jump()

def jump() :
    turn_left()
    while not right_is_clear() :
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() :
        move()
    turn_left()

while not at_goal():
    if front_is_clear() :
        move()
    elif wall_in_front() :
       jump()



    