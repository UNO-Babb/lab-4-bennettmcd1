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


import turtle

def drawSquare(myTurtle, size):
    # Draws a square of the specified size
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def fillQuadrant(myTurtle, quadrant, size):
    # Divide the square into four quadrants and fill the selected one
    myTurtle.penup()
    if quadrant == 1:  # Top-left quadrant
        myTurtle.goto(-size / 2, size / 2)  # Move to the top-left corner
        myTurtle.pendown()
        myTurtle.begin_fill()
        for _ in range(2):
            myTurtle.forward(size / 2)
            myTurtle.right(90)
        myTurtle.end_fill()
    elif quadrant == 2:  # Top-right quadrant
        myTurtle.goto(0, size / 2)  # Move to the top-right corner
        myTurtle.pendown()
        myTurtle.begin_fill()
        for _ in range(2):
            myTurtle.forward(size / 2)
            myTurtle.right(90)
        myTurtle.end_fill()
    elif quadrant == 3:  # Bottom-left quadrant
        myTurtle.goto(-size / 2, 0)  # Move to the bottom-left corner
        myTurtle.pendown()
        myTurtle.begin_fill()
        for _ in range(2):
            myTurtle.forward(size / 2)
            myTurtle.right(90)
        myTurtle.end_fill()
    elif quadrant == 4:  # Bottom-right quadrant
        myTurtle.goto(0, 0)  # Move to the bottom-right corner
        myTurtle.pendown()
        myTurtle.begin_fill()
        for _ in range(2):
            myTurtle.forward(size / 2)
            myTurtle.right(90)
        myTurtle.end_fill()

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)

    # Ask the user for the size of the square
    size = int(input("Enter the size of the square: "))

    # Ask the user for the quadrant to fill (1, 2, 3, or 4)
    quadrant = int(input("Enter the quadrant to fill (1 - Top left, 2 - Top right, 3 - Bottom left, 4 - Bottom right): "))

    # Draw the square and fill the selected quadrant
    drawSquare(myTurtle, size)
    fillQuadrant(myTurtle, quadrant, size)

    turtle.done()

if __name__ == "__main__":
    main()

import turtle

def drawSquare(myTurtle, size):
    # Draws a square of the specified size
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawMultipleSquares(myTurtle, num_squares, size):
    # Draws multiple squares with decreasing sizes
    for i in range(num_squares):
        drawSquare(myTurtle, size)  # Draw the current square
        myTurtle.penup()
        myTurtle.goto(myTurtle.xcor() + 10, myTurtle.ycor() + 10)  # Move the turtle slightly to the right and up
        myTurtle.pendown()
        size -= 20  # Decrease the size for the next square

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)

    # Ask the user for the number of squares and the size of the largest square
    num_squares = int(input("Enter the number of squares to draw: "))
    size = int(input("Enter the size of the largest square: "))

    # Draw multiple squares
    drawMultipleSquares(myTurtle, num_squares, size)

    turtle.done()

if __name__ == "__main__":
    main()


