//
//  Unittest.hpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#ifndef Unittest_hpp
#define Unittest_hpp

#include "EquationParser.hpp"
#include "Logging.hpp"
#include <ctime>

class Unittest: public EquationParser {
public:
    void unittest_eval_fast_cpp();
    void unittest_is_valid_equation_cpp();
};

#endif /* Unittest_hpp */
