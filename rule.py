class Rule:
    def __init__(self, color, direction_to_turn):
        self.color = color
        self.direction_to_turn = direction_to_turn
        self.direction_id = 0
        match direction_to_turn:
            case "R":
                self.direction_id = 1
            case "L":
                self.direction_id = -1