//
//  EquationParser.cpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#include "EquationParser.hpp"

//===-------------------------------===//
//
// Реалізація методів з точність 1e+15.
// Використовується тип даних <double>.
// Tokenizer вик. тип даних enum{op}.
// Created by Олександр on 07.09.2025.
//
//===-------------------------------===//

bool EquationParser::is_valid_equation_cpp(const std::string_view equation_equals)
{
    std::string left_eq;
    std::string right_eq;
    constexpr double precision = 1e-4;
    bool marker_left_right = true;
    
    //
    // SEPARATION: right_q, left_eq
    //
    for (size_t i = 0; i < equation_equals.length(); i++)
    {
        if (equation_equals[i] == '=')
        {
            marker_left_right = false;
            continue;
        }

        if (marker_left_right)
        {
            left_eq += equation_equals[i];
        }
        else
        {
            right_eq += equation_equals[i];
        }
    }
    
    //
    // left_eq -> eval_fast_cpp -> RECURSION
    // right_eq -> eval_fast_cpp -> RECURSION
    //
    try
    {
        left_eq_d = eval_fast_cpp(left_eq);
        right_eq_d = eval_fast_cpp(right_eq);
    }
    catch (int error)
    {
        logging_of(error);
        return false;
    }

    //
    // RESULT
    //
    // 1. left_eq<double> == right_eq<double>
    // 2. abs precision => |left_eq<double> - right_eq<double>| < 1e-4
    //
    if (left_eq_d == right_eq_d)
    {
        return true;
    }

    if (std::abs(left_eq_d - right_eq_d) < precision)
    {
        return true;
    }
    return false;
}

double EquationParser::eval_fast_cpp(const std::string_view equation)
{
    double res_change = 0.0;
    bool marker_exit = true;
    std::vector<Token> eq_symbols;
    double value_eq_symbols = 0.0;
    const size_t len_equation = equation.length();
    
    //
    // EXIT FUNC CODE EXIT=1
    //
    // 1. exit: digit<string>
    // 2. exit: -digit<string>
    //
    if (equation.length() == 1 || equation.length() == 2)
    {
        try
        {
            return std::stod(std::string(equation));
        }
        catch (int error)
        {
            throw(error);
        }
    }
    
    //
    // EXIT FUNC CODE EXIT=2
    //
    // digit.digit<string>
    //
    for (size_t i = 0; i < len_equation; i++)
    {
        if (equation[i] == '.')
        {
            return std::stod(std::string(equation));
        }
    }
    
    //
    // EXIT FUNC CODE EXIT=3
    //
    // len digit<string>
    //
    for (size_t i = 0; i < len_equation; i++) {
        if (!std::isdigit(equation[i])) {
            marker_exit = false;
            break;
        }
    }
    if (marker_exit) {
        return std::stod(std::string(equation));
    }

    //
    // TOKENIZATION
    //
    // 1. is_digit -> double   -> vector<variant<Token>>
    // 2. '(' -> OP::BRACKET_R -> vector<variant<Token>>
    // 3. ')' -> OP::BRACKET_L -> vector<variant<Token>>
    // 4. '^' -> OP:POW        -> vector<variant<Token>>
    // 5. '*' -> OP:MUL        -> vector<variant<Token>>
    // 6. '/' -> OP::DIV       -> vector<variant<Token>>
    // 7. '+' -> OP::ADD       -> vector<variant<Token>>
    // 8. '-' -> OP::SUB       -> vector<variant<Token>>
    //
    // PRIORITY
    //
    // 1. BRACKET_R = 10.
    // 2. BRACKET_L = 10.
    // 3. POW       = 20.
    // 4. MUL       = 30.
    // 5. DIV       = 30.
    // 6. ADD       = 40.
    // 7. SUB       = 40.
    //
    for (size_t i = 0; i < len_equation; i++)
    {
        if (std::isdigit(equation[i]))
        {
            value_eq_symbols = equation[i] - '0';
            eq_symbols.emplace_back(value_eq_symbols);
            continue;
        }
        
        switch (equation[i])
        {
            case '(':
                eq_symbols.emplace_back(BRACKET_R);
                break;
            case ')':
                eq_symbols.emplace_back(BRACKET_L);
                break;
            case '^':
                eq_symbols.emplace_back(POW);
                break;
            case '*':
                eq_symbols.emplace_back(MUL);
                break;
            case '/':
                eq_symbols.emplace_back(DIV);
                break;
            case '+':
                eq_symbols.emplace_back(ADD);
                break;
            case '-':
                eq_symbols.emplace_back(SUB);
            default:
                break;
        }
    }
    
    //
    // RESULT: vector<variant<Token>> -> compute() -> RECURSION
    //
    // PROBLEM: Logging -> display
    //
    try
    {
        res_change = compute(eq_symbols); // definition func compute()
    }
    catch (int error)
    {
        res_change = std::nan("");
        // if (error == 1)
        // {
        //     print<std::string>("Problem compute");
        // }
        // else
        // {
        //     logging_of(error);
        // }

        if (error != 1)
        {
            logging_of(error);
        }
    }
    return res_change;
}

