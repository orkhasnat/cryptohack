from typing import Tuple
import random
import string
from math import gcd
from struct import pack, unpack

### ----------- RSA Crypto System ----------- ###


class RSA:
  """
  === RSA Crypto System ===
  """

  ### ----------- Helper Classes ----------- ###

  class Message:
    """
    handles Plaintext and Ciphertext conversion and vice-versa.
    """

    @staticmethod
    def convert2Int(plaintext: str) -> int:
      """
      Convert string to integer using struct.pack().
      - struct.pact(format="BB...",ord('h'),ord('i'),...) 
          returns byte string. Here 'B' means unsigned char.
      - int.from_bytes(byte_string,endianness)
      """
      return int.from_bytes(pack('B' * len(plaintext), *map(ord, plaintext)),
                            'big')

    @staticmethod
    def convertFromInt(ciphertext: int) -> str:
      """
      Convert integer to string using struct.unpack().
      - struct.unpack(format="BB...",byte_string)
          returns a tuple in this case a tuple of integers
      - int.bit_lenght() 
          returns number of bits excluding leading zeros e.g. 7 => 3.
      - to_bytes(byte_length,endianness)
          here byte_length is computed by padding the last byte and
          flooring the value after division by 8.
      - map  --> because unpack returns a tuple of integers
      - join --> convert the list of characters to a string.

      """
      byte_length = (ciphertext.bit_length() + 7) // 8
      return "".join(
          map(
              chr,
              unpack('B' * byte_length,
                     ciphertext.to_bytes(byte_length, 'big'))))

