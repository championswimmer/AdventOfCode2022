import { readLines } from "../commons/io.ts";

function main() {
  const lines = readLines("day-04/input.txt");
  let duplicateRanges = 0;
  let overlapRanges = 0;

  class Range {
    public min: number;
    public max: number;
    constructor(range: string) {
      const [min, max] = range.split("-").map((n) => parseInt(n));
      this.min = min;
      this.max = max;
    }
    isContaining(other: Range): boolean {
      return this.min <= other.min && this.max >= other.max;
    }
    isOverlapping(other: Range): boolean {
      let overlap = false;
      if (this.min <= other.min && this.max >= other.min) overlap = true;
      if (this.min <= other.max && this.max >= other.max) overlap = true;
      return overlap;
    }
  }

  lines.forEach((line) => {
    const [range1, range2] = line.split(",").map((r) => new Range(r));
    if (range1.isContaining(range2) || range2.isContaining(range1)) {
      duplicateRanges++;
    }

    if (range1.isOverlapping(range2) || range2.isOverlapping(range1)) {
      overlapRanges++;
    }
  });

  console.log(`Duplicate ranges: ${duplicateRanges}`);
  console.log(`Overlapping ranges: ${overlapRanges}`);
}

main();