//
// UPDATE SET INDEX BRACKET
//
void EquationParser::update_set_index_bracket(const size_t& index)
{
    std::unordered_set<size_t> result;
    result.insert(index + 3);
    result.insert(index + 5);
    result.insert(index + 7);
    result.insert(index + 9);
    result.insert(index + 11);
    result.insert(index + 13);
    result.insert(index + 15);
    result.insert(index + 17);
    set_index_bracket = std::move(result);
}

//
// IF
// FIFTH ELEMENT == POW?
//
bool EquationParser::marker_pow_turn_on(
    const std::vector<Token>& tokens,
    const size_t& len_tokens,
    const OP& br,
    const size_t& i)
{
    return len_tokens > 5 && len_tokens - 1
    != find_index<OP>(tokens, br)
    && std::holds_alternative<OP>(tokens[i + 5])
    && std::get<OP>(tokens[i + 5]) == OP::POW;
}

//
// FALSE: (digit op digit) ^ (digit op digit)
// FALSE: ___________pow knife_______________
//
bool EquationParser::br_not_pow_and_not_pow_knife(
        const size_t& len_tokens,
        const bool& marker_pow,
        const bool& marker_pow_knife)
{
    return set_index_bracket.find(len_tokens)
    != set_index_bracket.end() && !marker_pow && !marker_pow_knife;
}

//
// TRUE: (digit op digit) ^ (digit op digit)
// FALSE: ___________pow knife_______________
//
bool EquationParser::br_pow_and_not_pow_knife(
    const size_t& len_tokens,
    const bool& marker_pow,
    const bool& marker_pow_knife)
{
    return set_index_bracket.find(len_tokens)
    != set_index_bracket.end() && marker_pow && !marker_pow_knife;
}

//
// FALSE: (digit op digit) ^ (digit op digit)
// TRUE: ___________pow knife________________
//
bool EquationParser::br_not_pow_and_pow_knife(
    const size_t& len_tokens,
    const bool& marker_pow,
    const bool& marker_pow_knife)
{
    return set_index_bracket.find(len_tokens)
    != set_index_bracket.end() && !marker_pow && marker_pow_knife;
}

//
// SLICE BRACKET
//
// PUSH_BACK: '+'
// PUSH_BACK: result in the bracket
//
bool EquationParser::br_slice_digit_plus(
    const size_t& len_tokens,
    const size_t& index_bracket,
    const ptrdiff_t& sub_index_line,
    const bool& marker_pow)
{
    return len_tokens != index_bracket + 1
    && sub_index_line < 7 && !marker_pow;
}

