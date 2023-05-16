class Cell:
    def __init__(self, rule_state_id=0):
        self.rule_state_id = rule_state_id

    def getRuleID(self):
        return self.rule_state_id
        
    def nextRule(self, modAmount):
        self.rule_state_id += 1
        self.rule_state_id %= modAmount
        #increases to next rule and modulo cycles the rules