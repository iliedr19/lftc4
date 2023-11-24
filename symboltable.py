from hashtable import HashTable

class SymbolTable:
    def __init__(self, size):
        self.hash_table = HashTable(size)

    def find_by_pos(self, pos):
        return self.hash_table.find_by_pos(pos)

    def get_hash_table(self):
        return self.hash_table

    def get_size(self):
        return self.hash_table.get_size()

    def find_position_of_term(self, term):
        return self.hash_table.find_position_of_term(term)

    def contains_term(self, term):
        return self.hash_table.contains_term(term)

    def add(self, term):
        return self.hash_table.add(term)

    def __str__(self):
        return str(self.hash_table)
