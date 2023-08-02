hexstr = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

cipher = bytes.fromhex(hexstr)

fv_byte = cipher[0] ^ ord("c")

flag = "".join(map(lambda x: chr(x ^ fv_byte), cipher))

print(flag)