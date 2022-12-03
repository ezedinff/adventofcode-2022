/* @author Ezedin Fedlu
 * @date 2021-12-02
 * @version 1.0
 * @brief Advent of Code 2022 Day 2
 */

use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn main() {
    let input_file = Path::new(&std::env::args().nth(1).unwrap());
    let input = BufReader::new(File::open(input_file).unwrap());
    let mut moves: Vec<(String, String)> = Vec::new();

    for line in input.lines() {
        let line = line.unwrap();
        let line = line.split_whitespace().collect::<Vec<&str>>();
        moves.push((line[0].to_string(), line[2].to_string()));
    }

    let mut score = 0;
    for (opponent, player) in moves {
        let round_score = play_round_part_1(&opponent, &player);
        score += round_score;
    }

    println!("Part 1: {}", score);

    let mut score = 0;
    for (opponent, player) in moves {
        let round_score = play_round_part_2(&opponent, &player);
        score += round_score;
    }

    println!("Part 2: {}", score);
}

fn play_round_part_1(opponent: &str, player: &str) -> i32 {
    let move_score_map = [
        (("Rock", "Scissors"), 0),
        (("Rock", "Paper"), 6),
        (("Rock", "Rock"), 3),
        (("Paper", "Rock"), 0),
        (("Paper", "Scissors"), 6),
        (("Paper", "Paper"), 3),
        (("Scissors", "Paper"), 0),
        (("Scissors", "Rock"), 6),
        (("Scissors", "Scissors"), 3),
    ];
    let opponent_move = move_map(opponent);
    let player_move = move_map(player);
    let score = move_score_map
        .iter()
        .find(|((a, b), _)| a == &opponent_move && b == &player_move)
        .unwrap()
        .1;
    score_map(&player_move) + score
}

fn play_round_part_2(opponent: &str, player: &str) -> i32 {
    let move_score_map = [
        (("Rock", "Scissors"), 6),
        (("Rock", "Paper"), 0),
        (("Rock", "Rock"), 3),
        (("Paper", "Rock"), 6),
        (("Paper", "Scissors"), 0),
        (("Paper", "Paper"), 3),
        (("Scissors", "Paper"), 6),
        (("Scissors", "Rock"), 0),
        (("Scissors", "Scissors"), 3),
    ];
    let opponent_move = move_map(opponent);
    let player_move = recommended_move_for_result_map(&opponent_move, &result_map(player));
    let score = move_score_map
        .iter()
        .find(|((a, b), _)| a == &player_move && b == &opponent_move)
        .unwrap()
        .1;
    score + score_map(&player_move)
}

fn move_map(move_str: &str) -> &str {
    match move_str {
        "Rock" => "Rock",
        "Paper" => "Paper",
        "Scissors" => "Scissors",
        _ => panic!("Invalid move"),
    }
}

fn result_map(move_str: &str) -> &str {
    match move_str {
        "Rock" => "Lose",
        "Paper" => "Win",
        "Scissors" => "Tie",
        _ => panic!("Invalid move"),
    }
}

fn recommended_move_for_result_map(opponent_move: &str, result: &str) -> &str {
    match (opponent_move, result) {
        ("Rock", "Win") => "Paper",
        ("Rock", "Lose") => "Scissors",
        ("Rock", "Tie") => "Rock",
        ("Paper", "Win") => "Scissors",
        ("Paper", "Lose") => "Rock",
        ("Paper", "Tie") => "Paper",
        ("Scissors", "Win") => "Rock",
        ("Scissors", "Lose") => "Paper",
        ("Scissors", "Tie") => "Scissors",
        _ => panic!("Invalid move"),
    }
}

fn score_map(move_str: &str) -> i32 {
    match move_str {
        "Rock" => 0,
        "Paper" => 6,
        "Scissors" => 3,
        _ => panic!("Invalid move"),
    }
}