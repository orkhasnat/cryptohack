from typing import List

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

normalise = lambda ch: ord(ch) - ord(ALPHABET[0])
denormalise = lambda x: chr(x + ord(ALPHABET[0]))


def str2Mat(s: str) -> List[List[int]]:
  pass


def encode(inp: str, key: List[List[int]]) -> str:
  pass


def decode(inp: str, key: List[List[int]]) -> str:
  pass


inp = input()
keystring = "lgdbaqmhecurnifxvsokzywtp"  # no j in key

# print(encode(inp, agreed_key))
# print(decode(inp, agreed_key))
# print(decode(encode(inp, key), key))
