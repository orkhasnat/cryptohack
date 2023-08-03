'''
11 ≡ x mod 6
8146798528947 ≡ y mod 17 

x,y which is smaller
'''

x, y = 11 % 6, 8146798528947 % 17

print(x if x < y else y)
