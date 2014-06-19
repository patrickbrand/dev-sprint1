# This is where Exercise 5.4 goes
# Name: Patrick Brand

def is_triangle(x, y, z):
    if x > y + z:
        print 'No'
    elif y > x + z:
        print 'No'
    elif z > y + x:
        print 'No'
    else:
        print 'Yes'
        
def get_triangle_input():
    x = int(raw_input('Enter length 1:\n'))
    y = int(raw_input('Enter length 2:\n'))
    z = int(raw_input('Enter length 3:\n'))
    
    is_triangle(x, y, z)
    
get_triangle_input()