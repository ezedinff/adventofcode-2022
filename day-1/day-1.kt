/**
* @author: Ezedin Fedlu
*/

import java.io.File
import java.io.FileNotFoundException
import java.util.*

fun parseInput(inputFile: File): List<List<Int>> {
    val elves = mutableListOf<List<Int>>()
    var elf = mutableListOf<Int>()
    try {
        Scanner(inputFile).use { scanner ->
            while (scanner.hasNextLine()) {
                val line = scanner.nextLine()
                if (line == "") {
                    elves.add(elf)
                    elf = mutableListOf()
                } else {
                    elf.add(line.toInt())
                }
            }
        }
    } catch (e: FileNotFoundException) {
        e.printStackTrace()
    }
    elves.add(elf)
    return elves
}

fun findLargestElf(elves: List<List<Int>>): Int {
    var largestElf = 0
    for (elf in elves) {
        val totalCalories = elf.sum()
        if (totalCalories > largestElf) {
            largestElf = totalCalories
        }
    }
    return largestElf
}

fun findTopThreeElves(elves: List<List<Int>>): Int {
    val totalCalories = mutableListOf<Int>()
    for (elf in elves) {
        totalCalories.add(elf.sum())
    }
    totalCalories.sortDescending()
    return totalCalories.take(3).sum()
}

fun part1(elves: List<List<Int>>): Int {
    return findLargestElf(elves)
}

fun part2(elves: List<List<Int>>): Int {
    return findTopThreeElves(elves)
}

fun main(args: Array<String>) {
    val inputFile = File(args[0])
    val elves = parseInput(inputFile)
    println("Part 1: ${part1(elves)}")
    println("Part 2: ${part2(elves)}")
}