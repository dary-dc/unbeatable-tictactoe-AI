
from players import HumanPlayer, UnbeatableComputer

class TicTacToe:
    def __init__(self):
        self.board_values = [" " for i in range(9)]
        self.winner = None
        self.players = [UnbeatableComputer("X"), HumanPlayer("O")]

    def print_board(self):
        print()
        for row in [self.board_values[j*3:(j+1)*3] for j in range(3)]:
            print("| " + " | ".join(row) + " |")

    def print_board_positions(self):
        print()
        board_positions = [str(n) for n, spot in enumerate(self.board_values)] # each position representes with a number, and converted to string
        for row in [board_positions[a*3:(a+1)*3] for a in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [n for n, spot in enumerate(self.board_values) if spot == " "]

    def available_moves_num(self):
        return len(self.available_moves())

    def make_move(self, spot, letter):
        self.board_values[spot] = letter
        return self.board_values

    def determine_winner(self, spot, letter):
        self.winner = letter if self.check_winner(spot) else None

    def there_is_empty_spot(self):
        return " " in self.board_values

    def check_winner(self, spot):
        row_ind = spot // 3
        row = self.board_values[row_ind*3:(row_ind+1)*3]
        row_win = all([self.board_values[spot] == letter for letter in row])
        
        col_ind = spot % 3
        col = [self.board_values[col_ind+(j*3)] for j in range(3)]
        col_win = all([self.board_values[spot] == letter for letter in col])

        diag_1_ind, diag_2_ind = [i for i in range(9) if i % 4 == 0], [i for i in range(2, 8) if i % 2 == 0]
        diag_1, diag_2 = [self.board_values[spot] for spot in diag_1_ind], [self.board_values[spot] for spot in diag_2_ind]
        diag_win = all([self.board_values[spot] == letter for letter in diag_1]) or all([self.board_values[spot] == letter for letter in diag_2])

        return any([row_win, col_win, diag_win])

    def provide_winner_letter(winner_letter):
        return winner_letter


def play(game, print_positions=True):
    if print_positions:
        game.print_board_positions()

    player_num = 0

    game.players.reverse()

    while game.there_is_empty_spot():
        spot = game.players[player_num].get_move(game)
        game.board_values = game.make_move(spot, game.players[player_num].letter)
        win = game.check_winner(spot)
        game.determine_winner(spot, game.players[player_num].letter)
        game.print_board()

        if win:
            return f"{game.winner} wins the game!!!"

        if print_positions:
            game.print_board_positions()

        player_num = 1 if player_num == 0 else 0

    return "It's a tie"

print(play(TicTacToe(), True))