from pair import Pair

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def find_by_pos(self, pos):
        if len(self.table) <= pos.first or len(self.table[pos.first]) <= pos.second:
            raise IndexError("Invalid position")
        return self.table[pos.first][pos.second]

    def get_size(self):
        return self.size

    def find_position_of_term(self, elem):
        pos = self.hash(elem)
        if not self.table[pos]:
            return None
        for i, el in enumerate(self.table[pos]):
            if el == elem:
                return Pair(pos, i)
        return None

    def hash(self, key):
        sum_chars = sum(ord(c) for c in key)
        return sum_chars % self.size

    def contains_term(self, elem):
        return self.find_position_of_term(elem) is not None

    def add(self, elem):
        if self.contains_term(elem):
            return False
        pos = self.hash(elem)
        self.table[pos].append(elem)
        return True

    def __str__(self):
        computed_string = ""
        for i in range(len(self.table)):
            if self.table[i]:
                computed_string += f"{i} - {self.table[i]}\n"
        return computed_string
