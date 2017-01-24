def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line(5))

def line_conf2(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf2(1, 1)
line2 = line_conf2(4, 5)
print(line1(5), line2(5))