//
// RECURSION LOWERING IN MATHEMATICAL OPERATORS
//
// 1. digit op digit
// 2. digit op op digit
// 3. digit op digit...
// 4. (digit op digit)
// 5. (digit op digit) op (digit op digit)
// 6. (digit op digit...) op (digit op digit...)
//
// RETURN  -> result<double>
//
// MAX RECURSION: 1000(diving)
//
// PROBLEM MATH FUNCS -> Logging -> display
//

/*
 * +-----------------------------------------+
 * |Find index and priority recursion index: |
 * |1. Len equation symbols.                 |
 * |2. 2. IF => check old priority.          |
 * |3. Struct operator info change.          |
 * +-----------------------------------------+
 */
void EquationParser::findOperator(
    const std::vector<Token>& eq_symbols,
    OperatorInfo& operator_info,
    int priority) const
{
    // 1. Len equation symbols
    const auto len_eq_symbols = eq_symbols.size();

    // 2. IF => check old priority
    if (priority != 0)
    {
        for (size_t i = 0; i < len_eq_symbols; i++)
        {
            if (std::holds_alternative<OP>(eq_symbols[i])
                && std::get<OP>(eq_symbols[i])
                == OP_MATH_OPERATORS[priority - 1])
            {
                priority--;
                break;
            }
        }
    }

    // 3. Struct operator info change
    operator_info.int_math_operator = INT_MATH_OPERATORS[priority];
    operator_info.index_rcn = priority;
}

/*
 * +------------------------------------------+
 * |Extract operands.                         |
 * |1. Init variables.                        |
 * |2. Init INT_MATH_OPERATOR.                |
 * |3. Init markers.                          |
 * |4. Start (one || two) operators negative. |
 * |5. Start number bracket.                  |
 * |6. Save change struct operands info.      |
 * |7. Save change struct compute state.      |
 * +------------------------------------------+
 */
