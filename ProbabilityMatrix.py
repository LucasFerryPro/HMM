class ProbabilityMatrix:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix

    def calculate_probabilities(self):
        probabilities = {}
        transitions = self.transition_matrix.get_transitions()
        for page, trans in transitions.items():
            total = sum(trans.values())
            if total > 0:
                probabilities[page] = {dst: round((count / total) * 100, 2) / 100 for dst, count in trans.items()}
            else:
                probabilities[page] = {dst: 0 for dst in transitions}
        return probabilities