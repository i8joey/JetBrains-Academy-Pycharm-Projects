import random

status = ""
guess = ""
won = 0
lost = 0


def resetGame():
    winner = random.choice(["python", "java", "swift", "javascript"])
    blank = ["-" for x in winner]
    guessed = set()
    attempts = 8
    return [winner, blank, guessed, attempts]

def menuPrompt():
    print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    return input()


def checkWinner(guess1, winner, blank):
    if guess1 == winner or "".join(blank) == winner:
        print(winner)
        print(f"You guessed the word {winner}!")
        print("You survived!")
        return True


while True:
    print("H A N G M A N # 8 attempts\n")
    status = menuPrompt()
    if status == "results":
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
    if status == "exit":
        break
    if status == "play":
        gameData = resetGame()
        while True:
            if checkWinner(guess, gameData[0], gameData[1]):
                won += 1
                break
            print("".join(gameData[1]))
            print("Input a letter: > ", end="")
            guess = input()
            if len(guess) != 1:
                print("Please, input a single letter.\n")
                continue
            elif guess.isupper() is True or guess.isalpha() is False:
                print("Please, enter a lowercase letter from the English alphabet.\n")
                continue
            if gameData[0].find(guess) >= 0 and len(guess) == 1 and guess not in gameData[2]:
                for i in range(len(gameData[0])):
                    gameData[2].add(guess)
                    if gameData[0][i] == guess:
                        gameData[1][i] = guess
                print()
                continue
            elif guess not in gameData[2]:
                gameData[2].add(guess)
                print(f"That letter doesn't appear in the word.  # {gameData[3]} attempts\n")
            elif guess in gameData[2]:
                print(f"You've already guessed this letter.' # {gameData[3]} attempts\n")
                continue
            gameData[3] -= 1
            if gameData[3] == 0:
                print("You lost!")
                lost += 1
                break
