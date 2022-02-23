__version__ = '0.1' # 2021/07/21
__author__ = 'Ramon Abud Alcala'

#class DivAlg:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.quotient = self.quotient()
        self.remainder = self.remainder()

    def quotient(self):
        return self.num // self.den

    def remainder(self):
        return self.num % self.den


#class EuclidAlg:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.table = self.table()
        self.gcd = self.gcd()
        self.extended_table = self.extended_table()

    def table(self):

        remainders_quotients_table = {"remainders": [self.num, self.den], "quotients": ['', '']}
        r0 = remainders_quotients_table["remainders"][0] # = a
        r = remainders_quotients_table["remainders"][1]  # = b
        while r != 0:
            q = DivAlg(r0, r).quotient
            remainders_quotients_table["quotients"].append(q)
            r = DivAlg(r0, r).remainder
            r0 = remainders_quotients_table["remainders"][-1]
            remainders_quotients_table["remainders"].append(r)

        return remainders_quotients_table

    def gcd(self):
        return self.table["remainders"][-2]

    def extended_table(self):

        extended_euclid_table = self.table
        extended_euclid_table["s"] = [0, 1]
        extended_euclid_table["t"] = [1, 0]
        for i in range(2, len(extended_euclid_table["quotients"])):
            q = extended_euclid_table["quotients"][i]
            s0 = extended_euclid_table["s"][i-2]
            s = extended_euclid_table["s"][i-1]
            t0 = extended_euclid_table["t"][i-2]
            t = extended_euclid_table["t"][i-1]
            s = q*s + s0
            t = q*t + t0
            extended_euclid_table["s"].append(s)
            extended_euclid_table["t"].append(t)

        return extended_euclid_table


#class Primes:

    def __init__(self, num):
        self.num = num
        self.factors_list = self.factors_list()
        self.euler_phi = self.euler_phi()
        self.binary_expansion = self.binary_expansion()

    def factors_list(self):

        n = self.num
        primes = []
        p = 2
        while p <= n:
            if n % p == 0:
                if primes == []:
                    primes.append([p,1])
                elif primes[-1][0] != p:
                    primes.append([p,1])
                else:
                    primes[-1][1] += 1
                n = n / p
            else:
                p = p + 1

        return primes

    def euler_phi(self):

        prime_factorisation = self.factors_list
        phi = 1
        for [prime, power] in prime_factorisation:
            phi = phi*( prime**power - prime**(power - 1) )

        return phi

    def binary_expansion(self):

        n = self.num
        expansion = []
        length = len(bin(n)) - 2 # binary numbers in Python have a "0b" prefix
        for i in range(2,length + 2):
            expansion.append( int(bin(n)[i]) * (2**(length + 1 - i)) )

        return expansion


#class EulerFermatAlg:

    def __init__(self, base, power, modulo):
        self.base = base
        self.power = power
        self.modulo = modulo
        self.binary_powers = self.binary_powers()

    def binary_powers(self):

        a0 = self.base % self.modulo
        length = len(bin(self.power)) - 2
        powers = [a0]
        for ith_power in range(1,length):
            a0 = (a0**2) % self.modulo
            powers.append(a0)

        return powers


#class DecimalConversion:
    
    # def __init__(self):
        
    def dec_to_base(n,b):
        q = n
        table = [(q,"")]
        while (q!=0):
            q = DivAlg(n,b).quotient
            r = DivAlg(n,b).remainder
            table.append((q,r))
            n = q
        answer = ""
        for row in reversed(table[1:]):
            answer += f"{row[1]}"
        return (table,answer)