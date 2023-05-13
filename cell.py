class Cell:
    def __init__(self, color, rule_state_id, x, y):
        self.color = color
        self.rule_state_id = rule_state_id
        self.x = x
        self.y = y
        self.is_visited = False

    def get_position(self):
        return (self.x, self.y)

    def set_color(self, new_color):
        self.color = new_color

    def flip_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def set_visited(self):
        self.is_visited = True

    def is_visited(self):
        return self.is_visited