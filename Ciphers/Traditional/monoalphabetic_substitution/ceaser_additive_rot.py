ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

normalise = lambda ch: ord(ch) - ord(ALPHABET[0])
denormalise = lambda x: chr(x + ord(ALPHABET[0]))


def encode(inp: str, key: int) -> str:
  return "".join(
      map(
          lambda ch: denormalise((normalise(ch) + key) % ALPHABET_SIZE)
          if ch in ALPHABET else ch, inp))


def decode(inp: str, key: int) -> str:
  return "".join(
      map(
          lambda ch: denormalise((normalise(ch) - key) % ALPHABET_SIZE)
          if ch in ALPHABET else ch, inp))


inp = input()
key = 19

# print(encode(inp, key))
# print(decode(inp, key))
print(decode(encode(inp, key), key))
