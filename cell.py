class Cell:
    def __init__(self, rule_state_id=0):
        self.rule_state_id = rule_state_id

    def getRuleID(self):
        return self.rule_state_id