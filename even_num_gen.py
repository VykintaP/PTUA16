# gen for even nums

def even_nums():
    num = 2
    while True:
        num += 2
        yield num


gen = even_nums()
print(next(gen))
print(next(gen))
