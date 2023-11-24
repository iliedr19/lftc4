from myscanner import MyScanner
from finiteautomation import FiniteAutomaton


def print_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except FileNotFoundError as e:
        print(e)


def run(file_path):
    scanner = MyScanner(file_path)
    scanner.scan()
    print_to_file(file_path.replace(".txt", "ST.txt"), str(scanner.get_symbol_table()))
    print_to_file(file_path.replace(".txt", "PIF.txt"), str(scanner.get_pif()))


def print_menu():
    print("1. Print states.")
    print("2. Print alphabet.")
    print("3. Print final states.")
    print("4. Print transitions.")
    print("5. Print initial state.")
    print("6. Print is deterministic.")
    print("7. Check if sequence is accepted by DFA.")


def options_for_dfa():
    finite_automaton = FiniteAutomaton("fa.txt")

    print("FA read from file.")
    print_menu()
    print("Your option: ")

    option = int(input())

    while option != 0:
        if option == 1:
            print("Final states: ")
            print(finite_automaton.get_states())
            print()
        elif option == 2:
            print("Alphabet: ")
            print(finite_automaton.get_alphabet())
            print()
        elif option == 3:
            print("Final states: ")
            print(finite_automaton.get_final_states())
            print()
        elif option == 4:
            print(finite_automaton.write_transitions())
        elif option == 5:
            print("Initial state: ")
            print(finite_automaton.get_initial_state())
            print()
        elif option == 6:
            print("Is deterministic?")
            print(finite_automaton.check_if_deterministic())
        elif option == 7:
            print("Your sequence: ")
            sequence = input()
            if finite_automaton.accepts_sequence(sequence):
                print("Sequence is valid")
            else:
                print("Invalid sequence")
        else:
            print("Invalid command!")

        print()
        print_menu()
        print("Your option: ")
        option = int(input())


def run_scanner():
    run("p1.txt")
    run("p2.txt")
    run("p3.txt")
    run("p1err.txt")


if __name__ == "__main__":
    print("1. FA")
    print("2. Scanner")
    print("Your option: ")

    option = int(input())

    if option == 1:
        options_for_dfa()
    elif option == 2:
        run_scanner()
    else:
        print("Invalid command!")
