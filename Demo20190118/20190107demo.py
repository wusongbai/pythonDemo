
class calc(object):
    def add(self, a, b):
        res = a + b
        return res


if __name__ == '__main__':
    c1 = calc()
    result = c1.add(3, 6)
    print(result)
