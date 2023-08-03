'''
a * b ≡ 1 (mod p)
to calculate b, the Modular Inverse.

We will use Fermat's little theorem in the case of a not divisible by p:

  a^(p-1) ≡ 1 mod p <=> a^(p-1) % p = 1

If we continue this equation we can get the following:

  a^(p-1) ≡ 1 mod p
  a^(p-1) * a^(-1) ≡ a^(-1) mod p
  a^(p-2) * a * a^(-1) ≡ a^(-1) mod p
  a^(p-2) ≡ a^(-1) mod p 
  <=>
  a^(p-2) % p = a^(-1)

So we can now find the inverse element a^(-1).

For our example, we have:

  3 * d ≡ 1 mod 13
  # Which can be written
  3^(13-2) % 13 = 9

It is important to note that Fermat's Little Theorem only applies when "p" is a prime number and "a" is not divisible by "p." In other cases, different methods, such as the Extended Euclidean Algorithm, are used to find modular inverses.

'''

print(pow(3, -1, 13))
