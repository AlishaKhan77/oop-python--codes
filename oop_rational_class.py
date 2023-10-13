class Rational():
    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d
    def show(self):
        print(f'{self.numerator}/{self.denominator}')
    def multiply(self,rat2):
        mul_num = self.numerator*rat2.numerator
        mul_den = self.denominator*rat2.denominator
        result = Rational(mul_num, mul_den)
        return result
    def real(self):
        if self.denominator!=0:
            print('Number is Real')
        else:
            print('Number is Imaginary(not Real)')
def main():
    print('First Rational Number:',end='\t')
    r1 = Rational(2,4)
    r1.show()
    print('Second Rational Number:',end='\t')
    r2 = Rational(3,2)
    r2.show()
    print('Product of both rational numbers:',end='\t')
    product = r1.multiply(r2)
    product.show()
    r1.real()
    r2.real()
    product.real()
main()
