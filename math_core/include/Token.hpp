//
//  Token.hpp
//  EquationAST
//
//  Created by Олександр on 07.09.2025.
//

#ifndef Token_hpp
#define Token_hpp

#include <variant>

//===--------------------------------===//
//
// ENUM -> 'TOKENS MATH OPERATOR'.
// token stream - mathematical operators.
// Created by Олександр on 07.09.2025
//
//===--------------------------------===//

enum OP {
    BRACKET_R,
    BRACKET_L,
    POW,
    MUL,
    DIV,
    ADD,
    SUB
};

//===-----------------------------===//
//
// TOKEN -> TOKENIZATION -> COMPUTE.
// Created by Олександр on 05.09.2025
//
//===-----------------------------===//

using Token = std::variant<OP, double>;

//===---------------------------===//
//
// PRIORITY:
// 1. BRACKET_R = 10.
// 2. BRACKET_L = 10.
// 3. POW       = 20.
// 4. MUL       = 30.
// 5. DIV       = 30.
// 6. ADD       = 40.
// 7. SUB       = 40.
// Created by Олександр on 08.09.2025
//
//===---------------------------===//

class Priority {
public:
    static int isPriority (const OP& op);
};

#endif
