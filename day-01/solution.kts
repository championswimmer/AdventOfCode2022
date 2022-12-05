@file:Include("../commons/io.kts")

fun main() {
    val lines: List<String> = readLines("day-01/input.txt")
    var elfCalories = ArrayList<Int>()
    var currElfCalories = 0
    lines.forEach { line ->
        if (line != "") {
            currElfCalories += line.toInt()
        } else {
            elfCalories.add(currElfCalories)
            currElfCalories = 0
        }
    }
    elfCalories.sortDescending()
    println(elfCalories[0] + elfCalories[1] + elfCalories[2])
}

main()