//
//  Unittest.cpp
//  EquationAST
//
//  Created by Олександр on 03.09.2025.
//

#include "Unittest.hpp"


void Unittest::unittest_eval_fast_cpp() {
    print<std::string>("\neval_fast:");
    const clock_t start = clock();
    
    // unittest one
    print<std::string>("#=====================1==================================#");
    print_result_eval("unitest_1.1 ", eval_fast_cpp("15"), "is 15");
    print_result_eval("unitest_1.2 ", eval_fast_cpp("2+3"), "is 5");
    print_result_eval("unitest_1.3 ", eval_fast_cpp("2*3"), "is 6");
    print_result_eval("unitest_1.4 ", eval_fast_cpp("3/3"), "is 1");
    print_result_eval("unitest_1.5 ", eval_fast_cpp("2^3"), "is 8");
    print_result_eval("unitest_1.6 ", eval_fast_cpp("2-3"), "is -1");
    print_result_eval("unitest_1.7 ", eval_fast_cpp("2--3"), "is 5");
    print_result_eval("unitest_1.8 ", eval_fast_cpp("2/3"), "is 0.66");
    print_result_eval("unitest_1.9 ", eval_fast_cpp("1+2+3+4+5+6+7+8+9"), "is 45");

    // unittest two
    print<std::string>("");
    print<std::string>("#=====================2==================================#");
    print_result_eval("unitest_2.1 ", eval_fast_cpp("1-(3-4)"), "is 2");
    print_result_eval("unitest_2.2 ", eval_fast_cpp("-7+8"), "is 1");
    print_result_eval("unitest_2.3 ", eval_fast_cpp("-3+3+7"), "is 7");
    print_result_eval("unitest_2.4 ", eval_fast_cpp("-1-7+8"), "is 0");
    print_result_eval("unitest_2.5 ", eval_fast_cpp("(3+4)*1"), "is 7");
    print_result_eval("unitest_2.6 ", eval_fast_cpp("(3*4)/2"), "is 6");
    print_result_eval("unitest_2.7 ", eval_fast_cpp("(3*4)*2"), "is 24");

    // unittest three
    print<std::string>("");
    print<std::string>("#=====================3==================================#");
    print_result_eval("unitest_3.1 ", eval_fast_cpp("-1+5"), "is 4");
    print_result_eval("unitest_3.2 ", eval_fast_cpp("(1+2)"), "is 3");
    print_result_eval("unitest_3.3 ", eval_fast_cpp("(1+8-9-1+2)+5"), "is 6");
    print_result_eval("unitest_3.4 ", eval_fast_cpp("(5*9-6+3)*6"), "is 252");

    // unitest four
    print<std::string>("");
    print<std::string>("#=====================4==================================#");
    print_result_eval("unitest_4.1 ", eval_fast_cpp("-1-5"), "is -6");
    print_result_eval("unitest_4.2 ", eval_fast_cpp("(1+2)"), "is 3");
    print_result_eval("unitest_4.3 ", eval_fast_cpp("-1-5"), "is -6");
    print_result_eval("unitest_4.4 ", eval_fast_cpp("2/3*6"), "is 4");
    print_result_eval("unitest_4.5 ", eval_fast_cpp("-3*5"), "is -15");
    print_result_eval("unitest_4.6 ", eval_fast_cpp("-7-8"), "is -15");
    print_result_eval("unitest_4.7 ", eval_fast_cpp("1--1+5"), "is 7");
    print_result_eval("unitest_4.8 ", eval_fast_cpp("(-1+2)+5"), "is 6");
    print_result_eval("unitest_4.9 ", eval_fast_cpp("1+(3-4)+3"), "is 3");
    print_result_eval("unitest_4.10 ", eval_fast_cpp("8-1^(3/4/2)"), "is 7");
    print_result_eval("unitest_4.11 ", eval_fast_cpp("8-1^(3^4^2)"), "is 7");
    print_result_eval("unitest_4.12 ", eval_fast_cpp("5+3-(9-8)^6"), "is 7");
    print_result_eval("unitest_4.13 ", eval_fast_cpp("5+3-(8-9)^3"), "is 9");
    print_result_eval("unitest_4.14 ", eval_fast_cpp("(9-6)^(9-6)"), "is 27");
    print_result_eval("unitest_4.15 ", eval_fast_cpp("(8-9)^(9-6)"), "is -1");
    print_result_eval("unitest_4.16 ", eval_fast_cpp("(8-9)^(9-5)"), "is 1");
    print_result_eval("unitest_4.17 ", eval_fast_cpp("(9-8)^(6-9)"), "is 1");
    print_result_eval("unitest_4.18 ", eval_fast_cpp("1-(2-3)+3+5"), "is 10");
    print_result_eval("unitest_4.19 ", eval_fast_cpp("6+(1+5)+2+4-9"), "is 9");
    
    const clock_t end = clock();
    print<std::string>("");
    const double time_check = static_cast<double>(end - start) / CLOCKS_PER_SEC;
    print<std::string>("#~~~~~~~~~~~~~~~~~~~~~~~ TIME UNIT(SEC): ~~~~~~~~~~~~~~~~~~~~~~~~~~~#");
    print<double>(time_check);
    print<std::string>("#~~~~~~~~~~~~~~~~~~~~~~~~~ TIME END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#");
}

