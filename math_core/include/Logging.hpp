//
//  Logging.hpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#ifndef Logging_hpp
#define Logging_hpp

#include <iostream>

class Logging {
public:
    template <typename T>
    static void print(const T& value) {
        std::cout << value << std::endl;
    }

    static void logging_of(int code_error);
    static void logging_operator(const std::string& op);

    static void print_result_eval(
        const std::string& name_test,
        float result_eval_fast,
        const std::string& is_result);

    static void print_result_valid(
        const std::string& name_test,
        bool result_is_valid_eq,
        const std::string& is_result);
};

#endif /* Logging_hpp */
