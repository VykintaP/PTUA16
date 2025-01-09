def fibonacci_gen():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield a, b


gen = fibonacci_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
