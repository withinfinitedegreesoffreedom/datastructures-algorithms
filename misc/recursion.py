class Recursion:
    def __init__(self):
        pass

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def sumupton(self, n):
        if n == 1:
            return 1
        else:
            return n+self.sumupton(n-1)
        
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x * self.pow(x, n-1)

    def fastpow(self, x, n):
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                y = self.fastpow(x, n/2)
                return y * y
            else:
                return x * self.fastpow(x, n-1)

    def mod_exp(self, x, n, m):
        if n == 0:
            return 1
        elif n % 2 == 0:
            y = self.mod_exp(x, n/2, m)
            return (y * y) % m
        else:
            return (self.mod_exp(x, n, m) * self.mod_exp(x, n-1, m)) % m

    def fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

r = Recursion()
print(r.factorial(3))
print(r.sumupton(3))
print(r.pow(2, 3))
print(r.fibonacci(4))