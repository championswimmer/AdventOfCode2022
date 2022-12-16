@file:Include("../commons/io.kts")

fun main() {
    val lines: List<String> = readLines("day-03/input.txt")

    val ALPHABET = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    var prioritySum1 = 0

    // PART 01

    lines.forEach { line ->
        // split line into 2 parts at mid point
        val first = line.slice(0 until line.length / 2)
        val second = line.slice(line.length / 2 until line.length)
        // find elements that are in both first and second
        val intersection = first.split("").filter { char -> char.isNotEmpty() && second.contains(char) }
        val priority = ALPHABET.indexOf(intersection[0])
        prioritySum1 += priority
    }

    // PART 02
    var prioritySum2 = 0
    // group lines into groups of 3
    for (i in 0 until lines.size step 3) {
        val first = lines[i]
        val second = lines[i + 1]
        val third = lines[i + 2]
        // find elements that are in all 3 lines
        val intersection = first.split("").filter { char -> char.isNotEmpty() && second.contains(char) && third.contains(char) }
        val priority = ALPHABET.indexOf(intersection[0])
        prioritySum2 += priority
    }

    println("Part 1 $prioritySum1")
    println("Part 2 $prioritySum2")
}

main()