void EquationParser::extractOperands(
    const std::vector<Token>& eq_symbols,
    const OperatorInfo& operator_info,
    OperandsInfo& operands_info,
    ComputeState& compute_state)
{
    // 1. Init variables
    OP op;
    double num_1 = 0.0;
    double num_2 = 0.0;
    size_t i = operands_info.i;
    constexpr int op_SUB = 40;

    // 2. Init int_math_operator and LEN eq
    const auto len_eq_symbols = eq_symbols.size();
    const int int_math_operator = operator_info.int_math_operator;

    // 3. Init markers
    const bool marker = compute_state.marker;
    bool marker_sub = compute_state.marker_sub;
    bool marker_pow = compute_state.marker_pow;
    bool marker_two_sub = compute_state.marker_two_sub;
    bool marker_pow_knife = compute_state.marker_pow_knife;
    bool marker_pow_return_bracket = compute_state.marker_pow_return_bracket;

    if (marker)
    {
        // 4. ===== START (ONE || TWO) OPERATORS NEGATIVE ==========
        op = std::get<OP>(eq_symbols[i]);

        if (int_math_operator == op_SUB &&
            std::holds_alternative<OP>(eq_symbols[i + 1])
            && std::get<OP>(eq_symbols[i + 1]) == SUB)
        {
            i++;
            marker_sub = true;
            marker_two_sub = true;
            num_1 = std::get<double>(eq_symbols[i - 2]);

            if (std::holds_alternative<OP>(eq_symbols[i - 1])
                && std::get<OP>(eq_symbols[i - 1]) == SUB)
            {
                num_1 = num_1 * -1;
            }
        }
        else if (i == 0)
        {
            op = std::get<OP>(eq_symbols[i + 2]);
            num_1 = std::get<double>(eq_symbols[i + 1]);

            if (std::holds_alternative<OP>(eq_symbols[i])
                && std::get<OP>(eq_symbols[i]) == SUB)
            {
                num_1 = num_1 * -1;
            }
        }
        else
        {
            if (len_eq_symbols > 3 && i >= 2)
            {
                if (op != POW &&
                    std::holds_alternative<double>(eq_symbols[i - 1]) &&
                    find_index<double>(eq_symbols, std::get<double>(eq_symbols[i - 1])) != 0
                    && std::holds_alternative<OP>(eq_symbols[i - 2])
                    && std::get<OP>(eq_symbols[i - 2]) == SUB)
                {
                    marker_sub = true;
                    if (std::holds_alternative<OP>(eq_symbols[i - 2])
                        && std::get<OP>(eq_symbols[i - 2]) == SUB)
                    {
                        num_1 = std::get<double>(eq_symbols[i - 1]) * -1;
                    }
                    else
                    {
                        num_1 = std::get<double>(eq_symbols[i - 1]);
                    }
                }
                else
                {
                    num_1 = std::get<double>(eq_symbols[i - 1]);
                }
            }
            else
            {
                num_1 = std::get<double>(eq_symbols[i - 1]);
            }
        }

        if (i == 0) num_2 = std::get<double>(eq_symbols[i + 3]);
        else num_2 = std::get<double>(eq_symbols[i + 1]);
    }
    else
    {
        // 5. ============ START NUMBER BRACKET ==========================
        if (std::holds_alternative<double>(eq_symbols[i + 1]))
        {
            if (find_index<OP>(eq_symbols, BRACKET_L) - i == 2)
            {
                marker_pow_knife = true;

                if (std::holds_alternative<OP>(eq_symbols[i + 4])
                    && std::get<OP>(eq_symbols[i + 4]) == BRACKET_R)
                {
                    i += 4;
                    marker_pow = false;
                    marker_pow_knife = false;
                    marker_pow_return_bracket = false;
                    num_1 = std::get<double>(eq_symbols[i + 1]);
                    op = std::get<OP>(eq_symbols[i + 2]);
                    num_2 = std::get<double>(eq_symbols[i + 3]);
                }
                else
                {
                    num_1 = std::get<double>(eq_symbols[i + 1]);
                    op = POW;
                    num_2 = std::get<double>(eq_symbols[i + 4]);
                }
            }
            else
            {
                if (std::holds_alternative<OP>(eq_symbols[i + 3])
                    && std::get<OP>(eq_symbols[i + 3]) == SUB)
                {
                    marker_sub = true;
                    marker_two_sub = true;
                    num_1 = std::get<double>(eq_symbols[i + 1]);
                    op = std::get<OP>(eq_symbols[i + 2]);

                    if (std::holds_alternative<OP>(eq_symbols[i + 3])
                        && std::get<OP>(eq_symbols[i + 3]) == SUB)
                    {
                        num_2 = std::get<double>(eq_symbols[i + 4]) * -1;
                    }
                    else
                    {
                        num_2 = std::get<double>(eq_symbols[i + 4]);
                    }
                }
                else
                {
                    num_1 = std::get<double>(eq_symbols[i + 1]);
                    op = std::get<OP>(eq_symbols[i + 2]);
                    num_2 = std::get<double>(eq_symbols[i + 3]);
                }

                if (marker_pow_turn_on(eq_symbols, len_eq_symbols, BRACKET_L, i)) // problem
                {
                    marker_pow = true;
                }
            }

            if (std::get<double>(eq_symbols[i + 1]) < 0.0)
                marker_sub = true;
        }
        else {
            marker_sub = true;
            if (find_index<OP>(eq_symbols, BRACKET_L) - i == 3)
            {
                // ReSharper disable once CppDFAUnusedValue
                marker_pow_knife = true;

                if (std::holds_alternative<OP>(eq_symbols[i + 5])
                    && std::get<OP>(eq_symbols[i + 5]) == BRACKET_L)
                {
                    i += 5;
                    marker_pow = false;
                    marker_pow_knife = false;
                    marker_pow_return_bracket = false;
                    num_1 = std::get<double>(eq_symbols[i + 1]);
                    op = std::get<OP>(eq_symbols[i + 2]);
                    num_2 = std::get<double>(eq_symbols[i + 3]);
                }
                else
                {
                    marker_pow_knife = true;
                    if (std::holds_alternative<OP>(eq_symbols[i + 1])
                        && std::get<OP>(eq_symbols[i + 1]) == SUB)
                    {
                        num_1 = std::get<double>(eq_symbols[i + 2]) * -1;
                    }
                    else
                    {
                        num_1 = std::get<double>(eq_symbols[i + 2]);
                    }
                    op = OP::POW;
                    num_2 = std::get<double>(eq_symbols[i + 5]);
                }
            }
            else
            {
                if (std::holds_alternative<OP>(eq_symbols[i + 1])
                    && std::get<OP>(eq_symbols[i + 1]) == SUB)
                {
                    num_1 = std::get<double>(eq_symbols[i + 2]) * -1;
                }
                else
                {
                    num_1 = std::get<double>(eq_symbols[i + 2]);
                }

                op = std::get<OP>(eq_symbols[i + 3]);
                num_2 = std::get<double>(eq_symbols[i + 4]);

                if (i >= 6 && std::holds_alternative<OP>(eq_symbols[i + 6])
                    && std::get<OP>(eq_symbols[i + 6]) == POW)
                {
                    marker_pow = true;
                }
            }
        }
    }

    // 6. Save change struct operands info
    operands_info.i = i;
    operands_info.op = op;
    operands_info.num_1 = num_1;
    operands_info.num_2 = num_2;

    // 7. Save change struct compute state
    compute_state.marker =  marker;
    compute_state.marker_sub = marker_sub;
    compute_state.marker_pow = marker_pow;
    compute_state.marker_two_sub = marker_two_sub;
    compute_state.marker_pow_knife = marker_pow_knife;
    compute_state.marker_pow_return_bracket = marker_pow_return_bracket;
}

