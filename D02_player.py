class Player:

    def __init__(self):
        pass

    def next_turn(self, other_guy_turn, *args):
        pass

    def reset(self):
        pass

class Cooperative(Player):
    turn = "coop"

    def __init__(self):
        pass

    def next_turn(self, other_guy_turn, *args):
        return Cooperative.turn

    def __str__(self):
        return "Cooperative"

class Cheater(Player):
    turn = "cheat"

    def __init__(self):
        pass

    def next_turn(self, other_guy_turn, *args):
        return Cheater.turn

    def __str__(self):
        return "Cheater"

class Copycat(Player):

    def __init__(self):
        self.other_guy_turn = "coop"

    def next_turn(self, other_guy_turn, *args):
        return other_guy_turn

    def __str__(self):
        return "Copycat"

class Grudger(Player):

    def __init__(self):
        self.mode = "Cooperative"

    def next_turn(self, other_guy_turn, *args):
        if self.mode == "Cheater":
            return "cheat"
        if other_guy_turn == "cheat":
            self.mode = "Cheater"
            return "cheat"
        return "coop"

    def reset(self):
        self.mode = "Cooperative"

    def __str__(self):
        return "Grudger"

class Detective(Player):

    def __init__(self):
        self.partner_turns = []
        self.start_turns = ["coop", "cheat", "coop", "coop"]
        self.mode = "Detective"

    def next_turn(self, other_guy_turn, *args):
        if self.mode == "Detective":
            self.partner_turns.append(other_guy_turn)
            if len(self.partner_turns) == 4:
                self.mode = "Cheater"
                if self.partner_turns.count("cheat") == 1:
                    self.mode = "Copycat"
        if self.start_turns:
            return self.start_turns.pop(0)
        else:
            if self.mode == "Copycat":
                return other_guy_turn
            return "cheat"

    def reset(self):
        self.partner_turns = []
        self.start_turns = ["coop", "cheat", "coop", "coop"]
        self.mode = "Detective"

    def __str__(self):
        return "Detective"

class Imposter(Player):
    
    def __init__(self):
        self.partner_turns = []
        self.mode = "Copycat"

    def next_turn(self, other_guy_turn, *args):
        if self.mode == "Copycat":
            self.partner_turns.append(other_guy_turn)
            if len(self.partner_turns) == args[0]:
                self.mode = "Cheater"
        if self.mode == "Cheater":
            return "cheat"
        else:
            return other_guy_turn

    def reset(self):
        self.partner_turns = []
        self.mode = "Copycat"

    def __str__(self):
        return "Imposter"





    
