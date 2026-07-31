//
//  Token.cpp
//  EquationAST
//
//  Created by Олександр on 08.09.2025.
//

#include "Token.hpp"

int Priority::isPriority(const OP& op)
{
    switch (op) {
        case BRACKET_R: return 10;
        case BRACKET_L: return 10;
        case POW:       return 20;
        case MUL:       return 30;
        case DIV:       return 30;
        case ADD:       return 40;
        case SUB:       return 40;
        default:        return 50;
    }
}