/*
 * +----------------------+
 * |Execute operands.     |
 * |1. Init variables.    |
 * |2. Math operation add.|
 * |3. Math operation mul.|
 * |4. Math operation sub.|
 * |5. Math operation div.|
 * |6. Math operation pow.|
 * +----------------------+
 */
void EquationParser::executeOperation(
    OperandsInfo& operands_info,
    const ComputeState& compute_state)
{
    double result = 0.0;
    std::string num_1_str;
    std::string num_2_str;
    const OP op = operands_info.op;
    double num_1 = operands_info.num_1;
    double num_2 = operands_info.num_2;
    const bool marker_two_sub = compute_state.marker_two_sub;

    switch (op)
    {
        case ADD: result = add(num_1, num_2); break;
        case MUL: result = mul(num_1, num_2); break;
        case SUB:
            num_1_str = std::to_string(num_1);
            num_2_str = std::to_string(num_2);

            if (num_2_str[0] == '-')
            {
                if (num_2_str.length() == 2)
                {
                    num_2 = std::stod(std::string(1, num_2_str[1]));
                }
                else
                {
                    num_2 = d_slice_start_index(num_2_str, 1);
                }
                result = add(num_1, num_2);
            }
            else if (num_1_str[0] == '-' && marker_two_sub)
            {
                num_1 = std::stod(std::string(1, num_1_str[1]));
                result = add(num_1, num_2);
            }
            else
            {
                result = sub(num_1, num_2);
            }
            break;
        case DIV:
            try
            {
                result = div(num_1, num_2);
            }
            catch (int error)
            {
                if (error == 1)
                {
                    // ReSharper disable once CppDFAUnusedValue
                    result = std::nan("");
                }
                throw(error);
            }
            break;
        case POW:
            try
            {
                result = power(num_1, num_2);
            }
            catch (int error)
            {
                if (error == 1)
                {
                    // ReSharper disable once CppDFAUnusedValue
                    result = std::nan("");
                }
                throw(error);
            }
            break;
        default:
            break;
    }

    // Save result execute operation
    operands_info.result = result;
}

/*
 * +--------------------+
 * |Replace expression. |
 * |1. Init variables.  |
 * |2. Init markers.    |
 * |3. Slice vector.    |
 * +--------------------+
 */
