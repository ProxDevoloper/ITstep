import tkinter as tk
import random

WIDTH, HEIGHT = 400, 400
SEG_SIZE = 20
INITIAL_LENGTH = 3
DELAY = 100

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = []
        self.direction = "Right"
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        for i in range(INITIAL_LENGTH):
            seg = canvas.create_rectangle(
                start_x - i*SEG_SIZE, start_y,
                start_x - i*SEG_SIZE + SEG_SIZE, start_y + SEG_SIZE,
                fill="green"
            )
            self.segments.append(seg)

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.segments[0])
        if self.direction == "Left":
            x1 -= SEG_SIZE
            x2 -= SEG_SIZE
        elif self.direction == "Right":
            x1 += SEG_SIZE
            x2 += SEG_SIZE
        elif self.direction == "Up":
            y1 -= SEG_SIZE
            y2 -= SEG_SIZE
        elif self.direction == "Down":
            y1 += SEG_SIZE
            y2 += SEG_SIZE

        # Add new head
        new_head = self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        self.segments = [new_head] + self.segments

    def remove_tail(self):
        tail = self.segments.pop()
        self.canvas.delete(tail)

    def get_head_coords(self):
        return self.canvas.coords(self.segments[0])

    def check_collision(self):
        x1, y1, x2, y2 = self.get_head_coords()
        # Wall collision
        if x1 < 0 or y1 < 0 or x2 > WIDTH or y2 > HEIGHT:
            return True
        # Self collision
        for seg in self.segments[1:]:
            if self.canvas.coords(seg) == [x1, y1, x2, y2]:
                return True
        return False

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = None
        self.place()

    def place(self):
        if self.id:
            self.canvas.delete(self.id)
        x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        self.id = self.canvas.create_oval(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="red")

    def get_coords(self):
        return self.canvas.coords(self.id)

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.running = True
        self.score = 0
        self.root.title(f"Змейка | Счёт: {self.score}")

        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Up>", self.up)
        self.root.bind("<Down>", self.down)

        self.restart_btn = tk.Button(root, text="Рестарт", font=("Arial", 14), command=self.restart)
        self.restart_btn.pack(pady=5)


        self.fun_btn = tk.Button


        self.update()

    def left(self, event):
        if self.snake.direction != "Right":
            self.snake.direction = "Left"

    def right(self, event):
        if self.snake.direction != "Left":
            self.snake.direction = "Right"

    def up(self, event):
        if self.snake.direction != "Down":
            self.snake.direction = "Up"

    def down(self, event):
        if self.snake.direction != "Up":
            self.snake.direction = "Down"


    def restart(self):
        self.canvas.delete("all")
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.running = True
        self.score = 0
        self.root.title(f"Змейка | Счёт: {self.score}")
        self.update()

    def update(self):
        if not self.running:
            return
        self.snake.move()
        # Check food collision
        if self.snake.get_head_coords() == self.food.get_coords():
            self.score += 1
            self.root.title(f"Змейка | Счёт: {self.score}")
            self.food.place()
        else:
            self.snake.remove_tail()
        # Check collisions
        if self.snake.check_collision():
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", 32))
            return
        self.root.after(DELAY, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()