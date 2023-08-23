ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)


def encode(inp: str, key: int) -> str:
  res = []
  for x in inp:
    if x in ALPHABET:
      res.append((ord(x) - ord(ALPHABET[0]) + key) % ALPHABET_SIZE)
      key = ord(x) - ord(ALPHABET[0])
    else:
      res.append(ord(x) - ord(ALPHABET[0]))
  return "".join(map(lambda ch: chr(ch + ord(ALPHABET[0])), res))


def decode(inp: str, key: int) -> str:
  res = []
  for x in inp:
    if x in ALPHABET:
      cipherChar = (ord(x) - ord(ALPHABET[0]) - key) % ALPHABET_SIZE
      res.append(cipherChar)
      key = cipherChar
    else:
      res.append(ord(x) - ord(ALPHABET[0]))
  return "".join(map(lambda ch: chr(ch + ord(ALPHABET[0])), res))


inp = input()
agreed_key = 4

# print(encode(inp, agreed_key))
# print(decode(inp, agreed_key))
print(decode(encode(inp, agreed_key), agreed_key))
