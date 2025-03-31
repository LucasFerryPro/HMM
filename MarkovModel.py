from TransitionMatrix import TransitionMatrix
from ProbabilityMatrix import ProbabilityMatrix

class MarkovModel:
    def __init__(self, pages):
        self.transition_matrix = TransitionMatrix(pages)
        self.probability_matrix = ProbabilityMatrix(self.transition_matrix)

    def update(self, src, dst):
        self.transition_matrix.update(src, dst)

    def get_transitions(self):
        return self.transition_matrix.get_transitions()

    def get_probabilities(self):
        return self.probability_matrix.calculate_probabilities()