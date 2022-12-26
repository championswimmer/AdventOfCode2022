import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from commons.io import readLines


class Range:
  def __init__(self, range_str: str):
    self.min, self.max = map(int, range_str.split("-"))

  def is_containing(self, other: "Range") -> bool:
    return self.min <= other.min and self.max >= other.max

  def is_overlapping(self, other: "Range") -> bool:
    overlap = False
    if self.min <= other.min and self.max >= other.min:
      overlap = True
    if self.min <= other.max and self.max >= other.max:
      overlap = True
    return overlap

def main():
  lines = readLines("day-04/input.txt")
  duplicate_lines = 0
  overlap_lines = 0

  for line in lines:
    range1, range2 = map(lambda r: Range(r), line.split(","))
    if range1.is_containing(range2) or range2.is_containing(range1):
      duplicate_lines += 1

    if range1.is_overlapping(range2) or range2.is_overlapping(range1):
      overlap_lines += 1

  print(f"Duplicate lines: {duplicate_lines}")
  print(f"Overlap lines: {overlap_lines}")


main()