### ----------- RSA Core ----------- ###

  def __init__(self, bitSize: int = 128) -> None:
    """
    bitSize: bit size of the generated primes
    """
    # generate large prime numbers
    self.__p = RSA.__generatePrime(bitSize)
    self.__q = RSA.__generatePrime(bitSize)

    # ensure q and q is not the same
    while self.__p == self.__q:
      self.__q = RSA.__generatePrime(bitSize)

    self.__n = self.__p * self.__q
    self.__phi = (self.__p - 1) * (self.__q - 1)

    # generate public and private keypairs
    self.publicKey, self.__privateKey = self.__generateKeys()

  def __generateKeys(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Generate public-private keypairs.
    """

    # public key e such that, e<phi and co-prime to phi
    e = random.randint(2, self.__phi - 1)
    while gcd(e, self.__phi) != 1:
      e = random.randint(2, self.__phi - 1)

    # private key d such that, d is the modular inverse of e % phi.
    d = pow(e, -1, self.__phi)

    # return publicKey, __privateKey
    return (e, self.__n), (d, self.__n)

  def public_key(self) -> None:
    print(
        f"Your public key is `{self.publicKey[0]}` with n `{self.publicKey[1]}`"
    )

  def private_key(self) -> None:
    print(
        f"Your private key is `{self.__privateKey[0]}` with n `{self.__privateKey[1]}`"
    )

  def encrypt(self, plaintext: str, key: Tuple[int, int]) -> int:
    """
    encrypt the plaintext into ciphertext with public key.
    """
    e, n = key
    return pow(RSA.Message.convert2Int(plaintext), e, n)

  def decrypt(self, ciphertext: int) -> str:
    """
    decrypt the ciphertext into plaintext with private key.
    """
    d, n = self.__privateKey
    return self.Message.convertFromInt(pow(ciphertext, d, n))

  ### ----------- Utils ----------- ###
  @staticmethod
  def __generatePrime(bitSize: int) -> int:
    """
    generates bitSize long primes.
    """
    p = random.getrandbits(bitSize)

    # if even make odd
    if not p % 2:
      p += 1

    # loop until probable prime is found
    while not RSA.__miller_rabin_test(p):  # primality testing
      p += 2

    return p

  @staticmethod
  def __miller_rabin_test(num: int, iteration: int = 10) -> bool:
    """
    Miller-Rabin Test for primality.
    Credit: https://cp-algorithms.com/algebra/primality_tests.html#miller-rabin-primality-test
    """
    # base cases
    if num == 2:
      return True

    if num == 1 or num % 2 == 0:
      return False

    # represent n-1 as (2^s)*d
    s, d = 0, num - 1

    while not d % 2:
      s += 1
      d //= 2

    assert (2**s * d == num - 1)

    def check_composite(a):
      x = pow(a, d, num)

      if x == 1 or x == num - 1:
        return False  # probably prime

      for _ in range(s):
        x = (x * x) % num  # check for each a^((2^i)*d)

        if x == num - 1:
          return False  # probably prime

      return True  # definitely composite

    for _ in range(iteration):
      a = random.randint(2, num - 1)

      if check_composite(a):
        return False  # definitely composite

    return True  # probably prime


### ----------- testing ----------- ###
def test():
  alice = RSA(512)
  bob = RSA(512)
  eve = RSA(512)

  def gen_random_text():

    # length can only be upto keysize/8 bytes.
    length = random.randint(1, 2**6)

    text = ''.join(
        random.choice(string.ascii_letters + string.digits +
                      string.punctuation + string.whitespace)
        for _ in range(length))
    return (text, length)

  no_errors = True
  for i in range(0, 1000):
    text, length = gen_random_text()
    assertions = [
        # Alice sends OK
        ((alice.decrypt(alice.encrypt(text, alice.publicKey)) == text) == True,
         "A(A) --> A"),
        ((bob.decrypt(alice.encrypt(text, bob.publicKey)) == text) == True,
         "A(B) --> B"),
        # Bob sends OK
        ((bob.decrypt(bob.encrypt(text, bob.publicKey)) == text) == True,
         "B(B) --> B"),
        ((alice.decrypt(bob.encrypt(text, alice.publicKey)) == text) == True,
         "B(A) --> A"),
        # Alice and Bob dont send OK
        ((bob.decrypt(alice.encrypt(text, alice.publicKey)) == text) == False,
         "A(A) --> B"),
        ((alice.decrypt(bob.encrypt(text, bob.publicKey)) == text) == False,
         "B(B) --> A"),
        # eve cant eavesdrop
        ((eve.decrypt(alice.encrypt(text, alice.publicKey)) == text) == False,
         "A(A) --> E"),
        ((eve.decrypt(alice.encrypt(text, bob.publicKey)) == text) == False,
         "A(B) --> E"),
        ((eve.decrypt(bob.encrypt(text, alice.publicKey)) == text) == False,
         "B(A) --> E"),
        ((eve.decrypt(bob.encrypt(text, bob.publicKey)) == text) == False,
         "B(B) --> E")
    ]

    for condition, msg in assertions:
      try:
        assert condition
        # print(f"\033[92mTested OK {msg} with plaintext = `{text}` and of length {length}.\033[0m")

      except AssertionError:
        no_errors = False
        # print in red
        print(f"\033[1;91m{msg} failed with of length {length}.\033[0m")
  if no_errors:
    # print in green and bold
    print(f"\033[1;32mNo Errors!!! We are good to go!\033[0m")


### ----------- Execution Script ----------- ###

if __name__ == "__main__":

  while True:
    print("Welcome to RSA Cryptosytem.")
    if (choice :=
        input("Choose who you are?\n\t1.Alice\n\t2.Bob\n").lower()) in {
            '1', 'alice'
        }:
      print("Hello Alice!")
      person = 1
      break
    elif choice in {'2', 'bob'}:
      print("Hello Bob!")
      person = 2
      break
    else:
      print("Please Choose either Alice or Bob !!!")

  print("""
  Welcome to  the RSA cryptosystem.
  You have the following features, 
    - encrypt() message  with any public key.
      encrypt(message,any_public_key) => ciphertext
    - decrypt() message with your own private key.
      decrypt(ciphertext) => plaintext
    - public_key() 
      printout your public_key.
    - private_key()
      In case you want to printout your private_key.
  """)

  # Key Size
  size = input(
      "\nEnter your keysize: \nMust be a power of 2!!!\nLeave empty for default keysize=128\n"
  )
  is_power_of_two = lambda n: n > 0 and (n & (n - 1)) == 0
  if size:
    size = int(size)
    if not is_power_of_two(size):
      print("\033[1;31mInvalid Key Length.\nUsing Default.\033[0m")
      size = 128
  else:
    size = 128

  a = RSA(size)
  b = RSA(size)

  while True:
    print("\nOptions:")
    print("\t1. Encrypt a message")
    print("\t2. Decrypt a message")
    print("\t3. Print private key")
    print("\t4. Print public key")
    print("\t5. Test for Errors")
    print("\t0. Exit")

    if (choice := int(input("Enter the choice number: "))) == 1:
      message = input("\nEnter your message\n\t")
      if person == 1:
        ct = a.encrypt(message, b.publicKey)
        print(f'Ciphertext: \t `{ct}`')
      elif person == 2:
        ct = b.encrypt(message, a.publicKey)
        print(f'Ciphertext: \t `{ct}`')

    elif choice == 2:
      message = input("\nEnter your ciphertext\n\t")
      if person == 1:
        ct = b.decrypt(int(message))
        print(f'Message from Alice: \t `{ct}`')
      elif person == 2:
        ct = a.decrypt(int(message))
        print(f'Message from Bob: \t `{ct}`')

    elif choice == 3:
      if person == 1:
        a.public_key()
      elif person == 2:
        b.public_key()

    elif choice == 4:
      if person == 1:
        a.private_key()
      elif person == 2:
        b.private_key()

    elif choice == 5:
      print("== Starting Testing ==")
      test()

    elif choice == 0:
      break
    else:
      print("Invalid Choice")
