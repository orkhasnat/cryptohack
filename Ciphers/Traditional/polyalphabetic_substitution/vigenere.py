from itertools import cycle

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)


def encode(inp: str, key: int) -> str:
  res = ""
  iter = cycle(key)
  for i in inp:
    res += chr(ord(i) - ord(ALPHABET[0]) + ord(iter))


def decode(inp: str, key: int) -> str:
  pass


inp = input()
agreed_key = "pascal"

# print(encode(inp, agreed_key))
# print(decode(inp, agreed_key))
print(decode(encode(inp, agreed_key), agreed_key))
