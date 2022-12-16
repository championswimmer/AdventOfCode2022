import { readLines } from "../commons/io.ts";

function main() {
  const lines = readLines("day-03/input.txt");
  const ALPHABET = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

  let prioritySum1 = 0;

  // PART 01

  lines.forEach((line) => {
    // split line into 2 parts at mid point
    const first = line.slice(0, line.length / 2);
    const second = line.slice(line.length / 2);
    // find elements that are in both first and second
    const intersection = first
      .split("")
      .filter((char) => second.includes(char));
    const priority = ALPHABET.indexOf(intersection[0]);
    prioritySum1 += priority;
  });

  // PART 02
  let prioritySum2 = 0;
  // group lines into groups of 3
  for (let i = 0; i < lines.length; i += 3) {
    const first = lines[i];
    const second = lines[i + 1];
    const third = lines[i + 2];
    // find elements that are in all 3 lines
    const intersection = first
      .split("")
      .filter((char) => second.includes(char) && third.includes(char));
    const priority = ALPHABET.indexOf(intersection[0]);
    prioritySum2 += priority;
  }

  console.log("Part 1", prioritySum1);
  console.log("Part 2", prioritySum2);
}

main();
