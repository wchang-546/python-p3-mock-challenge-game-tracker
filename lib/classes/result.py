class Result:

    all = []

    def __init__(self, player, game, score):
        self.score = score 
        self.player = player
        self.game = game
        Result.all.append(self)

        game.results(self)
        game.players(player)

        player.results(self)
        player.games_played(game)


    @property 
    def score(self):
        return self._score 

    @score.setter 
    def score(self, score): 
        if isinstance(score, int) and 1 <= score <= 5000: 
            self._score = score
        else: 
            raise Exception
        
    @property
    def player(self):
        return self._player 
    
    @player.setter 
    def player(self, player): 
        from classes.player import Player 
        if isinstance(player, Player): 
            self._player = player 
        else:
            raise Exception
    
    @property
    def game(self): 
        return self._game 
    
    @game.setter 
    def game(self, game):
        from classes.game import Game 
        if isinstance(game, Game):
            self._game = game 
        else: 
            raise Exception

