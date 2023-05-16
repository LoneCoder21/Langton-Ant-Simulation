class Rule:
    def __init__(self, direction_to_turn, color):
        self.color = color
        self.direction_id = 0
        #map L and R to -1 and 1 respectively (used for ants)
        match direction_to_turn:
            case "R":
                self.direction_id = 1
            case "L":
                self.direction_id = -1