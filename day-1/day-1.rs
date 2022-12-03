/* @author Ezedin Fedlu
 * @date 2021-12-01
 * @version 1.0
 * @brief Advent of Code 2022 Day 1
 */
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn parse_input(input_file: &str) -> Vec<Vec<i32>> {
    let file = File::open(input_file).unwrap();
    let reader = BufReader::new(file);
    let mut elves: Vec<Vec<i32>> = Vec::new();
    let mut elf: Vec<i32> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        if line == "" {
            elves.push(elf);
            elf = Vec::new();
        } else {
            elf.push(line.parse::<i32>().unwrap());
        }
    }
    elves.push(elf);
    elves
}

fn find_largest_elf(elves: &Vec<Vec<i32>>) -> i32 {
    let mut total_elves_calories: Vec<i32> = Vec::new();
    for elf in elves {
        total_elves_calories.push(elf.iter().sum());
    }
    *total_elves_calories.iter().max().unwrap()
}

fn find_top_three_elves(elves: &Vec<Vec<i32>>) -> i32 {
    let mut total_elves_calories: Vec<i32> = Vec::new();
    for elf in elves {
        total_elves_calories.push(elf.iter().sum());
    }
    total_elves_calories.sort_by(|a, b| b.cmp(a));
    total_elves_calories.iter().take(3).sum()
}

fn part_1(elves: &Vec<Vec<i32>>) -> i32 {
    find_largest_elf(elves)
}

fn part_2(elves: &Vec<Vec<i32>>) -> i32 {
    find_top_three_elves(elves)
}

fn main() {
    let input_file = Path::new(&std::env::args().nth(1).unwrap());
    let elves = parse_input(input_file);
    println!("Part 1: {}", part_1(&elves));
    println!("Part 2: {}", part_2(&elves));
}