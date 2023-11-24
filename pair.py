class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def __str__(self):
        return f"({str(self.first)}, {str(self.second)})"

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return self.first == other.first and self.second == other.second

    def __hash__(self):
        return hash((self.first, self.second))
