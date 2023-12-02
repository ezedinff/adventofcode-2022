# @author: Ezedin Fedlu
# @date: 2023-12-02
# @version: 1.0.0
# @description: Advent of Code 2023 - Day 1

def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")

def sum_of_all_calibration(content):
    result = 0
    for line in content:
        numbers = []
        for char in line:
            if char in "0123456789":
                numbers.append(char)
        result += int(numbers[0] + numbers[-1])
    
    return result

def sum_of_all_calibration_with_words(content):
    result = 0
    for line in content:
        numbers = []
        for i in range(len(line)):
            if line[i] in "0123456789":
                numbers.append(line[i])
            numbers_in_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            for word in numbers_in_words:
                if line[i:i+len(word)] == word:
                    numbers.append(str(numbers_in_words.index(word)))

        result += int(numbers[0] + numbers[-1])
    
    return result


if __name__ == '__main__':
    content = read_input("./input.txt")
    print(f"Part one solution: {sum_of_all_calibration(content)}")
    print(f"Part two solution: {sum_of_all_calibration_with_words(content)}")