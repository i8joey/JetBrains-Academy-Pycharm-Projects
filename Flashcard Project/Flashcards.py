import json
from io import StringIO
import argparse


class DuplicateError(Exception):
    pass


class WrongAnswerError(Exception):
    pass


# checks the term/definition to see if there are duplicates
# if there are duplicates, it will ask for a new term/definition
def check_cards(deck, term_or_def):
    if term_or_def == "term":
        cards = list(deck.keys())
    else:
        cards = list(deck.values())
    while True:
        word = save_input(input())
        try:
            if word in cards:
                raise DuplicateError
            else:
                return word
        except DuplicateError:
            save_print("The {type} \"{word}\" already exists. Try again:".format(type=term_or_def, word=word))


# checks the answers
def check_answer(deck, card_word, card_answer, answer):
    if card_answer == answer:
        save_print("Correct!")
        return True
    elif answer not in list(deck.values()):
        save_print("Wrong. The right answer is \"{right}\".".format(right=card_answer))
        log_dict[card_word] += 1
        return True
    for i in deck.items():
        if i[1] == answer:
            save_print("Wrong. The right answer is \"{right}\", but your definition is correct for \"{word}\".".format(
                right=card_answer, word=i[0]))
            break


def add_card(deck):
    save_print("The card:")
    word = check_cards(deck, "term")
    save_print("The definition of the card:")
    definition = check_cards(deck, "definition")
    deck[word] = definition
    save_print(f"The pair (\"{word}\":\"{definition}\") has been added.")
    log_dict[word] = 0


def remove_card(deck):
    save_print("Which card?")
    word = save_input(input())
    try:
        deck.pop(word)
        save_print("The card has been removed.")
    except KeyError:
        save_print(f"Can't remove \"{word}\": there is no such card.")


# exports current deck to file name of choice and saves the amount of wrong answers for each card
def export_card(deck, run, export):
    if not run:
        save_print("File name:")
        name = save_input(input())
    else:
        name = export
    with open(name, "w") as file:
        json.dump(deck, file)
    save_print(f"{len(deck)} cards have been saved.")
    with open(name + "log", "w") as x:
        json.dump(log_dict, x)


# takes file name and imports deck if it exists
def import_card(deck, run, imp):
    if not run:
        save_print("File name:")
        name = save_input(input())
    else:
        name = imp
    try:
        with open(name, "r") as file:
            data = json.load(file)
            for i in data.items():
                deck[i[0]] = i[1]
        save_print(f"{len(deck)} cards have been loaded.")
        with open(name + "log", "r") as x:
            data =json.load(x)
            for i in data.items():
                log_dict[i[0]] = i[1]
    except FileNotFoundError and UnboundLocalError and FileNotFoundError:
        save_print("File not found.")


# saves all user input and program output information
def log():
    save_print("File name:")
    name = save_input(input())
    memory_file.seek(0)
    with open(name, "w") as log:
        for i in memory_file:
            log.write(i)
    save_print("The log has been saved.")


# asks X amount of questions from the current deck
def ask(deck):
    length = len(deck)
    words_list = list(deck.keys())
    definition_list = list(deck.values())
    save_print("How many times to ask?")
    num = int(save_input(input()))
    for x in range(num):
        save_print(f"Print the definition of \"{words_list[x % length]}\":")
        answer = save_input(input())
        check_answer(deck, words_list[x % length], definition_list[x % length], answer)


# uses saved data to see the cards with the most amount of wrong answers
def hardest_card():
    try:
        sorted_dict = dict(sorted(log_dict.items(), key=lambda x: -x[1]))
        hardest = list(sorted_dict.keys())
        if not sorted_dict[hardest[0]] == 0:
            if sorted_dict[hardest[0]] == sorted_dict[hardest[1]]:
                save_print(f"The hardest cards are {hardest[0]}, {hardest[1]}. You have {sorted_dict[hardest[0]]} errors answering them.")
            else:
                save_print(f"The hardest card is {hardest[0]}. You have {sorted_dict[hardest[0]]} errors answering it.")
        else:
            raise KeyError
    except KeyError:
        save_print("There are no cards with errors.")
    except IndexError:
        save_print("There are no cards with errors.")


def reset_stats():
    for i in log_dict.keys():
        log_dict[i] = 0
    save_print("Card statistics have been reset.")


# used to save user inputs and program outputs to log
def save_print(string):
    print(string)
    memory_file.write(string)


def save_input(string):
    memory_file.write(string)
    return string


deck = {}
log_dict = {}
memory_file = StringIO()


# Reads command line arguments if any in order to import cards from file
parser = argparse.ArgumentParser()
parser.add_argument("--import_from")
parser.add_argument("--export_to")
args = parser.parse_args()
if args.import_from is not None:
    import_card(deck, True, args.import_from)
    save_print(f"{len(deck)} cards have been loaded.")


# runs the console menu
while True:
    save_print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    action = save_input(input())
    if action == "add":
        add_card(deck)
    elif action == "remove":
        remove_card(deck)
    elif action == "import":
        import_card(deck, False, None)
    elif action == "export":
        export_card(deck, False, None)
    elif action == "ask":
        ask(deck)
    elif action == "exit":
        card_count = len(deck)
        if args.export_to is not None:
            export_card(deck, True, args.export_to)
            save_print(f"{card_count} cards have been saved.")
        save_print("Bye bye!")
        break
    elif action == "log":
        log()
    elif action == "reset stats":
        reset_stats()
    elif action == "hardest card":
        hardest_card()
