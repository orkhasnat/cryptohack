from pwn import xor
# from itertools import cycle

cipher = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e2634511501040e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)

flagpart = b"crypto{"

key = xor(cipher[:len(flagpart)], flagpart) + b'y'

flag = xor(cipher, key)  # xor cycles by itself

print(flag.decode("utf-8").split('}')[0] + '}')