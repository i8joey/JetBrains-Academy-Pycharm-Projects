
class FlashCard:

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition


print("Input the number of cards:")
number_of_cards = int(input())
cards = []
for x in range(number_of_cards):
    print(f"The term for card #{x + 1}:")
    term = input()
    print(f"The definition for card #{x + 1}:")
    cards.append(FlashCard(term, input()))
for x in range(number_of_cards):
    print(f"Print the definition of \"{cards[x].word}\":")
    answer = input()
    if answer == cards[x].definition:
        print("Correct!")
    else:
        print(f"Wrong. The right answer is \"{cards[x].definition}\"")
