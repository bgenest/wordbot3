from random import choice, randint
from tendies import tendies_or_no
from get import read_random_line
from fishingGame import fishingGame

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered.startswith('hey bot'):
      if 'how are you' in lowered:
          return (read_random_line('libraries/howYou.txt'))
      elif 'bye' in lowered:
          return (read_random_line('libraries/bye.txt'))
      elif 'roll dice' in lowered or 'roll the dice' in lowered:
          return f'You rolled: {randint(1, 6)}'
      elif 'tendies pls' in lowered or 'tendies please' in lowered:
          return f"Here you go: {tendies_or_no()}"
      elif 'cast me' in lowered:
          return f'You caught: {fishingGame()}'
      else:
          return (read_random_line('libraries/hello.txt'))
