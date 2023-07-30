print("Here is your flag:")

# typical iterative approach  in a one-liner
# flag = "".join(chr(ord(ch) ^ 13) for ch in "label")

# pointlessly complicated using functional approach
flag = "".join(map(lambda ch: chr(ord(ch) ^ 13), "label"))

print(
    f"crypto{{{flag}}}"
)  # in order to escape the {} we need to provide 3 pairs of curly braces.
