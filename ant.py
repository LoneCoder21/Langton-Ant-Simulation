class Ant:
    def __init__(self, id, position, direction):
        self.id = id
        self.position = position
        self.direction = direction
        self.is_alive = True

    def move(self):
        x, y = self.position
        if self.direction == "up":
            y -= 1
        elif self.direction == "down":
            y += 1
        elif self.direction == "left":
            x -= 1
        elif self.direction == "right":
            x += 1
        self.position = (x, y)

    def turn_left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "right":
            self.direction = "up"

    def turn_right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "right":
            self.direction = "down"

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def kill(self):
        self.is_alive = False
