from random import choice, randint
from get import read_random_line

def tendies_or_no():
  i = randint(0,1000)
  tender = read_random_line('libraries/tendies.txt')
  noTender = choice([
                '  just kidding LOL',
                '  actually we ran out...'])
  if i == 1000:
    response = "...You've...beaten me....you won: https://imgur.com/XWcnoLH"
  if i > 400:
    response = noTender
  else:
    response = tender
  return response
    