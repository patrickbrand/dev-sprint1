# Exercise 5.6

# Name: Patrick Brand


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

def koch(t, length):
    if length < 3:
        draw(t, length, 5)
    else:
        curve = length / 3
        draw(t, curve, 5)
        lt(t, 60)
        draw(t, curve, 5)
        rt(t, 120)
        draw(t, curve, 5)
        lt(t, 60)
    
koch(bob, 9)

wait_for_user()					

