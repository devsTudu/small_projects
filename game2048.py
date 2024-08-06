import random

rule = """
Commands are as follows:
W : to move up
S : to move down
D : to move right
A : to move left
"""


class Game:
    def __init__(self):
        self.score = 0
        self.board = []

    def play(self):
        for i in range(4):
            self.board.append([0]*4)
        print(rule)
        self.add_new_2()

    def add_new_2(self):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        while self.board[r][c] != 0:
            r = random.randint(0, 3)
            c = random.randint(0, 3)
        self.board[r][c] = 2

    def show_board(self):
        for i in range(4):
            print(self.board[i])

    def get_current_state(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 2048:
                    print("Congratulations! You did it")
                    return "Won"

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1] or self.board[i][j] == self.board[i+1][j]:
                    return "Not Over"

        for j in range(3):
            if self.board[3][j] == self.board[3][j+1] or self.board[j][3] == self.board[j+1][3]:
                return "Not Over"
        return "Lost"

    @staticmethod
    def compress(mat):
        changed = False
        new_mat = []
        for i in range(4):
            new_mat.append([0]*4)

        # Here we will shift entries of each cell to its extreme left by rows
        for i in range(4):
            pos = 0

            for j in range(4):
                if mat[i][j] != 0:
                    new_mat[i][pos] = mat[i][j]
                    if j != pos:
                        changed = True
                    pos += 1
        return changed, new_mat

    @staticmethod
    def merge(mat):
        changed = False
        for i in range(4):
            for j in range(3):
                if (mat[i][j] != 0) and (mat[i][j] == mat[i][j+1]):
                    changed = True
                    mat[i][j] *= 2
                    mat[i][j+1] = 0
        return changed, mat

    @staticmethod
    def reverse(mat):
        new_mat = []
        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(mat[i][3-j])
        return new_mat

    @staticmethod
    def transpose(mat):
        new_mat = []
        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(mat[j][i])
        return new_mat

    def move_left(self):
        changed_1, new_mat = self.compress(self.board)
        changed_2, new_mat = self.merge(new_mat)
        changed = changed_1 or changed_2

        _, self.board = self.compress(new_mat)

        return changed

    def move_right(self):
        self.board = self.reverse(self.board)
        changed = self.move_left()
        self.board = self.reverse(self.board)

        return changed

    def move_up(self):
        self.board = self.transpose(self.board)
        changed = self.move_left()
        self.board = self.transpose(self.board)

        return changed

    def move_down(self):
        self.board = self.transpose(self.board)
        changed = self.move_right()
        self.board = self.transpose(self.board)

        return changed

    def game_move(self, char):
        char = char.upper()
        if char == "W":
            self.move_up()
        elif char == "S":
            self.move_down()
        elif char == "D":
            self.move_right()
        elif char == "A":
            self.move_left()
        else:
            return False
        return True

def main():
    game = Game()
    game.play()
    game.show_board()
    print(game.get_current_state())

    while True:
        x = input("Press a command :")
        if not game.game_move(x):
            print("Invalid input")
            continue
        print(game.get_current_state())
        if game.get_current_state() == "Not Over":
            game.add_new_2()
        else:
            break
        game.show_board()


if __name__ == "__main__":
    main()
    print("Game Over")

