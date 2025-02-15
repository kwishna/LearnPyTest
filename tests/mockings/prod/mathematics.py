from operator import add, imul
class Calculations:
    def summation(self, *args):
        return add(args)

    def div_mod(self, a, b):
        return divmod(a, b)

if __name__ == '__main__':
    c = Calculations()
    print(c.div_mod(5, 4))