# gen of range of nums as dict
def gen_dict():
    num_dict = {x: x for x in range(10)}
    yield num_dict


gen = gen_dict()
print(next(gen))
