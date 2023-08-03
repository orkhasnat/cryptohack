'''
bit confused about the whole bezouts identity thing
'''


def extended_euclidean_mod_inverse(a, b):
  '''
  Neso -- https://www.youtube.com/watch?v=0cUV_x0do2c&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII
  using extended euclidean can be  used to compute modular inverse of a*x = 1 mod b also can be done by M.I=pow(a,-1,b)
  we can only compute M.I if a and b are coprimes. we firstly need to check if  gcd(a,b) == 1
  also we  can write it this way t1* a + t2* b = gcd(a,b) = 1 where t1,t2 are called Bézout’s identity.
  the algo can only work when a>b
  returns M.I
  '''
  M = b
  if a < b:
    a, b = b, a
  t1, t2 = 0, 1
  r = a % b
  while r != 0:
    q = a // b
    r = a % b
    # this function could have been used; quotient, remainder = divmod(a, b)
    a, b = b, r
    t = t1 - q * t2
    t1, t2 = t2, t
  if a != 1:  # basically a is the gcd of original a and b
    return None
  return t1 % M  # same as t1 if t1 > 0 else t1 + M


def extended_euclidean_bezouts_identity(a, b):
  '''
  not clear on the math!!!
  Bézout's identity states that for any two integers a and b, there exist integers x and y such that their greatest common divisor (GCD) can be expressed as a linear combination of a and b. The equation is given by: gcd(a, b) = a*x + b*y

  '''

  x0, x1, y0, y1 = 1, 0, 0, 1

  while b != 0:
    q = a // b
    r = a % b
    # this function could have been used; quotient, remainder = divmod(a, b)
    a, b = b, r

    # this updates maintain the relationship -- a*x0 + b*y0 = a    and    a*x1 + b*y1 = b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
  return x0, y0  #  here x0 is also the M.I of a*M=1%b but negative M.I needs to handled


# print(extended_euclidean_mod_inverse(11, 26))

p, q = 26513, 32321
a, b = extended_euclidean_bezouts_identity(p, q)
print(f"crypto{{{a},{b}}}")
