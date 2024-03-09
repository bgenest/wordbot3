from random import randint, choice
from get import read_random_line


def fishingGame():
  max = 5000
  i = randint(0,max)
  fish = read_random_line('libraries/tendies.txt')
  print(i)
  if i == max:
    return read_random_line('libraries/superrarefish.txt')
  if i <= 3125:
    return "A common fish " + read_random_line('libraries/commonfish.txt')
  if i > 3125 and i <= 4500:
    return "An uncommon fish: " + read_random_line('libraries/uncommonfish.txt')
  if i > 4500 and i < 5000:
    return "A rare fish! :" + read_random_line('libraries/rarefish.txt')