void EquationParser::replaceExpression(
        std::vector<Token>& eq_symbols,
        const OperandsInfo& operands_info,
        const ComputeState& compute_state)
{
    // 1. Init variables
    const size_t i = operands_info.i;
    const double num_1 = operands_info.num_1;
    const double result = operands_info.result;
    const auto len_eq_symbols = eq_symbols.size();

    // 2. Init markers
    const bool marker = compute_state.marker;
    const bool marker_sub = compute_state.marker_sub;
    const bool marker_pow = compute_state.marker_pow;
    const bool marker_pow_knife = compute_state.marker_pow_knife;
    const bool marker_pow_return_bracket = compute_state.marker_pow_return_bracket;

    if (marker)
    {
        if (marker_sub)
        {
            if (i > 2)
            {
                if (i == 3
                    && !(std::holds_alternative<double>(eq_symbols[i - 3]))
                    && num_1 > 0)
                {
                    slice(
                        eq_symbols,
                        result,
                        i - 2,
                        i + 2,
                        true,
                        true);
                }
                else
                {
                    slice(
                        eq_symbols,
                        result,
                        i - 2,
                        i + 2,
                        false,
                        true);
                }
            }
            else if (i == 2)
            {
                slice(
                    eq_symbols,
                    result,
                    i - 2,
                    i + 2,
                    true,
                    true);
            }
            else if (i == 1)
            {
                slice(
                    eq_symbols,
                    result,
                    i - 1,
                    i + 2,
                    false,
                    true);
            }
            else
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    i + 3,
                    true,
                    true);
            }
        }
        else if (i == 0)
        {
            slice(
                eq_symbols,
                result,
                i,
                i + 4,
                true,
                true);
        }
        else
        {
            slice(
                eq_symbols,
                result,
                i - 1,
                i + 2,
                true,
                true);
        }
        return; // EXIT replaceExpression()
    }
    else
    {
        // Search index_bracket
        ptrdiff_t sub_index = 0;
        size_t index_bracket = 0;

        if (marker_pow_return_bracket)
        {
            index_bracket = find_index<OP>(eq_symbols, OP::BRACKET_L);
        }
        else
        {
            size_t len_slice_eq_symbols;
            std::vector<Token> slice_eq_symbols = slice_start_index(eq_symbols, i);
            len_slice_eq_symbols = slice_eq_symbols.size();

            for (size_t j = 0; j < len_slice_eq_symbols; j++)
            {
                if (std::holds_alternative<OP>(slice_eq_symbols[j])
                    && std::get<OP>(slice_eq_symbols[j]) == OP::BRACKET_L)
                {
                    index_bracket = j + i;
                    break;
                }
            }
        }

        if (marker_sub)
        {
            // Безпечне віднімання ptrdiff_t = <ptrdiff_t>(size_t) - <ptrdiff_t>(size_t)
            sub_index = static_cast<ptrdiff_t>(index_bracket) - static_cast<ptrdiff_t>(i);

            if (sub_index > 5)
            {
                slice(
                    eq_symbols,
                    result,
                    i + 1,
                    i + 5,
                    true, true);
            }
            else if (!marker_pow && !marker_pow_knife)
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    index_bracket + 1,
                    true, true);
            }
            else if (!marker_pow && marker_pow_knife)
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    i + 5,
                    true, true);
            }
            else
            {
                slice(
                    eq_symbols,
                    result,
                    i + 1,
                    index_bracket,
                    true, true);
            }
        }
        else
        {
            ptrdiff_t sub_index_line = 0;
            update_set_index_bracket(index_bracket);
            // Безпечне віднімання ptrdiff_t = <ptrdiff_t>(size_t) - <ptrdiff_t>(size_t)
            sub_index = static_cast<ptrdiff_t>(index_bracket) - static_cast<ptrdiff_t>(i);
            sub_index_line = static_cast<ptrdiff_t>(len_eq_symbols) - static_cast<ptrdiff_t>(index_bracket);

            if (sub_index > 4)
            {
                slice(
                    eq_symbols,
                    result,
                    i + 1,
                    i + 4,
                    true, true);
            }
            else if (br_not_pow_and_not_pow_knife(
                        len_eq_symbols,
                        marker_pow,
                        marker_pow_knife))
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    index_bracket + 1,
                    true, true);
            }
            else if (br_pow_and_not_pow_knife(
                        len_eq_symbols,
                        marker_pow,
                        marker_pow_knife))
            {
                slice(
                    eq_symbols,
                    result,
                    i + 1,
                    index_bracket,
                    true, true);
            }
            else if (br_not_pow_and_pow_knife(
                        len_eq_symbols,
                        marker_pow,
                        marker_pow_knife))
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    index_bracket + 3,
                    true, true);
            }
            else if (br_slice_digit_plus(
                        len_eq_symbols,
                        index_bracket,
                        sub_index_line,
                        marker_pow))
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    index_bracket,
                    false,
                    false);
            }
            else if (!marker_pow)
            {
                slice(
                    eq_symbols,
                    result,
                    i,
                    index_bracket + 1,
                    true,
                    true);
            }
            else
            {
                slice(
                    eq_symbols,
                    result,
                    i + 1,
                    index_bracket,
                    true,
                    true);
            }
        }
        return; // EXIT replaceExpression()
    }
}

