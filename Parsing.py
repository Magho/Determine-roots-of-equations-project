from math import *
from sympy import *

class Parser:
    """
supported operations :
our syntax     meaning
+ - * /          __
fabs(x)         |x|
factorial(x)     x!
exp(x)        e power x
x**3          x power 3
log(x,y)     log x base y
log(x)       log x base e  ( ln x )
pow(x,y)     x power y
acos            cos-1(rad)
asin            ..
atan            ..
cos             ..
sin             ..
tan             ..
pi              pi constant
e               natural number
    """
    func = ""

    def set_func(self, my_function):
        """
        this function must be called before f if not , f would return nothing
        :param my_function: the string representing the mathematical exepression
        :return: true if the functions contains no injection attack
        """
        self.func = my_function
        return self.check_func()

    def check_func(self):
        """
        :return: true if the function is parsed correctly , false  otherwise
        """
        i = 0
        while True:
            if i >= len(self.func):
                break
            c = self.func[i]
            if c != ',' \
                    and c != 'x' \
                    and c != ' ' \
                    and c != '+' \
                    and c != '-' \
                    and c != ')' \
                    and c != '.' \
                    and c != '(' \
                    and c != '*' \
                    and c != '/' \
                    and not self.is_number(c):
                if str.find(self.func, "pi", i, i+2) != -1:
                    i += 2
                    continue
                elif str.find(self.func, "pow", i, i+3) != -1:
                    i += 3
                    continue
                elif str.find(self.func, "log", i, i+3) != -1:
                    i += 3
                    continue
                elif str.find(self.func, "sin", i, i+3) != -1:
                    i += 3
                    continue
                elif str.find(self.func, "cos", i, i+3) != -1:
                    i += 3
                    continue
                elif str.find(self.func, "tan", i, i+3) != -1:
                    i += 3
                    continue
                elif str.find(self.func, "exp", i, i+3) != -1:
                    i += 3
                    continue
                elif c == 'e':
                    i += 1
                    continue
                elif str.find(self.func, "fabs", i, i+4) != -1:
                    i += 4
                    continue
                elif str.find(self.func, "acos", i, i+4) != -1:
                    i += 4
                    continue
                elif str.find(self.func, "asin", i, i+4) != -1:
                    i += 4
                    continue
                elif str.find(self.func, "atan", i, i+4) != -1:
                    i += 4
                    continue
                elif str.find(self.func, "factorial", i, i + 9) != -1:
                    i += 9
                    continue
                else:
                    print(c)
                    return False
            i += 1
        return True

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def f(self):
        """
        XXXX this function throws an exception if there is something wrong with the function (syntax error , /0 , ..)
        it returns the f(x) where the function mus be set before using set_func
        :return: f(x)
        """
        x = Symbol('x')
        object_code = compile(self.func, '', 'eval')
        res = eval(object_code)

        return res

    def poly_coeffs(self):
        """

        :return:
        """
        x = Symbol('x')
        object_code = compile(self.func, '', 'eval')
        res = eval(object_code)
        return Poly(res).all_coeffs()

    def g(self):
        """
        assumes that the function f(x) is on the format
                f(x) =   a * g(x) (- or +) a*x
        """

        g = self.func
        count = len(g)-1
        number_of_xs =0
        while g[count] != '-' and g[count] != '+':
            if count < 0 or number_of_xs > 1:
                return False
            if g[count] == 'x':
                if count+1<len(g):
                  g = g[:count]+'1'+g[count+1:]
                else :
                  g = g[:count]+'1'
                number_of_xs += 1
            count -= 1
        sign = g[count]
        g = '('+g[:count]+')/('+g[count+1:]+')'
        if sign == '+':
            g = '-1*'+g
        x = Symbol('x')
        object_code = compile(g, '', 'eval')
        res = eval(object_code)
        return res

#### examples on Parser class


p = Parser()

p.set_func("4+sin(5*x)-exp(4/x)+30*x")
s=p.g()
print(s)

p.set_func("7+x**5+x-70*x**2")
print(p.poly_coeffs())

print(p.f())
"""
#0
if p.set_func("x**3 + 2 * x**2  - 4 * x + 3"):
    print(p.f(3))
else:
    print("error")
#1
if p.set_func("pow(2,.5)- 2* sin(45 * pi /180)+ e **2 /(e**2) + x"):
    print(p.f(3))
else:
    print("error")

#2
if p.set_func("acos(.707)*180/pi"):
    print(p.f(3))
else:
    print("error")

#3
if p.set_func("2 * sin(x) - 3 * cos(x) + 9 * tan (x) - log(e,x)"):
    print(p.f(3))
else:
    print("error")

#4
if p.set_func("exp(3)/(e**3)"):
    print(p.f(3))
else:
    print("error")

#5
if p.set_func("fabs(-11+x)- x + x *2"):
    print(p.f(3))
else:
    print("error")

#6
if p.set_func("factorial(x)"):
    print(p.f(3))
else:
    print("error")

#7
try:
    if p.set_func("factorial(x)/0"):
        print(p.f(3))
    else:
        print("error from injection check")
except Exception as e:
    print("error from the syntax : " + str(e))

#8
try:
    if p.set_func("factorial(x) + factorial(sincos"):
        print(p.f(3))
    else:
        print("error from injection check")
except Exception as e:
    print("error from the syntax : " + str(e))

"""