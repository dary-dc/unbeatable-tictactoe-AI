import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputer(Player):
    def get_move(self, game):
        spot_num = random.choice(game.available_moves())
        return spot_num

class UnbeatableComputer(Player):
    def get_move(self, game):
        spot = self.minimax(game, self.letter)["spot"]
        return spot
    
    def minimax(self, game, player):
        max_player = self.letter
        min_player = "X" if player == "O" else "O"

        if game.winner:
            return {"spot": None, 
                    "score": 1 * (game.available_moves_num() + 1) if min_player == max_player \
                       else -1 * (game.available_moves_num() + 1)}
        elif not game.there_is_empty_spot():
            return {"spot": None, "score": 0}

        if player == max_player:
            best = {"spot": None, "score": -float('inf')}
        else:
            best = {"spot": None, "score": float('inf')}

        for possible_move in game.available_moves():
            game.make_move(possible_move, player) 
            game.determine_winner(possible_move, player)
    
            score = self.minimax(game, min_player)
            score["spot"] = possible_move

            game.make_move(possible_move, " ")
            game.determine_winner(possible_move, player)
        
            if player == max_player:
                if score["score"] > best["score"]:
                    best = score
            else:
                if score["score"] < best["score"]:
                    best = score
       
        return best
    

class HumanPlayer(Player):
    def get_move(self, game):
        while True:
            try:
                spot = int(input(f"\n{self.letter}'s turn. Input move (0-8).\nAvailable moves are: {game.available_moves()}, choose one: "))
                if spot in game.available_moves():
                    return spot
                else:
                    raise ValueError
            except ValueError:
                print("Please, follow the instructions.")
