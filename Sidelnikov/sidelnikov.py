from sage.all import *


class Sidelnikov:
    def __init__(self, q):
        self.q = q

        self.galoisFieldq = GF(self.q, 'a')

        if not is_prime_power(self.q):
            raise TypeError(f"{self.q} must be a prime or a prime power.")

    def __call__(self, t):
        primitive_elm = self.galoisFieldq.primitive_element()

        if not (primitive_elm ** t + 1).is_square():
            return 1
        else:
            return 0

    def getSequence(self):
        sidelSeq = []
        for t in range(len(self.galoisFieldq))[1:]:
            sidelSeq.append(self(t))
        return sidelSeq
