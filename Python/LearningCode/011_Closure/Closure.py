def add_out(x):
    def add_inside(y): return x + y
    return add_inside

out = add_out(2)
print(out(10))
print(out(12))