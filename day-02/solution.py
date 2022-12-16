import sys
import os
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from commons.io import readLines

def main():
  lines: List[str] = readLines("day-02/input.txt")
  PRECOMPUTED = {
    "A X": 1 + 3,     # rock rock          DRAW
    "A Y": 2 + 6,     # rock paper         WIN
    "A Z": 3 + 0,     # rock scissors      LOSE
    "B X": 1 + 0,     # paper rock         LOSE
    "B Y": 2 + 3,     # paper paper        DRAW
    "B Z": 3 + 6,     # paper scissors     WIN
    "C X": 1 + 6,     # scissors rock      WIN
    "C Y": 2 + 0,     # scissors paper     LOSE
    "C Z": 3 + 3,     # scissors scissors  DRAW
  }

  PRECOMPUTED2 = {
    "A X": 3 + 0,     # rock       LOSE    scissors
    "A Y": 1 + 3,     # rock       DRAW    rock
    "A Z": 2 + 6,     # rock       WIN     paper
    "B X": 1 + 0,     # paper      LOSE    rock
    "B Y": 2 + 3,     # paper      DRAW    paper
    "B Z": 3 + 6,     # paper      WIN     scissors
    "C X": 2 + 0,     # scissors   LOSE    paper
    "C Y": 3 + 3,     # scissors   DRAW    scissors
    "C Z": 1 + 6,     # scissors   WIN     rock
  }

  totalScore = 0

  for line in lines:
    lineScore = PRECOMPUTED2[line]
    totalScore += lineScore

  print(totalScore)

main()