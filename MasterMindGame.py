import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def __init__(self, score=0):
        self.guesses = None
        self.digit = None
        self.score = score

    def play(self):
        clear()
        print("Lets start the game, your current score %f" % self.score)
        self.rules()
        self.set_digit()
        random_num = random.randint(10 ** (self.digit - 1), 10 ** self.digit - 1)
        print("I have decided a number, you can guess now:")
        self.guesses = []
        ask = self.try_guess(random_num)
        while True:
            if ask:
                break
            print("Current Score %.2f Try again, your  last guesses were" % self.score)
            print(self.guesses)
            ask = self.try_guess(random_num)

        print("Game over! your final score is %.f" % self.score)
        ask = input("Would you like to play again, from this score? (y/n)")
        if ask == "y":
            self.play()
        else:
            print("Thanks for playing!")

    def set_digit(self):
        print("How many digits do you want?")
        while True:
            self.digit = int(input("(1-8)->"))
            if self.digit < 1 or self.digit > 8:
                print("Please enter a number between 1 and 8")
            else:
                break

    def try_guess(self, target_num):
        """It will allow the user to guess a number,
        and returns
        True, to stop the game, in two cases,
        1. User didn't enter a number.
        2. User passed the guess game"""

        guess = input(f"Guess a {self.digit} digit number(leave blank to stop guess): ")
        if guess == "":
            return True
        guess = int(guess)
        self.guesses.append(guess)
        similar_score, similar_char = self.check_similar(guess, target_num)
        if similar_score == 1:
            self.score += 1 * self.digit * 10
            print("Congrats you guessed the correct number!")
            return True
        elif similar_score == 0:
            clear()
            print("Sorry you guessed the wrong number!")
            self.score += -1
        else:
            clear()
            print("Your guess was partly correct, ie %f percent" % (similar_score * 100))
            self.score += similar_score * 10

            print("The correct predictions were")
            print(" ".join(similar_char))

    @staticmethod
    def check_similar(guess, target):
        if guess == target:
            return 1, target
        else:
            guess_num = str(guess)
            target_num = str(target)
            correct = ['x'] * len(target_num)
            correct_digits = 0
            for i in range(min(len(guess_num), len(target_num))):
                if guess_num[i] == target_num[i]:
                    correct[i] = target_num[i]
                    correct_digits += 1
            return correct_digits / len(guess_num), correct

    @staticmethod
    def rules():
        rule = """
        The Rules are as follows
        1. For a number of digits the computer will guess a number
        2. If correctly guessed, you will get score (10 * #total_digits)
        3. If partly correct, you will get score (10 * (#correct_digits/#total_digits))
        4. Otherwise -1, when all digits are wrong"""
        print(rule)

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
