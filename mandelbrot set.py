from setup_screen import setup_screen
import turtle

def mandelbrot_func(c, z):
    return z.real**2 - z.imag**2 + 2j*z.real*z.imag + c


def draw_mandelbrot(size,iterations):
    """Draws the Mandelbrot set
    this time actually my own creation
    size - size of the drawing (equals 1 unit in the coordinate system)
    iterations - the number of iterations tried on every coordinate
    """
    
    
    nums_calculated = 0
    
    for x in range(-2*size, int((1/2)*size)): 
        for y in range (-size, size):
            in_mandelbrot = True
            c = complex(x/size, y/size)
            nums_calculated += 1
            z = 0 + 0j
            for i in range(iterations):
                z = mandelbrot_func(c,complex(round(z.real,iterations//2),round(z.imag, iterations//2)))
                if z.real**2 + z.imag**2 > 4:
                    in_mandelbrot = False
                    red = i
                    green = (i + 32) % 255 
                    blue = ((i) + 100) % 255
                    turtle.color(red, green, blue)
                    break

            if in_mandelbrot:
                turtle.color("black")
            turtle.setposition(x, y)
            turtle.pendown()
            turtle.dot(1.5)
            turtle.penup()

        
        percent_done = nums_calculated * 20 / ((5)*size*size)  # Percent of numbers that have been iterated through
        if percent_done.is_integer():
            print(str(5*percent_done) + "% done")

size = input("Enter a size for the Mandelbrot Set:    ")
while not size.isnumeric():
    size = input("The input must be a positive integer!    ")
size = int(size)

iterations = input("Enter the amount of iterations:    ")
while not iterations.isnumeric():
    iterations = input("The input must be a positive integer!    ")
iterations = int(iterations)
    
setup_screen(title="The Mandelbrot Set", lenx=4*size, leny=2.5*size, tracer_size=3200)
turtle.colormode(255)
print("Starting drawing")
draw_mandelbrot(size, iterations)
turtle.update()
print("Done")


