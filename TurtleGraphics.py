#TurtleGraphics.py
#Name: Bennett McDonald    
#Date: 2/16/25
#Assignment: turtle graphic

import turtle

def drawPolygon(myTurtle, sides):
    angle = 360 / sides  # Calculate the interior angle of the polygon
    for _ in range(sides):
        myTurtle.forward(100)  # Move forward by 100 units (length of each side)
        myTurtle.right(angle)  # Turn right by the calculated angle

def main():
    # Create a turtle object
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)  # Set the drawing speed to maximum

    # Ask the user for the number of sides of the polygon
    sides = int(input("Enter the number of sides for the polygon: "))

    # Draw the polygon with the given number of sides
    drawPolygon(myTurtle, sides)

    turtle.done()

if __name__ == "__main__":
    main()


