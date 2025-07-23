# Hashing immutable objects
string_hash = hash("hello")
int_hash = hash(123)
float_hash = hash(3.14)
tuple_hash = hash((1, 2, 3))

print(f"Hash of 'hello': {string_hash}")
print(f"Hash of 123: {int_hash}")
print(f"Hash of 3.14: {float_hash}")
print(f"Hash of (1, 2, 3): {tuple_hash}")

# Attempting to hash mutable objects will raise a TypeError
try:
    list_hash = hash([1, 2, 3])
except TypeError as e:
    print(f"Error hashing list: {e}")