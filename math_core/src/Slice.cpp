//
//  Slice.cpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#include "Slice.hpp"

/*
 * +---------------------------------+
 * |Slice start index and end index: |
 * |1. Create vector => Token.       |
 * |2. Itr -> old symbol start.      |
 * |3. Add new symbol.               |
 * |4. Itr -> old symbol end.        |
 * +---------------------------------+
 */
void Slice::slice(
    std::vector<Token>& tokens,
    const double& inp_double,
    const size_t start_index,
    const size_t end_index,
    const bool marker_1,
    const bool marker_2)
{
    std::vector<Token> result;
    
    //
    // old symbol - start
    //
    for (size_t i = 0; i < start_index; i++)
    {
        result.push_back(tokens[i]);
    }
    
    //
    // new symbol
    //
    // vector<Token>.push_back(input)
    //
    if (marker_1 && marker_2)
    {
        result.emplace_back(inp_double);
    }
    else if (!marker_1 && marker_2)
    {
        result.emplace_back(ADD);
        result.emplace_back(inp_double);
    }
    else
    {
        result.emplace_back(inp_double);
        result.emplace_back(ADD);
    }
    
    //
    // old symbol - end
    //
    // vector<Token>.push_back(end)
    //
    for (size_t j = end_index; j < tokens.size(); j++)
    {
        result.push_back(tokens[j]);
    }
    
    //
    // UPDATE GLOBAL VECTOR<TOKEN>
    //
    tokens = std::move(result);
}

/*
 * +---------------------------+
 * |Slice start index token:   |
 * |1. Create vector => Token. |
 * |2. Itr -> token.           |
 * +---------------------------+
 */
std::vector<Token> Slice::slice_start_index(
    const std::vector<Token>& tokens,
    const size_t& index_start)
{
    std::vector<Token> result;
    
    for (size_t i = index_start; i < tokens.size(); i++)
    {
        result.push_back(tokens[i]);
    }
    return result;
}

/*
 * +------------------------------+
 * |Slice start index strying:    |
 * |1. Create variable result_str.|
 * |2. Itr -> symbol.             |
 * +------------------------------+
 */
double Slice::d_slice_start_index(
    const std::string& row,
    const size_t index)
{
    std::string result_str;
    
    for (size_t i = index; i < row.length(); i++)
    {
        result_str += row[i];
    }
    return std::stod(result_str);
}
