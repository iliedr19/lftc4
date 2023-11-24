from symboltable import SymbolTable
from programinternalform import ProgramInternalForm
from pair import Pair
from finiteautomation import FiniteAutomaton
import re


class MyScanner:
    def __init__(self, file_path):
        self.operators = ["+", "-", "*", "/", "%", "<=", ">=", "==", "!=", "<", ">", "="]
        self.separators = ["{", "}", "(", ")", "[", "]", ":", ";", " ", ",", "\t", "\n", "'", "\""]
        self.reserved_words = ["spatiu", "linie_noua", "citeste", "scrie", "daca", "altfel", "pentru", "cat_timp", "returneaza", "start", "finish", "tab", "int", "string", "char", "array"]
        self.file_path = file_path
        self.symbol_table = SymbolTable(100)
        self.pif = ProgramInternalForm()

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read().replace("\t", "")
            return content
        except FileNotFoundError as e:
            print(e)

    def create_list_of_program_elems(self):
        content = self.read_file()
        if content is None:
            return None

        # Split content into words
        words = re.findall(r'[a-zA-Z_]\w*|[+\-*/%=<>!]=?|[-+]?\d+|\S', content)

        # Escape metacharacters in separators
        separators_string = ''.join(re.escape(sep) for sep in self.separators)

        # Tokenize words
        tokens = []
        for word in words:
            subtokens = re.split(f'({separators_string})', word)
            tokens.extend(self.tokenize(subtokens))

        return tokens

    def tokenize(self, tokens_to_be):
        resulted_tokens = []
        is_string_constant = False
        is_char_constant = False
        created_string = ""
        number_line = 1
        number_column = 1

        for t in tokens_to_be:
            if t == "\"":
                if is_string_constant:
                    created_string += t
                    resulted_tokens.append((created_string, (number_line, number_column)))
                    created_string = ""
                else:
                    created_string += t
                is_string_constant = not is_string_constant
            elif t == "'":
                if is_char_constant:
                    created_string += t
                    resulted_tokens.append((created_string, (number_line, number_column)))
                    created_string = ""
                else:
                    created_string += t
                is_char_constant = not is_char_constant
            elif t == "\n":
                number_line += 1
                number_column = 1
            else:
                if is_string_constant:
                    created_string += t
                elif is_char_constant:
                    created_string += t
                elif t != " ":
                    resulted_tokens.append((t, (number_line, number_column)))
                    number_column += 1

        return resulted_tokens

    def scan(self):
        tokens = self.create_list_of_program_elems()
        lexical_error_exists = False

        if not tokens:
            return

        for t in tokens:
            token = t[0]
            if token in self.reserved_words:
                self.pif.add(Pair(token, Pair(-1, -1)), 2)
            elif token in self.operators:
                self.pif.add(Pair(token, Pair(-1, -1)), 3)
            elif token in self.separators:
                self.pif.add(Pair(token, Pair(-1, -1)), 4)
            elif re.match("^'[1-9]'|'[a-zA-Z]'|\"[0-9]*[a-zA-Z ]*\"$", token) or FiniteAutomaton("fa_integer_constant.txt").accepts_sequence(token):
                self.symbol_table.add(token)
                self.pif.add(Pair(token, self.symbol_table.find_position_of_term(token)), 0)
            elif FiniteAutomaton("FA_identifier.txt").accepts_sequence(token):
                self.symbol_table.add(token)
                self.pif.add(Pair(token, self.symbol_table.find_position_of_term(token)), 1)
            else:
                line, column = t[1]
                print(f"Error at line: {line} and column: {column}, invalid token: {token}")
                lexical_error_exists = True

        if not lexical_error_exists:
            print("Program is lexically correct!")

    def get_pif(self):
        return self.pif

    def get_symbol_table(self):
        return self.symbol_table
