import random
import sys

class RPS:
    def __init__(self):
        print('Ready to play Rock, Paper, Scissors!!')
        self.moves: dict = {'rock':'🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score: int = 0
        self.ai_score: int = 0

    def play_game(self):
        user_move: str = input(
            "\nMake your move (rock, paper, scissors) or type 'exit' to quit:\n>> "
        ).lower()
        
        if user_move == 'exit':
            print(f"\nThanks for playing Rock Paper Scissors!")
            print(f"Final Score → You: {self.user_score} | AI: {self.ai_score}")
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)


    def display_moves(self, user_move: str, ai_move: str):
        print('----------')
        print(f"You: {self.moves[user_move]}")
        print(f"ai: {self.moves[ai_move]}")
        print('----------')

    def check_moves(self, user_move: str, ai_move: str):
        wins_against: dict = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        if user_move == ai_move:
            print("It's a tie!")
        elif wins_against[user_move] == ai_move:
            self.user_score += 1
            print("You win this round!")
        else:
            self.ai_score += 1
            print("AI wins this round!")

        print(f'Score: You: {self.user_score} | AI: {self.ai_score}')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
