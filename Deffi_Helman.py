import random
import primesieve

class DiffieHellman:
    def __init__(self, secret_num, p, g):
        self.p = p
        self.g = g
        self.secret_num = secret_num
        self.key = pow(g, secret_num) % p

    def get_key(self):
        return self.key

    def get_secret_key(self, companion_key):
        return pow(companion_key, self.secret_num) % self.p





g = primesieve.nth_prime(random.randint(50, 150))
p = primesieve.nth_prime(random.randint(50, 150))
Alisa = DiffieHellman(random.randint(1, 500), p, g)
Bob = DiffieHellman(random.randint(1, 500), p, g)
print('Alisa key:', Alisa.get_secret_key(Alisa.get_key()))
print('Bob key:', Bob.get_secret_key(Bob.get_key()))  
