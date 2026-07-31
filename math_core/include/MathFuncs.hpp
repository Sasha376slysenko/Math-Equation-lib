//
//  MathFuncs.hpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#ifndef MathFuncs_hpp
#define MathFuncs_hpp

#include <cmath>

class MathFuncs {
public:
    static double power(double base, double exp);
    static double mul(double digit_1, double digit_2);
    static double div(double digit_1, double digit_2);
    static double add(double digit_1, double digit_2);
    static double sub(double digit_1, double digit_2);
};

#endif /* MathFuncs_hpp */
