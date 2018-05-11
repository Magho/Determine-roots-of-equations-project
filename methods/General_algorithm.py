import Bisection_method
import Newton_raphson_method
from random import randint
from random import uniform
import math
from sympy import *

class General_Algorithm:

    def exist_with_small_tolerance(self, roots_list, root, tolerance = 0.000000001):
        for r in roots_list:
            if (not isinstance(r[0], str)) and (math.fabs(root - r[0]) < tolerance):
                return true
        return false

    def findAllRoots(self, function_formula):
        newton_roots = [["Xr"]]
        bisec_roots = [["Xr"]]
        self.function_formula_biSec = function_formula
        self.function_formula = function_formula
        num_of_bisec_roots = 0

        for i in range(-1000, 1000, 1):
            single_root = []
            minusRandom = uniform(0, 1)
            plusRandom = uniform(0, 1)
            function_value_at_lower_bound = self.function_formula_biSec.subs(Symbol('x'), i-minusRandom)
            function_value_at_upper_bound = self.function_formula_biSec.subs(Symbol('x'), i+plusRandom)
            indicator = function_value_at_lower_bound * function_value_at_upper_bound
            if indicator < 0:
                biSec = Bisection_method.BracketingMethod(self.function_formula_biSec, i-minusRandom, i+plusRandom, 50, 0.000000000001)
                biSec.determine_number_of_iterations()
                root = biSec.compute_root()[1]
                eval = self.function_formula_biSec.subs(Symbol('x'), root)
                if (eval is zoo or math.isnan(eval) or (eval < 1e-8 and eval > -1e-8)):
                    if (root < 1e-10 and root > -1e-10):
                        single_root.append(0.0)
                    else:
                        single_root.append(root)
                    num_of_bisec_roots += 1
                    bisec_roots.append(single_root)
            elif indicator == 0:
                if function_value_at_lower_bound == 0:
                    if (i-minusRandom < 1e-10 and i-minusRandom > -1e-10):
                        single_root.append(0.0)
                    else:
                        single_root.append(i-minusRandom)
                    num_of_bisec_roots += 1
                    bisec_roots.append(single_root)
                elif function_value_at_upper_bound == 0:
                    if (i+plusRandom < 1e-10 and i+plusRandom > -1e-10):
                        single_root.append(0.0)
                    else:
                        single_root.append(i+plusRandom)
                    num_of_bisec_roots += 1
                    bisec_roots.append(single_root)


        num_of_newton_roots = 0
        newton_num_of_non_ordinary_roots = 0
        for i in range(100):
            single_nroot = []
            if (isinstance(self.function_formula, int)
            or isinstance(self.function_formula, float)
            or isinstance(self.function_formula, numbers.One)):
                return
            randomInitialPoint = randint(-100000, 100000)
            newtonR = Newton_raphson_method.NewtonRaphson(self.function_formula, randomInitialPoint, 75, 0.000000000001);
            root = newtonR.compute_root()[1]
            if root is "db0":
                continue
            elif root is "r0" or root is '0' or root is '0.0':
                self.function_formula = (self.function_formula / (x))
                num_of_newton_roots += 1
                single_nroot.append(0.0)
                newton_roots.append(single_nroot)
            elif root is "err":
                continue
            elif (isinstance(root, int) or isinstance(root, float)) and (not math.isnan(root)):
                if root < -1e+8 or root > 1e+8:
                    newton_num_of_non_ordinary_roots += 1
                eval = self.function_formula.subs(Symbol('x'), root)
                if (root < 1e-10 and root > -1e-10):
                    if (eval is zoo or math.isnan(eval) or (eval < 1e-8 and eval > -1e-8)):
                        self.function_formula = (self.function_formula / x)
                        num_of_newton_roots += 1
                        single_nroot.append(0.0)
                        newton_roots.append(single_nroot)
                else:
                    if (eval is zoo or math.isnan(eval) or (eval < 1e-8 and eval > -1e-8)):
                        self.function_formula = (self.function_formula / (x - root))
                        num_of_newton_roots += 1
                        single_nroot.append(root)
                        newton_roots.append(single_nroot)
            else:
                break

            if newton_num_of_non_ordinary_roots > 9:
                break

        if len(newton_roots) > len(bisec_roots) + 9:
            for r in newton_roots:
                if (not isinstance(r[0], str)) and (not (r[0] < -1e+8 or r[0] > 1e+8)):
                    if not (self.exist_with_small_tolerance(bisec_roots, r[0], 0.00001)):
                        rootToAppend= []
                        rootToAppend.append(r[0])
                        bisec_roots.append(rootToAppend)
            return bisec_roots
        else:
            for r in bisec_roots:
                if (not isinstance(r[0], str)) and  (not (self.exist_with_small_tolerance(newton_roots, r[0], 0.00001))):
                    rootToAppend= []
                    rootToAppend.append(r[0])
                    newton_roots.append(rootToAppend)
            return newton_roots




# ------------------------------------------------ test 1 -------------------------------------------------
x = Symbol('x')
function_formula = (x-1)*(x-5) * (x-3)**3 * x
ga = General_Algorithm()
print(ga.findAllRoots(function_formula))
