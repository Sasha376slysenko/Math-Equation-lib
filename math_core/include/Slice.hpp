//
//  Slice.hpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#ifndef Slice_hpp
#define Slice_hpp

#include <vector>
#include <string>
#include <iostream>
#include "Token.hpp"

class Slice {
private:
    size_t index_not_fund = 0;
public:
    // Slice 1
    void slice(
        std::vector<Token>& tokens,
        const double& inp_double,
        size_t start_index,
        size_t end_index,
        bool marker_1,
        bool marker_2);

    // Slice 2
    static double d_slice_start_index(
        const std::string& row,
        size_t index);

    // Slice 3
    std::vector<Token> slice_start_index(
        const std::vector<Token>& tokens,
        const size_t& index_start);

    // Find index. TEMPLATE
    template <typename op_el>
    size_t find_index(
        const std::vector<Token>& tokens,
        const op_el& element)
    {
        for (size_t i = 0; i < tokens.size(); i++)
        {
            if (std::holds_alternative<op_el>(tokens[i])
                && std::get<op_el>(tokens[i]) == element)
            {
                return i;
            }
        }
        return index_not_fund;
    }
};

#endif /* Slice_hpp */
