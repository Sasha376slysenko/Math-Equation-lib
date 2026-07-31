//
//  Logging.cpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#include "Logging.hpp"


void Logging::logging_of(const int code_error)
{
    std::cout << "[ERROR] " << "CODE EXIT: " << code_error << std::endl;
}

void Logging::logging_operator(const std::string& op)
{
    std::cout << "[ERROR] " << "PROBLEM: op: " << op << std::endl;
}

void Logging::print_result_eval(
    const std::string& name_test,
    const float result_eval_fast,
    const std::string& is_result)
{
    std::cout << "[TEST] " << name_test
    << result_eval_fast << " " << is_result << std::endl;
}

void Logging::print_result_valid(
    const std::string& name_test,
    const bool result_is_valid_eq,
    const std::string& is_result)
{
    if (result_is_valid_eq)
    {
        std::cout << "[TEST] " << name_test
        << "True" << " " << is_result << std::endl;
    }else
    {
        std::cout << "[TEST] " << name_test
        << "False" << " " << is_result << std::endl;
    }
}
