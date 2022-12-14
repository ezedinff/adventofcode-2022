'''
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
'''

'''
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''

# @author: Ezedin Fedlu
# @date: 2021-12-02
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 2
import sys
from pathlib import Path
from typing import List, Tuple
move_map = {
    "A": "Rock", "B": "Paper", "C": "Scissors",
    "X": "Rock", "Y": "Paper", "Z": "Scissors",
}

score_map = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

result_map = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}

recommended_move_for_result_map = {
    ("Rock", "Win"): "Paper",
    ("Rock", "Draw"): "Rock",
    ("Rock", "Lose"): "Scissors",
    ("Paper", "Win"): "Scissors",
    ("Paper", "Draw"): "Paper",
    ("Paper", "Lose"): "Rock",
    ("Scissors", "Win"): "Rock",
    ("Scissors", "Draw"): "Scissors",
    ("Scissors", "Lose"): "Paper",
}


def parse_input(input_file: Path) -> List[Tuple[str, str]]:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    return [(line[0], line[2]) for line in lines]


def play_round_part_1(opponent: str, player: str) -> int:
    opponent_move = move_map[opponent]
    player_move = move_map[player]
    move_score_map = {
        ("Rock", "Scissors"): 0,
        ("Rock", "Paper"): 6,
        ("Rock", "Rock"): 3,
        ("Paper", "Rock"): 0,
        ("Paper", "Scissors"): 6,
        ("Paper", "Paper"): 3,
        ("Scissors", "Paper"): 0,
        ("Scissors", "Rock"): 6,
        ("Scissors", "Scissors"): 3,
    }
    return score_map[player_move] + move_score_map[(opponent_move, player_move)]


def part_1(input_file: Path) -> int:
    moves = parse_input(input_file)
    score = 0

    for opponent, player in moves:
        round_score = play_round_part_1(opponent, player)
        score += round_score
    return score


def part_2(input_file: Path) -> int:
    moves = parse_input(input_file)
    score = 0
    for opponent, player in moves:
        round_score = play_round_part_2(opponent, player)
        score += round_score
    return score


def play_round_part_2(opponent: str, player: str) -> int:
    move_score_map = {
        ("Rock", "Scissors"): 6,
        ("Rock", "Paper"): 0,
        ("Rock", "Rock"): 3,
        ("Paper", "Rock"): 6,
        ("Paper", "Scissors"): 0,
        ("Paper", "Paper"): 3,
        ("Scissors", "Paper"): 6,
        ("Scissors", "Rock"): 0,
        ("Scissors", "Scissors"): 3,
    }
    opponent_move = move_map[opponent]
    player_move = recommended_move_for_result_map[(
        opponent_move, result_map[player])]
    return move_score_map[(player_move, opponent_move)] + score_map[player_move]


def main():
    input_file = Path(sys.argv[1])
    print(f"Part 1: {part_1(input_file)}")
    print(f"Part 2: {part_2(input_file)}")


if __name__ == "__main__":
    main()




