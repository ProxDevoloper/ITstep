import tkinter as tk
import random

WIDTH, HEIGHT = 600, 400

class Enemy:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 30
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(0, HEIGHT // 2)
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill="red")

    def move(self):
        self.y += 2
        self.canvas.move(self.id, 0, 2)
        if self.y > HEIGHT:
            self.canvas.delete(self.id)
            return False
        return True

class Bullet:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x-2, y-10, x+2, y, fill="yellow")

    def move(self):
        self.canvas.move(self.id, 0, -10)
        coords = self.canvas.coords(self.id)
        if coords[1] < 0:
            self.canvas.delete(self.id)
            return False
        return True

class ShooterGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.player = self.canvas.create_rectangle(WIDTH//2-20, HEIGHT-40, WIDTH//2+20, HEIGHT-20, fill="blue")
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.running = True

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
        

        self.spawn_enemy()
        self.update()

    def move_left(self, event):
        coords = self.canvas.coords(self.player)
        if coords[0] > 0:
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        coords = self.canvas.coords(self.player)
        if coords[2] < WIDTH:
            self.canvas.move(self.player, 20, 0)

    def shoot(self, event):
        coords = self.canvas.coords(self.player)
        x = (coords[0] + coords[2]) // 2
        y = coords[1]
        self.bullets.append(Bullet(self.canvas, x, y))

    def spawn_enemy(self):
        if self.running:
            self.enemies.append(Enemy(self.canvas))
            self.root.after(1000, self.spawn_enemy)

    def update(self):
        if not self.running:
            return

        # Move bullets
        for bullet in self.bullets[:]:
            if not bullet.move():
                self.bullets.remove(bullet)

        # Move enemies
        for enemy in self.enemies[:]:
            if not enemy.move():
                self.enemies.remove(enemy)
                self.game_over()
                return

        # Check collisions
        for bullet in self.bullets[:]:
            bullet_coords = self.canvas.coords(bullet.id)
            for enemy in self.enemies[:]:
                enemy_coords = self.canvas.coords(enemy.id)
                if self.check_collision(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet.id)
                    self.canvas.delete(enemy.id)
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    self.root.title(f"Score: {self.score}")
                    break

        self.root.after(30, self.update)

    def check_collision(self, a, b):
        return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", 32))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shooter Game")
    game = ShooterGame(root)
    root.mainloop()