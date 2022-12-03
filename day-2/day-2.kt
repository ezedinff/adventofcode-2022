/**
* @author: Ezedin Fedlu
*/

import java.io.File
import java.io.FileNotFoundException
import java.util.*

fun main(args: Array<String>) {
    val input = File(args[0])
    val moves = parseInput(input)
    println("Part 1: ${part1(moves)}")
    println("Part 2: ${part2(moves)}")
}

fun part1(moves: List<Pair<String, String>>): Int {
    var score = 0
    for ((opponent, player) in moves) {
        val roundScore = playRoundPart1(opponent, player)
        score += roundScore
    }
    return score
}

fun part2(moves: List<Pair<String, String>>): Int {
    var score = 0
    for ((opponent, player) in moves) {
        val roundScore = playRoundPart2(opponent, player)
        score += roundScore
    }
    return score
}

fun playRoundPart1(opponent: String, player: String): Int {
    val opponentMove = moveMap[opponent]!!
    val playerMove = moveMap[player]!!
    val moveScoreMap = mapOf(
        "Rock" to mapOf("Scissors" to 0, "Paper" to 6, "Rock" to 3),
        "Paper" to mapOf("Rock" to 0, "Scissors" to 6, "Paper" to 3),
        "Scissors" to mapOf("Paper" to 0, "Rock" to 6, "Scissors" to 3)
    )
    return scoreMap[playerMove]!! + moveScoreMap[opponentMove]!![playerMove]!!
}

fun playRoundPart2(opponent: String, player: String): Int {
    val moveScoreMap = mapOf(
        "Rock" to mapOf("Scissors" to 6, "Paper" to 0, "Rock" to 3),
        "Paper" to mapOf("Rock" to 6, "Scissors" to 0, "Paper" to 3),
        "Scissors" to mapOf("Paper" to 6, "Rock" to 0, "Scissors" to 3)
    )
    val opponentMove = moveMap[opponent]!!
    val playerMove = recommendedMoveForResultMap[Pair(opponentMove, resultMap[player]!!)]!!
    return moveScoreMap[playerMove]!![opponentMove]!! + scoreMap[playerMove]!!
}

fun parseInput(input: File): List<Pair<String, String>> {
    val moves = mutableListOf<Pair<String, String>>()
    try {
        val scanner = Scanner(input)
        while (scanner.hasNextLine()) {
            val line = scanner.nextLine()
            moves.add(Pair(line[0].toString(), line[2].toString()))
        }
        scanner.close()
    } catch (e: FileNotFoundException) {
        e.printStackTrace()
    }
    return moves
}

val moveMap = mapOf(
    "R" to "Rock",
    "P" to "Paper",
    "S" to "Scissors"
)

val scoreMap = mapOf(
    "Rock" to 0,
    "Paper" to 3,
    "Scissors" to 6
)

val resultMap = mapOf(
    "W" to "Win",
    "D" to "Draw",
    "L" to "Lose"
)

val recommendedMoveForResultMap = mapOf(
    Pair("Rock", "Win") to "Paper",
    Pair("Rock", "Draw") to "Rock",
    Pair("Rock", "Lose") to "Scissors",
    Pair("Paper", "Win") to "Scissors",
    Pair("Paper", "Draw") to "Paper",
    Pair("Paper", "Lose") to "Rock",
    Pair("Scissors", "Win") to "Rock",
    Pair("Scissors", "Draw") to "Scissors",
    Pair("Scissors", "Lose") to "Paper"
)