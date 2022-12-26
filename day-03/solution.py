import sys
import os
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from commons.io import readLines


def main():
  lines: List[str] = readLines("day-03/input.txt")
  ALPHABET: str = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  prioritySum1: int = 0

  # PART 01

  for line in lines:
    # split line into 2 parts at mid point
    first = line[0:len(line) // 2]
    second = line[len(line) // 2:]
    # find elements that are in both first and second
    intersection = list(set(first) & set(second))
    priority = ALPHABET.index(intersection[0])
    prioritySum1 += priority

  # PART 02
  prioritySum2 = 0
  # group lines into groups of 3
  for i in range(0, len(lines), 3):
    first = lines[i]
    second = lines[i + 1]
    third = lines[i + 2]
    # find elements that are in all 3 lines
    intersection = [char for char in first if char in second and char in third]
    priority = ALPHABET.index(intersection[0])
    prioritySum2 += priority

  print("Part 01: " + str(prioritySum1))
  print("Part 02: " + str(prioritySum2))


main()
