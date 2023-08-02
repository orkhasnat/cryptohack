from math import gcd
import random


def eucledean_gcd(a, b):
  while a % b != 0:
    r = a % b
    a = b
    b = r
  return b


def chatgpt_gcd(a, b):
  while b:
    a, b = b, a % b
  return a


def chatgpt_recurse_gcd(a, b):
  return a if b == 0 else chatgpt_recurse_gcd(b, a % b)


euclead = lambda a, b: euclead(b, a % b) if b else a

# testing my implementation


def testing_my_func():
  rand = lambda: random.randint(23, 8523)
  test = [(rand(), rand()) for _ in range(100)]
  # return [False for a, b in test if gcd(a, b) != eucledean_gcd(a, b)]

  # returns the number of false or inequalities
  return sum(gcd(a, b) != eucledean_gcd(a, b) for a, b in test)


# print(testing_my_func())

a, b = 66528, 52920

print(eucledean_gcd(a, b))
