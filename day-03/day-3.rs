/* @author Ezedin Fedlu
 * @date 2021-12-03
 * @version 1.0
 * @brief Advent of Code 2022 Day 3
 */
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let input_file_path = std::env::args().nth(1).unwrap();
    let file = File::open(input_file_path).unwrap();
    let reader = BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        lines.push(line);
    }
    let mut rucksacks_part_1 = Vec::with_capacity(lines.len());
    let mut rucksacks_part_2 = Vec::with_capacity(lines.len());
    for line in &lines {
        rucksacks_part_1.push((line[0..line.len()/2].to_string(), line[line.len()/2..].to_string()));
    }
    for i in (0..lines.len()).step_by(3) {
        rucksacks_part_2.push((lines[i].to_string(), lines[i+1].to_string(), lines[i+2].to_string()));
    }
    println!("Part 1: {}", part_1(&rucksacks_part_1));
    println!("Part 2: {}", part_2(&rucksacks_part_2));

}

fn part_1(rucksacks: &Vec<(String, String)>) -> i32 {
    let mut total = 0;
    for rucksack in rucksacks {
        for item in rucksack.0.chars() {
            if rucksack.1.contains(item) {
                total += get_priority(&item);
                break;
            }
        }
    }
    total
}

fn part_2(rucksacks: &Vec<(String, String, String)>) -> i32 {
    let mut total = 0;
    for rucksack in rucksacks {
        for item in rucksack.0.chars() {
            if rucksack.1.contains(item) && rucksack.2.contains(item) {
                total += get_priority(&item);
                break;
            }
        }
    }
    total
}

fn get_priority(c: &char) -> i32 {
    if c.is_ascii_uppercase() {
        *c as i32 - 38
    } else {
        *c as i32 - 96
    }
}