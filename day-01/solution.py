import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from commons.io import readLines

from typing import List

def main():
  lines: List[str] = readLines("day-01/input.txt")

  elf_calorie_sums: List[int] = []
  curr_elf_calories: int = 0
  for line in lines:
    if line != "":
      curr_elf_calories += int(line)
    else:
      elf_calorie_sums.append(curr_elf_calories)
      curr_elf_calories = 0
  elf_calorie_sums = sorted(elf_calorie_sums, reverse=True)
  print(elf_calorie_sums[0] + elf_calorie_sums[1] + elf_calorie_sums[2])

main()