/*
 * +--------------------------------+
 * |Global compute:                 |
 * |1. Check recursion exit.        |
 * |2. Init variables: structs.     |
 * |3. Find operator.               |
 * |4. Extract operands.            |
 * |5. Execute operation.           |
 * |6. Replace expression.          |
 * |7. RECURSION -> func compute(). |
 * +--------------------------------+
 */
double EquationParser::compute(
    std::vector<Token>& eq_symbols,
    int count_rcn,
    int counter_max)
{
    // 1. Check recursion exit.
    if (eq_symbols.size() == 1
        && std::holds_alternative<double>(eq_symbols[0]))
    {
        return std::get<double>(eq_symbols[0]);
    }

    if (count_rcn == 7)
    {
        print<std::string>("MAX MATH OPERATION");
        throw(1);
    }

    if (counter_max == 1000)
    {
        print<std::string>("MAX RECURSION");
        throw(1);
    }

    // 2 Init variables: structs
    int int_math_operator;
    ComputeState computeState = {};
    OperatorInfo operatorInfo = {};
    OperandsInfo operandsInfo = {};
    size_t len_eq_symbols = eq_symbols.size();

    // 3. Find operator
    findOperator(eq_symbols, operatorInfo, count_rcn);
    int_math_operator = operatorInfo.int_math_operator;
    count_rcn = operatorInfo.index_rcn;

    // op not bracket
    if (count_rcn >= 1)
        computeState.marker = true;

    for (size_t i = 0; i < len_eq_symbols; i++)
    {
        if (std::holds_alternative<OP>(eq_symbols[i]) &&
            isPriority(std::get<OP>(eq_symbols[i])) == int_math_operator)
        {
            // 4. ======= Extract operands ============
            operandsInfo.i = i;
            extractOperands(
                eq_symbols,
                operatorInfo,
                operandsInfo,
                computeState);

            // 5. ======= Execute operation ============
            executeOperation(operandsInfo, computeState);
            if (std::isnan(operandsInfo.result))
                return operandsInfo.result;

            // 6. ======= Replace expression ============
            replaceExpression(
                eq_symbols,
                operandsInfo,
                computeState);

            if (computeState.marker)
            {
                return compute(
                    eq_symbols,
                    count_rcn,
                    counter_max + 1); // 7. RECURSION -> func compute()
            }
            else
            {
                return compute(
                    eq_symbols,
                    count_rcn + 1,
                    counter_max + 1); // 7. RECURSION -> func compute()
            }
        }
    }
    return compute(
        eq_symbols,
        count_rcn + 1,
        counter_max + 1); // 7. RECURSION -> func compute()
}
