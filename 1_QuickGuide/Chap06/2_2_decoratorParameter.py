def pre_str(pre=''):
    def decorator(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)
        return new_F
    return decorator

@pre_str('^_^')
def square_sum(a, b):
    return a**2 + b**2

print(square_sum(3, 4))