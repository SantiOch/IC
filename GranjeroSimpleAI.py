from simpleai.search import SearchProblem, breadth_first

class WolfSheepCabbage(SearchProblem):
    def __init__(self):
        # all start on left bank (0)
        super().__init__((0, 0, 0, 0))

    def is_goal(self, state):
        return state == (1, 1, 1, 1)

    def actions(self, state):
        f, w, s, c = state
        possible_actions = []

        # farmer moves alone
        new_state = (1-f, w, s, c)
        if self.is_valid(new_state):
            possible_actions.append('F')

        # farmer moves with wolf
        if f == w:
            new_state = (1-f, 1-f, s, c)
            if self.is_valid(new_state):
                possible_actions.append('FW')

        # farmer moves with sheep
        if f == s:
            new_state = (1-f, w, 1-f, c)
            if self.is_valid(new_state):
                possible_actions.append('FS')

        # farmer moves with cabbage
        if f == c:
            new_state = (1-f, w, s, 1-f)
            if self.is_valid(new_state):
                possible_actions.append('FC')

        return possible_actions

    def result(self, state, action):
        f, w, s, c = state
        nf = 1 - f

        if action == 'F':
            return (nf, w, s, c)
        if action == 'FW':
            return (nf, nf, s, c)
        if action == 'FS':
            return (nf, w, nf, c)
        if action == 'FC':
            return (nf, w, s, nf)

    def is_valid(self, state):
        f, w, s, c = state

        # wolf eats sheep
        if w == s and f != w:
            return False

        # sheep eats cabbage
        if s == c and f != s:
            return False

        return True

    def cost(self, state, action, state2):
        return 1


# Creamos el problema y buscamos solución
problem = WolfSheepCabbage()
result = breadth_first(problem)

print("Solution:")
for action, state in result.path():
    print(action, state)