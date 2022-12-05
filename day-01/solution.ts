import { readLines } from "../commons/io.ts";

function main () {

    const lines = readLines("day-01/input.txt");
    let elfCalorieSums: Array<number> = [];
    let currElfCalories = 0;
    lines.forEach((line) => {
        if (line !== "") {
            currElfCalories += Number(line);
        } else {
            elfCalorieSums.push(currElfCalories);
            currElfCalories = 0;
        }
    });
    elfCalorieSums = elfCalorieSums.sort((a, b) => b - a);
    console.log(elfCalorieSums[0] + elfCalorieSums[1] + elfCalorieSums[2]);

}

main()