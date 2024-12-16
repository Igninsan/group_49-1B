from logic import game
from decouple import config

attempts_amount = config('ATTEMPTS_AMOUNT', cast=int)
base_money = config('BASE_MONEY', cast=int)
random_range = config('RANDOM_RANGE').split()

game(base_money, random_range, attempts_amount)