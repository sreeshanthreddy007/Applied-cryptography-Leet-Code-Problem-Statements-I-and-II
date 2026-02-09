# Problem 2: Algebraic Structures
n = int(input("Enter value of n for Z_n: "))
Z = list(range(n))
print("Set Z_n =", Z)
# Closure
def is_closed_add():
    for a in Z:
        for b in Z:
            if (a + b) % n not in Z:
                return False
    return True
def is_closed_mul():
    for a in Z:
        for b in Z:
            if (a * b) % n not in Z:
                return False
    return True
# Inverses
def has_add_inverse():
    for a in Z:
        found = False
        for b in Z:
            if (a + b) % n == 0:
                found = True
        if not found:
            return False
    return True
def has_mul_inverse():
    for a in Z[1:]:
        found = False
        for b in Z:
            if (a * b) % n == 1:
                found = True
        if not found:
            return False
    return True
# Results
add_closed = is_closed_add()
mul_closed = is_closed_mul()
add_inv = has_add_inverse()
mul_inv = has_mul_inverse()
print("Closed under Addition:", add_closed)
print("Closed under Multiplication:", mul_closed)
print("Additive Inverse exists:", add_inv)
print("Multiplicative Inverse exists:", mul_inv)
# Decide structure
if add_closed and add_inv and not mul_inv:
    print("Structure: GROUP")
elif add_closed and mul_closed and not mul_inv:
    print("Structure: RING")
elif add_closed and mul_closed and mul_inv:
    print("Structure: FIELD")
else:
    print("Not a valid algebraic structure")
