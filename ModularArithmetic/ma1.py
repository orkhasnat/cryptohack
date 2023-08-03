'''
Fermats Little Theorem:

for any prime number p, a positive integer and a not divisible by p
a^p-1 is congruent to 1 mod p ie a^(p-1) ≡ 1 mod p

also it says a^p mod p = a ie a^p ≡ a mod p

'''
print(pow(7675, 65537) % 65537 == 7675)
print(pow(767589096, 65537) % 65537 == 767589096 % 65537)  #==19752
# print(1)