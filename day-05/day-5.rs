use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() {
    let input_file_path = std::env::args().nth(1).unwrap();
    let file = File::open(input_file_path).unwrap();
    let reader = BufReader::new(file);
    let crates = parse_crates(reader.lines());
    let program = parse_program(reader.lines());
    println!("Part 1: {}", part_1(&crates, &program));
    println!("Part 2: {}", part_2(&crates, &program));
}

fn parse_crates(lns: &Vec<String>) -> Vec<Vec<char>> {
    let mut lines = Vec::new();
    for line in lns {
        if line.starts_with("1") {
            break;
        }
        lines.push(line.clone());
        line.clear();
    }
    let n = line.trim().split(' ').last().unwrap().parse::<usize>().unwrap();
    let mut crates = vec![vec![]; n];
    while let Some(line) = lines.pop() {
        for i in 0..n {
            let p = 1 + 4*i;
            if p < line.len() && line.chars().nth(p).unwrap() != ' ' {
                crates[i].push(line.chars().nth(p).unwrap());
            }
        }
    }
    crates.iter_mut().for_each(|crate_| crate_.reverse());
    crates
}

fn parse_program(lns: &Vec<String>) -> Vec<Vec<char>> {
    let mut program = vec![];
    let mut line = String::new();
    for line in lns {
        let mut iter = line.trim().split(' ');
        iter.next();
        let k = iter.next().unwrap().parse::<usize>().unwrap();
        iter.next();
        let fm = iter.next().unwrap().parse::<usize>().unwrap();
        iter.next();
        let to = iter.next().unwrap().parse::<usize>().unwrap();
        program.push((k, fm, to));
        line.clear();
    }
    program
}


fn part_1(crates: &Vec<Vec<char>>, program: &Vec<(usize, usize, usize)>) -> String {
    let mut crates = crates.iter().map(|crate_| crate_.clone()).collect::<Vec<Vec<char>>>();
    for (k, fm, to) in program {
        for _ in 0..*k {
            crates[*to - 1].push(crates[*fm - 1].pop().unwrap());
        }
    }

    crates.iter().map(|crate_| crate_.last().unwrap()).collect::<String>()
}

fn part_2(crates: &Vec<Vec<char>>, program: &Vec<(usize, usize, usize)>) -> String {
    let mut crates = crates.iter().map(|crate_| crate_.clone()).collect::<Vec<Vec<char>>>();
    for (k, fm, to) in program {
        let mut tmp = vec![];
        for _ in 0..*k {
            tmp.push(crates[*fm - 1].pop().unwrap());
        }
        for _ in 0..*k {
            crates[*to - 1].push(tmp.pop().unwrap());
        }

    }

    crates.iter().map(|crate_| crate_.last().unwrap()).collect::<String>()
}