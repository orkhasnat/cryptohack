ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

normalise = lambda ch: ord(ch) - ord(ALPHABET[0])
denormalise = lambda x: chr(x + ord(ALPHABET[0]))


def encode(inp: str, key: int) -> str:
  res = []
  for x in inp:
    if x in ALPHABET:
      res.append((normalise(x) + key) % ALPHABET_SIZE)
      key = normalise(x)
    else:
      res.append(normalise(x))
  return "".join(map(lambda ch: denormalise(ch), res))


def decode(inp: str, key: int) -> str:
  res = []
  for x in inp:
    if x in ALPHABET:
      cipherChar = (normalise(x) - key) % ALPHABET_SIZE
      res.append(cipherChar)
      key = cipherChar
    else:
      res.append(normalise(x))
  return "".join(map(lambda ch: denormalise(ch), res))


inp = input()
agreed_key = 4

# print(encode(inp, agreed_key))
# print(decode(inp, agreed_key))
print(decode(encode(inp, agreed_key), agreed_key))
