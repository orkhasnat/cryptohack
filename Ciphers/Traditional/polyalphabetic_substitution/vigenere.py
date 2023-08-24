from itertools import cycle

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

normalise = lambda ch: ord(ch) - ord(ALPHABET[0])
denormalise = lambda x: chr(x + ord(ALPHABET[0]))


def encode(inp: str, key: int) -> str:
  iter = cycle(key)
  return "".join(
      map(
          lambda x: denormalise(
              (normalise(x) + normalise(next(iter))) % ALPHABET_SIZE)
          if x in ALPHABET else x, inp))


def decode(inp: str, key: int) -> str:
  iter = cycle(key)
  return "".join(
      map(
          lambda x: denormalise(
              (normalise(x) - normalise(next(iter))) % ALPHABET_SIZE)
          if x in ALPHABET else x, inp))


inp = input()
agreed_key = "pascal"

# print(encode(inp, agreed_key))
# print(decode(inp, agreed_key))
print(decode(encode(inp, agreed_key), agreed_key))
