//
//  EquationParser.hpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#ifndef EquationParser_hpp
#define EquationParser_hpp

#include <vector>
#include <unordered_set>

#include "Logging.hpp"
#include "MathFuncs.hpp"
#include "Slice.hpp"

// Find operator
struct OperatorInfo
{
    int int_math_operator;
    int index_rcn;
};

// Extract operands
struct OperandsInfo
{
    size_t i = 0;
    OP op = ADD;
    double num_1 = 0.0;
    double num_2 = 0.0;
    double result = 0.0;
};

// Global ompute state
struct ComputeState
{
    bool marker = false;
    bool marker_sub = false;
    bool marker_pow = false;
    bool marker_two_sub = false;
    bool marker_pow_knife = false;
    bool marker_pow_return_bracket = false;
};

// Equation parser
class EquationParser: public Logging, public MathFuncs, public Slice, public Priority {
public:
    bool is_valid_equation_cpp(std::string_view equation_equals);
    double eval_fast_cpp(std::string_view equation);
private:
    double left_eq_d = 0.0;
    double right_eq_d = 0.0;
    const int INT_MATH_OPERATORS[4] = { 10, 20, 30, 40 };
    const OP OP_MATH_OPERATORS[7] = { BRACKET_R, BRACKET_L, POW, MUL, DIV, ADD, SUB };

    std::vector<Token> slice_eq_symbols;
    std::unordered_set<size_t> set_index_bracket;

    bool f_is_digit(const char& el);
    void update_set_index_bracket(const size_t& index);

    // 1. IF
    bool marker_pow_turn_on(
        const std::vector<Token>& tokens,
        const size_t& len_tokens,
        const OP& br,
        const size_t& i);

    // 2. IF
    bool br_not_pow_and_not_pow_knife(
        const size_t& len_tokens,
        const bool& marker_pow,
        const bool& marker_pow_knife);

    // 3. IF
    bool br_pow_and_not_pow_knife(
        const size_t& len_tokens,
        const bool& marker_pow,
        const bool& marker_pow_knife);

    // 4. IF
    bool br_not_pow_and_pow_knife(
        const size_t& len_tokens,
        const bool& marker_pow,
        const bool& marker_pow_knife);

    // 5. IF
    static bool br_slice_digit_plus(
        const size_t& len_tokens,
        const size_t& index_bracket,
        const ptrdiff_t& sub_index_line,
        const bool& marker_pow);

    // 1. COMPUTE
    void findOperator(
        const std::vector<Token>& eq_symbols,
        OperatorInfo& operator_info,
        int priority) const;

    // 2. COMPUTE
    void extractOperands(
        const std::vector<Token>& eq_symbols,
        const OperatorInfo& operator_info,
        OperandsInfo& operands_info,
        ComputeState& compute_state);

    // 3. COMPUTE
    static void executeOperation(
        OperandsInfo& operands_info,
        const ComputeState& compute_state);

    // 4. COMPUTE
    void replaceExpression(
        std::vector<Token>& eq_symbols,
        const OperandsInfo& operands_info,
        const ComputeState& compute_state);

    double compute(
        std::vector<Token>& eq_symbols,
        int count_rcn = 0,
        int counter_max = 0);
};

#endif /* EquationParser_hpp */