void Unittest::unittest_is_valid_equation_cpp() {
    print<std::string>("\nis_valid_equation:");
    const clock_t start = clock();
    
    // unittest one
    print<std::string>("#=======================1==============================#");
    print_result_valid("unitest_1.1 ", is_valid_equation_cpp("1+2=+3"), "is true");
    print_result_valid("unitest_1.2 ", is_valid_equation_cpp("1+2=3+"), "is true");
    print_result_valid("unitest_1.3 ", is_valid_equation_cpp("2+3=5"), "is true");
    print_result_valid("unitest_1.4 ", is_valid_equation_cpp("2*3=6"), "is true");
    print_result_valid("unitest_1.5 ", is_valid_equation_cpp("3/3=1"), "is true");
    print_result_valid("unitest_1.6 ", is_valid_equation_cpp("2^3=8"), "is true");
    print_result_valid("unitest_1.7 ", is_valid_equation_cpp("2-3=-1"), "is true");
    print_result_valid("unitest_1.8 ", is_valid_equation_cpp("2--3=5"), "is true");
    print_result_valid("unitest_1.9 ", is_valid_equation_cpp("9*8=9*8"), "is true");
    print_result_valid("unitest_1.10 ", is_valid_equation_cpp("1+2+3+4+5+6+7+8+9=45"), "is true");

    // unittest two
    print<std::string>("");
    print<std::string>("#=======================2================================#");
    print_result_valid("unitest_2.1 ", is_valid_equation_cpp("2=1-(3-4)"), "is true");
    print_result_valid("unitest_2.2 ", is_valid_equation_cpp("6=(8-1)-1"), "is true");
    print_result_valid("unitest_2.3 ", is_valid_equation_cpp("8=8+(6*0)"), "is true");
    print_result_valid("unitest_2.4 ", is_valid_equation_cpp("(2+5)=9-2"), "is true");
    print_result_valid("unitest_2.5 ", is_valid_equation_cpp("5=(7*5)/7"), "is true");
    print_result_valid("unitest_2.6 ", is_valid_equation_cpp("(3+9)=(5+7)"), "is true");
    print_result_valid("unitest_2.7 ", is_valid_equation_cpp("(7*4)/4=7"), "is true");
    print_result_valid("unitest_2.8 ", is_valid_equation_cpp("(5/8)=5/8"), "is true");
    print_result_valid("unitest_2.9 ", is_valid_equation_cpp("7=(9-6)+4"), "is true");
    print_result_valid("unitest_2.10 ", is_valid_equation_cpp("1=(9-8)-0"), "is true");
    print_result_valid("unitest_2.11 ", is_valid_equation_cpp("-7+8=-1"), "is false");
    print_result_valid("unitest_2.12 ", is_valid_equation_cpp("-3+3+7=8"), "is false");
    print_result_valid("unitest_2.13 ", is_valid_equation_cpp("-1-7+8=-1"), "is false");
    print_result_valid("unitest_2.14 ", is_valid_equation_cpp("(3+4)*1=7"), "is true");
    print_result_valid("unitest_2.15 ", is_valid_equation_cpp("(3*4)/2=6"), "is true");
    print_result_valid("unitest_2.16 ", is_valid_equation_cpp("(3*4)*2=24"), "is true");

    // unittest three
    print<std::string>("");
    print<std::string>("#=======================3================================#");
    print_result_valid("unitest_3.1 ", is_valid_equation_cpp("-1+5=-4"), "is false");
    print_result_valid("unitest_3.2 ", is_valid_equation_cpp("(1+2)=3"), "is true");
    print_result_valid("unitest_3.3 ", is_valid_equation_cpp("(1+8-9-1+2)+5=-9"), "is false");
    print_result_valid("unitest_3.4 ", is_valid_equation_cpp("(5*9-6+3)*6=252"), "is true");

    // unitest four
    print<std::string>("");
    print<std::string>("#=======================4=================================#");
    print_result_valid("unitest_4.1 ", is_valid_equation_cpp("-1-5=-3-3"), "is true");
    print_result_valid("unitest_4.2 ", is_valid_equation_cpp("(1+2)=1+2"), "is true");
    print_result_valid("unitest_4.3 ", is_valid_equation_cpp("-1-5=-2-4"), "is true");
    print_result_valid("unitest_4.4 ", is_valid_equation_cpp("2/3*6=1+3"), "is true");
    print_result_valid("unitest_4.5 ", is_valid_equation_cpp("-3*5=-5*3"), "is true");
    print_result_valid("unitest_4.6 ", is_valid_equation_cpp("-7-8=-6-9"), "is true");
    print_result_valid("unitest_4.7 ", is_valid_equation_cpp("1--1+5=2+5"), "is true");
    print_result_valid("unitest_4.8 ", is_valid_equation_cpp("(-1+2)+5=2+4"), "is true");
    print_result_valid("unitest_4.9 ", is_valid_equation_cpp("1+(3-4)+3=0-(-1-2)"), "is true");
    print_result_valid("unitest_4.10 ", is_valid_equation_cpp("8-1^(3/4/2)=1+1+2+3"), "is true");
    print_result_valid("unitest_4.11 ", is_valid_equation_cpp("8-1^(3^4^2)=1--1+2+3"), "is true");
    print_result_valid("unitest_4.12 ", is_valid_equation_cpp("5+3-(9-8)^6=3+2+1--1"), "is true");
    print_result_valid("unitest_4.13 ", is_valid_equation_cpp("5+3-(8-9)^3=2^3+1-1--1"), "is true");
    print_result_valid("unitest_4.14 ", is_valid_equation_cpp("(9-6)^(9-6)=3^(1+1+0+1)"), "is true");
    print_result_valid("unitest_4.15 ", is_valid_equation_cpp("(8-9)^(9-6)=2-2+3-3+4-4-1"), "is true");
    print_result_valid("unitest_4.16 ", is_valid_equation_cpp("(8-9)^(9-5)=3-1-1-1+0^(8-8)"), "is true");
    print_result_valid("unitest_4.17 ", is_valid_equation_cpp("(9-8)^(6-9)=4*9*7-7*9*4+0^(8-8)"), "is true");
    print_result_valid("unitest_4.18 ", is_valid_equation_cpp("1-(2-3)+3+5=1+1+1+1+2+(1+1)+(1--1)"), "is true");
    print_result_valid("unitest_4.19 ", is_valid_equation_cpp("6+(1+5)+2+4-9=(1--1--1)^(1-1+1--1)"), "is true");

    const clock_t end = clock();
    print<std::string>("");
    const double time_check = static_cast<double>(end - start) / CLOCKS_PER_SEC;
    print<std::string>("#~~~~~~~~~~~~~~~~~~~~~~~ TIME UNIT(SEC): ~~~~~~~~~~~~~~~~~~~~~~~~~~~#");
    print<double>(time_check);
    print<std::string>("#~~~~~~~~~~~~~~~~~~~~~~~~~ TIME END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#");
}
