import turtle

def draw_square(some_turtle):
    count = 4
    while(count>0):
        some_turtle.forward(100)
        some_turtle.right(90)
        count = count-1;
  

def draw_circle():
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range (1,37):
        draw_square(brad);
        brad.right(10);
    #draw_circle();
    window.exitonclick();

draw_art();

