//
//  MathFuncs.cpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#include "MathFuncs.hpp"

double MathFuncs::power(const double base, const double exp)
{
    const int exp_int = static_cast<int>(std::round(exp));

    if (exp == 0.0) return 1.0;
    if (exp == 1.0) return base;
    if (base == 1.0) return 1.0;

    if (base == -1.0)
    {
        if (exp_int != 0 && exp_int % 2 == 0) return 1.0;
        else return -1.0;
    }
    
    if (base < 0.0) throw(1);
    if (base == 0.0 && exp < 0.0) throw(1);
    if (exp < -34.0 || exp > 80.0) throw(1);

    return std::pow(base, exp);
}

double MathFuncs::mul(const double digit_1, const double digit_2)
{
    return digit_1 * digit_2;
}

double MathFuncs::div(const double digit_1, const double digit_2)
{
    if (digit_2 == 0.0f) throw(1);
    else return digit_1 / digit_2;
}

double MathFuncs::add(const double digit_1, const double digit_2)
{
    return digit_1 + digit_2;
}

double MathFuncs::sub(const double digit_1, const double digit_2)
{
    return digit_1 - digit_2;
}
