class ProgramInternalForm:
    def __init__(self):
        self.token_position_pair = []
        self.types = []

    def add(self, pair, type):
        self.token_position_pair.append(pair)
        self.types.append(type)

    def __str__(self):
        computed_string = ""
        for i in range(len(self.token_position_pair)):
            computed_string += (
                str(self.token_position_pair[i].first)
                + " - "
                + str(self.token_position_pair[i].second)
                + " -> "
                + str(self.types[i])
                + "\n"
            )
        return computed_string
