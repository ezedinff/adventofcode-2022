/**
* @author: Ezedin Fedlu
*/

import java.io.File
import java.io.InputStream
import java.util.*

fun main(args: Array<String>) {
    val input = File(args[0]).readLines()
    val rucksacksPart1 = getRucksacksPart1(input)
    val rucksacksPart2 = getRucksacksPart2(input)
    println("Part 1: ${part1(rucksacksPart1)}")
    println("Part 2: ${part2(rucksacksPart2)}")
}

fun getRucksacksPart1(lines: List<String>): List<Pair<String, String>> {
    val rucksacks = mutableListOf<Pair<String, String>>()
    for (line in lines) {
        rucksacks.add(Pair(line.substring(0, line.length / 2), line.substring(line.length / 2)))
    }
    return rucksacks
}

fun part1(rucksacks: List<Pair<String, String>>): Int {
    var total = 0
    for (rucksack in rucksacks) {
        for (item in rucksack.first) {
            if (rucksack.second.contains(item)) {
                total += if (item.isLowerCase()) item.toInt() - 96 else item.toInt() - 38
                break
            }
        }
    }
    return total
}

fun getRucksacksPart2(lines: List<String>): List<List<String>> {
    val rucksacks = mutableListOf<List<String>>()
    for (i in 0 until lines.size step 3) {
        rucksacks.add(listOf(lines[i], lines[i + 1], lines[i + 2]))
    }
    return rucksacks
}

fun part2(rucksacks: List<List<String>>): Int {
    var total = 0
    for (rucksack in rucksacks) {
        for (item in rucksack[0]) {
            if (rucksack[1].contains(item) && rucksack[2].contains(item)) {
                total += if (item.isLowerCase()) item.toInt() - 96 else item.toInt() - 38
                break
            }
        }
    }
    return total
}
