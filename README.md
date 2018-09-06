# Determine-roots-of-equations-project
  This is the semester project for the course of ‘Numerical Analysis and Computer
  Applications’ - CS213 for the 2
  nd year of Computer and Systems Engineering Department
  to be delivered to Dr. Wafaa ElHaweet and the teaching assistant Eng. Omar
  Salaheldine.
  Our project is developed in Python programming language. We used appJar library to
  create the interactive GUI.
  
- #### Specifications:
  The pupose of the app is to find roots of any Equation based on some methods: 
    - Bracketing Methods.
    - Open Methods.
    - Bierge Vieta
    - General Algorithm.
    
- #### Bracketing Methods:
   the bracketing methods aim to iteratively shorten the interval in order to find the root within a certain level of significance (epsilon).
   
   - ###### Bisection Method
      The bracketing mechanism is done by finding the function’s value in the middle of the bracketed interval. Then moving to a subproblem of the same type in either the left-halved interval or right-halved interval by checking the bracketing condition’s validation for each.

<img src="https://github.com/Magho/Root-finder/blob/master/images/1.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/2.png" width="400"> 
      
   - ###### False Position (Regula Falsi) Method
      The bracketing mechanism is by connecting a line between the two function’s values at
      the terminals of the interval. The root estimate is the intersection of that line with the
      abscissa. To get a better estimate, we evaluate the function’s value at the x-coordinate
      intersection found at that iteration, and run the same bracketing test with the terminals
      and use the valid interval to the find a better estimate in the next iteration.
      Regula Falsi, like Bisection, always converges, usually considerably faster than
      Bisection—but sometimes much slower than Bisection.
      
<img src="https://github.com/Magho/Root-finder/blob/master/images/3.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/4.png" width="400"> 


- #### Open Methods
  The open points try to find the root in a way that doesn’t require as much initial
  knowledge as the bracketing methods which rely on having a certain interval where a
  root is guaranteed to exist within.
  The open methods for root finding rely mostly on trying to adapt with the function’s
  behaviour, mostly through its first derivative or its estimate, to guide it to the roots of the
  equation.
  
    - ###### Fixed-Point Method
      This method relies on finding the intersection between two functions; y = x and y = g(x).
      This is why it iterates through this formula of equating them to get g(x) = x and iteratively
      closer to the solution.
      We get the function g(x) by separating an x from the function in question f(x). The
      intersection x-coordinate shall be found to be the x-coordinate of the root.

<img src="https://github.com/Magho/Root-finder/blob/master/images/5.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/6.png" width="400"> 
            
   - ###### Newton-Raphson Method
      The idea of the method is as follows: one starts with an initial guess which is reasonably
      close to the true root, then the function is approximated by its tangent line (which can be
      computed using the tools of calculus), and one computes the x-intercept of this tangent
      line (which is easily done with elementary algebra). This x-intercept will typically be a
      better approximation to the function's root than the original guess, and the method can
      be iterated.
      
<img src="https://github.com/Magho/Root-finder/blob/master/images/7.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/8.png" width="400"> 
            
   - ###### Secant Method
      The secant method is in theory, the same as the Newton-Raphson method explained
      earlier. However, instead of finding the first derivative through calculus, we use a simple
      delta y / delta x using the points of previous two iterations. Which introduces the
      disadvantage of the Secant method which is the fact that it needs two points initially not
      one, unlike most of the open methods.
      
<img src="https://github.com/Magho/Root-finder/blob/master/images/9.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/10.png" width="400"> 

  - #### Bierge Vieta Method
    explanation can be found in the Report 
    
<img src="https://github.com/Magho/Root-finder/blob/master/images/11.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/12.png" width="400"> 
                
- #### General Algorithm
  This mode runs by being given a function to compute as much as possible of its roots, it’s
  a combine of two methods introduced in this report in such a way to come over the
  disadvantage of each method.
  Newton and bisection methods are used (An iterative method along with a bracketing
  one)
  
<img src="https://github.com/Magho/Root-finder/blob/master/images/13.png" width="400"> <img src="https://github.com/Magho/Root-finder/blob/master/images/14.png" width="400"> 
                
### a detaield Explanation can be found here [Report](https://github.com/Magho/Root-finder/blob/master/NumericalProjectReport.pdf)

## Running

#### Clone & install
* 
* Clone this repo `https://github.com/Magho/Root-finder`
* cd `Root-finder/appJar`
* run `appjar.py` file

## Authors
  - [Magho](https://github.com/Magho)
  - [Mahmoud Tarek](https://github.com/MahmoudTarek97)
  - [Abdelrahman Ahmed](https://github.com/abdelrahman882)
  - [BassamMattar](https://github.com/BassamMattar)
  - [SajedHassan](https://github.com/SajedHassan)

## License 
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
[LICENSE.md](https://github.com/Magho/Root-finder/blob/master/LICENSE)

