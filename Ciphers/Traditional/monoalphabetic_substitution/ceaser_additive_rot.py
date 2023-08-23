ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)


def encode(inp: str, key: int) -> str:
  return "".join(
      map(
          lambda ch: chr(((ord(ch) - ord(ALPHABET[0]) + key) % ALPHABET_SIZE) +
                         ord(ALPHABET[0])) if ch in ALPHABET else ch, inp))


def decode(inp: str, key: int) -> str:
  return "".join(
      map(
          lambda ch: chr(((ord(ch) - ord(ALPHABET[0]) - key) % ALPHABET_SIZE) +
                         ord(ALPHABET[0])) if ch in ALPHABET else ch, inp))


inp = input()
key = 19

# print(encode(inp, key))
print(decode(inp, key))
