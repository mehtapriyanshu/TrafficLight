import tkinter as tk

class Light:
    def __init__(self, circle):
        self.circle = circle
        self.circle.title("Circle in the box")


        self.canvas = tk.Canvas(self.circle, width=400, height=1000, bg="white")
        self.canvas.pack()

        self.draw_box()
        self.draw_circles()
        self.draw_buttons()

        # Dictionary to keep track of circle colors
        self.circle_colors = {
            0: '',  # Index of circle: color
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: ''
        }

    def draw_box(self):
        self.canvas.create_rectangle(50, 50, 300, 150, outline="black")
    
    def draw_circles(self):
        self.circles = []
        circle_positions = [
            (100, 100), (175, 100), (250, 100),
            (175, 200), (175, 400), (175, 600),
            (175, 800), (175, 900)
        ]
        for x, y in circle_positions:
            circle = self.canvas.create_oval(x-30, y-30, x+30, y+30, outline='black', fill='')
            self.circles.append(circle)
    
    def draw_buttons(self):
        button_positions = [(270, 200), (270, 400), (270, 600), (270, 800), (270, 900)]
        button_commands = [self.handle_click, self.handle, self.clicked, self.click, self.alternate]
        for position, command in zip(button_positions, button_commands):
            button = tk.Button(self.canvas, text="Click Me!", command=command)
            button_window = self.canvas.create_window(position[0], position[1], anchor="w", window=button)

    def handle_click(self):
        self.reset_colors()
        self.color_circle(0, 'red')
        self.color_circle(3, 'red')

    def handle(self):
        self.reset_colors()
        self.color_circle(1, 'yellow')
        self.color_circle(4, 'yellow')

    def clicked(self):
        self.reset_colors()
        self.color_circle(2, 'green')
        self.color_circle(5, 'green')

    def click(self):
        self.reset_colors()
        self.color_circle(0, 'red')
        self.color_circle(1, 'yellow')
        self.color_circle(2, 'green')
        self.color_circle(6, 'blue')

    def alternate(self):
        self.reset_colors()
        colors = ['red', 'yellow', 'green']
        for i in range(len(colors)):
            self.color_circle(i, colors[i])
    
    def color_circle(self, index, color):
        self.canvas.itemconfig(self.circles[index], fill=color)
        self.circle_colors[index] = color

    def reset_colors(self):
        for index, color in self.circle_colors.items():
            self.canvas.itemconfig(self.circles[index], fill='')
            self.circle_colors[index] = ''

def main():
    root = tk.Tk()
    root.title('LIGHT')
    app = Light(root)
    root.mainloop()

if __name__ == "__main__":
    main()
