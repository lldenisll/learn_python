import math
class Bhaskara:
    def main(self):

        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        c = float(input("Valor de c: "))

        print(self.imprime_raizes(a, b, c))

    def delta(self,a, b, c):
        return b ** 2 - 4 * a * c


    def imprime_raizes(self,a, b, c):
        d = self.delta(a, b, c)

        if d < 0:
            return 0
        else:
            raizdelta = math.sqrt(d)
            x1 = (-b + (raizdelta)) / (2 * a)
            x2 = (-b - (raizdelta)) / (2 * a)
            x3 = (-b) / (2 * a)
            if d > 0:
                return 2, x1, x2
            if d == 0:
                return 1, x3


