import { readLines } from "../commons/io.ts";

function main() {
  const lines = readLines("day-06/input.txt");
  const input = lines[0];

  // Part 1
  function checkAll4Different(a: string, b: string, c: string, d: string) {
    return a !== b && a !== c && a !== d && b !== c && b !== d && c !== d;
  }

  for (let i = 3; i < input.length; i++) {
    const a = input[i - 3];
    const b = input[i - 2];
    const c = input[i - 1];
    const d = input[i];
    if (checkAll4Different(a, b, c, d)) {
      console.log("Marker is at ", i+1);
      break;
    }
  }

  // Part 2

  function checkStringHasDistinctChars(str: string) {
    const set = new Set();
    for (let i = 0; i < str.length; i++) {
      set.add(str[i]);
    }
    return set.size === str.length;
  }

  for (let i = 13; i < input.length; i++) {
    const check = input.slice(i - 13, i+1);
    if (checkStringHasDistinctChars(check)) {
      console.log("Marker is at ", i+1);
      break;
    }
  }
}

main();
