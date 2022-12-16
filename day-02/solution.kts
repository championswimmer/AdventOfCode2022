@file:Include("../commons/io.kts")

fun main() {
    val lines: List<String> = readLines("day-02/input.txt")
    var totalScore = 0
    
    val PRECOMPUTED: Map<String, Int> = mapOf(
        "A X" to 1 + 3,     // rock rock          DRAW
        "A Y" to 2 + 6,     // rock paper         WIN
        "A Z" to 3 + 0,     // rock scissors      LOSE
        "B X" to 1 + 0,     // paper rock         LOSE
        "B Y" to 2 + 3,     // paper paper        DRAW
        "B Z" to 3 + 6,     // paper scissors     WIN
        "C X" to 1 + 6,     // scissors rock      WIN
        "C Y" to 2 + 0,     // scissors paper     LOSE
        "C Z" to 3 + 3,     // scissors scissors  DRAW
    )

    val PRECOMPUTED2: Map<String, Int> = mapOf(
        "A X" to 3 + 0,     // rock       LOSE    scissors
        "A Y" to 1 + 3,     // rock       DRAW    rock
        "A Z" to 2 + 6,     // rock       WIN     paper
        "B X" to 1 + 0,     // paper      LOSE    rock
        "B Y" to 2 + 3,     // paper      DRAW    paper
        "B Z" to 3 + 6,     // paper      WIN     scissors
        "C X" to 2 + 0,     // scissors   LOSE    paper
        "C Y" to 3 + 3,     // scissors   DRAW    scissors
        "C Z" to 1 + 6,     // scissors   WIN     rock
    )
    
    for (line in lines) {
        val lineScore: Int = PRECOMPUTED2.get(line)!!
        totalScore += lineScore
    }

    println(totalScore)

}

main()