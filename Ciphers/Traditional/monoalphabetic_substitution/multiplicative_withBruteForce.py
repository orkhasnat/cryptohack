from typing import List, Tuple

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

normalise = lambda ch: ord(ch) - ord(ALPHABET[0])
denormalise = lambda x: chr(x + ord(ALPHABET[0]))


def computePossibleKeys(start, end, mod) -> List[Tuple[int, int]]:
  res = []
  for i in range(start, end + 1):
    try:
      res.append((i, pow(i, -1, mod)))
    except ValueError:
      pass
  return res


# remember bodmas
def encode(inp: str, key: int) -> str:
  return "".join(
      map(
          lambda ch: denormalise(((normalise(ch) * key) % ALPHABET_SIZE))
          if ch in ALPHABET else ch, inp))


# remember bodmas
def decode(inp: str, key: int) -> str:
  modInv = pow(key, -1, ALPHABET_SIZE)
  return "".join(
      map(
          lambda ch: denormalise(((normalise(ch) * modInv) % ALPHABET_SIZE))
          if ch in ALPHABET else ch, inp))


def decodeBruteForce(inp: str):
  possibleKeys = computePossibleKeys(1, ALPHABET_SIZE, ALPHABET_SIZE)
  [print(f"Key {i} : {decode(inp,i)}") for i, _ in possibleKeys]


inp = input()
key = 19
# print(encode(inp, key))
# print(decode(inp, key))
# decodeBruteForce(inp)
print(decode(encode(inp, key), key))