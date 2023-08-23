'''
Affine is the culmination of aditive and multiplicative ciphers
Its in the form ax+b
Here C = ((P*a % ALSize) + b) % AlSize
And P = ((C-b % ALSize) * a^-1 ) % ALSize
'''
###################
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)
###################


def encode(inp: str, mul: int, add: int) -> str:
  return "".join(
      map(
          lambda ch: chr(
              (((((ord(ch) - ord(ALPHABET[0])) * mul) % ALPHABET_SIZE) + add) %
               ALPHABET_SIZE) + ord(ALPHABET[0]))
          if ch in ALPHABET else ch, inp))


def decode(inp: str, mul: int, add: int) -> str:
  modInv = pow(mul, -1, ALPHABET_SIZE)
  return "".join(
      map(
          lambda ch: chr(
              (((((ord(ch) - ord(ALPHABET[0])) - add) % ALPHABET_SIZE) * modInv
                ) % ALPHABET_SIZE) + ord(ALPHABET[0]))
          if ch in ALPHABET else ch, inp))


inp = input()
a = 19
b = 7
# print(encode(inp, a, b))
print(decode(inp, a, b))
