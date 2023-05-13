class Rule:
    def __init__(self, color, direction_to_turn, next_color):
        self.color = color
        self.direction_to_turn = direction_to_turn
        self.next_color = next_color

    def get_next_direction(self, current_direction):
        if self.direction_to_turn == "left":
            if current_direction == "up":
                return "left"
            elif current_direction == "down":
                return "right"
            elif current_direction == "left":
                return "down"
            elif current_direction == "right":
                return "up"
        elif self.direction_to_turn == "right":
            if current_direction == "up":
                return "right"
            elif current_direction == "down":
                return "left"
            elif current_direction == "left":
                return "up"
            elif current_direction == "right":
                return "down"