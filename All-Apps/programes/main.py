from parsers import parse
import random

user_input = input("enter lower bound and upper bound divided a comma (e.g, 2,10)")

parsed = parse(user_input)

rad = random.randint(parsed['lower_bound'], parsed['upper_bound'])
print(rad)