class TransitionMatrix:
    def __init__(self, pages):
        self.pages = pages
        self.transitions = {page: {p: 0 for p in pages} for page in pages}

    def update(self, src, dst):
        if src in self.pages and dst in self.pages:
            self.transitions[src][dst] += 1

    def get_transitions(self):
        return self.transitions