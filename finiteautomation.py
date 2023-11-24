class FiniteAutomaton:
    def __init__(self, file_path):
        self.elem_separator = ";"
        self.is_deterministic = False
        self.initial_state = ""
        self.states = []
        self.alphabet = []
        self.final_states = []
        self.transitions = {}
        self.read_from_file(file_path)

    def read_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.states = lines[0].strip().split(self.elem_separator)
                self.initial_state = lines[1].strip()
                self.alphabet = lines[2].strip().split(self.elem_separator)
                self.final_states = lines[3].strip().split(self.elem_separator)

                for line in lines[4:]:
                    transition_components = line.strip().split()
                    if (
                        transition_components[0] in self.states
                        and transition_components[2] in self.states
                        and transition_components[1] in self.alphabet
                    ):
                        transition_states = (transition_components[0], transition_components[1])
                        if transition_states not in self.transitions:
                            self.transitions[transition_states] = {transition_components[2]}
                        else:
                            self.transitions[transition_states].add(transition_components[2])
            self.is_deterministic = self.check_if_deterministic()
        except FileNotFoundError as e:
            print(e)

    def check_if_deterministic(self):
        return all(len(states) <= 1 for states in self.transitions.values())

    def get_states(self):
        return self.states

    def get_initial_state(self):
        return self.initial_state

    def get_alphabet(self):
        return self.alphabet

    def get_final_states(self):
        return self.final_states

    def get_transitions(self):
        return self.transitions

    def write_transitions(self):
        result = "Transitions: \n"
        for transition, state_set in self.transitions.items():
            result += f"<{transition[0]}, {transition[1]}> -> {state_set}\n"
        return result

    def accepts_sequence(self, sequence):
        if not self.is_deterministic:
            return False
        if len(sequence) == 0:
            return self.initial_state in self.final_states

        current_state = self.initial_state

        for symbol in sequence:
            transition = (current_state, symbol)
            if transition not in self.transitions:
                return False
            current_state = next(iter(self.transitions[transition]))

        return current_state in self.final_states
