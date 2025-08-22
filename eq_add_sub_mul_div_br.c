#include "levels.h"
#include <string.h>

struct EqAddSubMulDivBracket AddSubMulDivBracket;

void initAddSubMulDivBracket() {
	AddSubMulDivBracket.digit[0] = 6876;
	strcpy(AddSubMulDivBracket.equation[0], "6*(8-7)=6, 6=(8-7)*6, 6/(8-7)=6");

	AddSubMulDivBracket.digit[1] = 3513;
	strcpy(AddSubMulDivBracket.equation[1], "(3-5)=1-3, 3=(5+1)-3, 3=5+(1-3), 3-5=(1-3), 3-5=1-3, 3=5+1-3, (3-5)=(1-3)");

	AddSubMulDivBracket.digit[2] = 6056;
	strcpy(AddSubMulDivBracket.equation[2], "6=0/5+6, 6+(0/5)=6, 6+0/5=6, 6-(0*5)=6, 6-(0/5)=6, 6+(0*5)=6, 6-0/5=6, 6-0*5=6, 6+0*5=6, 6=(0*5)+6, 6=0*5+6, 6=(0/5)+6");

	AddSubMulDivBracket.digit[3] = 8935;
	strcpy(AddSubMulDivBracket.equation[3], "8=(9/3)+5, 8=9/3+5, 8-9/3=5, 8-(9/3)=5");

	AddSubMulDivBracket.digit[4] = 3865;
	strcpy(AddSubMulDivBracket.equation[4], "(3+8)=6+5, (3+8)-6=5, 3+(8-6)=5, 3+8-6=5, 3+8=6+5, 3+8=(6+5), (3+8)=(6+5)");

	AddSubMulDivBracket.digit[5] = 5317;
	strcpy(AddSubMulDivBracket.equation[5], "5+3=1+7, 5+(3-1)=7, 5+3-1=7, (5+3)-1=7, (5+3)=(1+7), 5+3=(1+7), (5+3)=1+7");

	AddSubMulDivBracket.digit[6] = 2209;
	strcpy(AddSubMulDivBracket.equation[6], "2=2-0/9, 2=2-(0*9), 2=2-(0/9), 2=2+0/9, 2=2+(0/9), 2=2-0*9, 2=2+0*9, 2=2+(0*9)");

	AddSubMulDivBracket.digit[7] = 5234;
	strcpy(AddSubMulDivBracket.equation[7], "(5+2)=3+4, (5+2)-3=4, 5+(2-3)=4, (5+2)=(3+4), 5+2=3+4, 5+2=(3+4), 5+2-3=4");

	AddSubMulDivBracket.digit[8] = 4244;
	strcpy(AddSubMulDivBracket.equation[8], "(4*2)=(4+4), (4*2)=4+4, 4*2=(4+4), 4=(2*4)-4, 4=2*4-4, (4*2)-4=4, 4*2=4+4, 4*2-4=4");

	AddSubMulDivBracket.digit[9] = 8624;
	strcpy(AddSubMulDivBracket.equation[9], "8-(6-2)=4, (8-6)+2=4, 8=6*2-4, (8-6)*2=4, 8=(6*2)-4, 8=6-(2-4), 8=6-2+4, 8=(6-2)+4, 8-6+2=4");

	AddSubMulDivBracket.digit[10] = 3524;
	strcpy(AddSubMulDivBracket.equation[10], "(3+5)=(2*4), 3=(5+2)-4, 3-5=(2-4), 3+5=2*4, (3+5)=2*4, (3-5)=2-4, 3+5=(2*4), (3-5)=(2-4), 3=5+(2-4), 3=5+2-4, 3-5=2-4, (3+5)/2=4");

	AddSubMulDivBracket.digit[11] = 3287;
	strcpy(AddSubMulDivBracket.equation[11], "3=2+8-7, 3=2+(8-7), 3-2=8-7, 3=(2+8)-7, 3-2=(8-7), (3-2)=8-7, (3-2)=(8-7)");

	AddSubMulDivBracket.digit[12] = 4859;
	strcpy(AddSubMulDivBracket.equation[12], "4=(8+5)-9, 4=8+5-9, 4-8=(5-9), 4-8=5-9, (4-8)=5-9, (4-8)=(5-9), 4=8+(5-9)");

	AddSubMulDivBracket.digit[13] = 2602;
	strcpy(AddSubMulDivBracket.equation[13], "2-(6*0)=2, 2-6*0=2, 2+(6*0)=2, 2=6*0+2, 2+6*0=2, 2=(6*0)+2");

	AddSubMulDivBracket.digit[14] = 2052;
	strcpy(AddSubMulDivBracket.equation[14], "2+0/5=2, 2=0/5+2, 2-(0*5)=2, 2+(0/5)=2, 2=0*5+2, 2+(0*5)=2, 2=(0/5)+2, 2-0*5=2, 2+0*5=2, 2=(0*5)+2, 2-(0/5)=2, 2-0/5=2");

	AddSubMulDivBracket.digit[15] = 6734;
	strcpy(AddSubMulDivBracket.equation[15], "(6-7)=(3-4), 6=7+3-4, 6=7+(3-4), 6=(7+3)-4, 6-7=(3-4), 6-7=3-4, (6-7)=3-4");

	AddSubMulDivBracket.digit[16] = 1248;
	strcpy(AddSubMulDivBracket.equation[16], "1=2*(4/8), 1=2*4/8, 1*(2*4)=8, 1/2=4/8, (1*2)*4=8, 1/2=(4/8), (1/2)=4/8, (1/2)=(4/8), 1=(2*4)/8, 1*2*4=8");

	AddSubMulDivBracket.digit[17] = 7543;
	strcpy(AddSubMulDivBracket.equation[17], "(7+5)=4*3, (7+5)=(4*3), (7+5)/4=3, 7+5=(4*3), 7+5=4*3");

	AddSubMulDivBracket.digit[18] = 6060;
	strcpy(AddSubMulDivBracket.equation[18], "6-0=6+0, 6=(0+6)-0, (6+0)=6+0, (6+0)=6-0, 6=(0+6)+0, 6+0=(6+0), 6=0+6-0, 6=0+(6+0), 6+0=6-0, (6-0)=(6+0), 6+0=(6-0), (6-0)=6-0, 6-0=(6-0), 6+0=6+0, 6-0=(6+0), 6=0+(6-0), (6-0)=(6-0), (6+0)=(6-0), (6+0)=(6+0), 6=0+6+0, 6-0=6-0, (6-0)=6+0");

	AddSubMulDivBracket.digit[19] = 6921;
	strcpy(AddSubMulDivBracket.equation[19], "6=9-(2+1), 6=9-2-1, 6=(9-2)-1");

	AddSubMulDivBracket.digit[20] = 2531;
	strcpy(AddSubMulDivBracket.equation[20], "2=5-(3/1), 2=5-3/1, 2=5-(3*1), 2=5-3*1, 2/(5-3)=1, 2=(5-3)/1, 2=(5-3)*1");

	AddSubMulDivBracket.digit[21] = 5140;
	strcpy(AddSubMulDivBracket.equation[21], "5-1=(4-0), 5=1+4+0, (5-1)=4+0, (5-1)=4-0, 5-1=(4+0), 5=1+4-0, 5-1=4+0, (5-1)=(4-0), 5=(1+4)-0, 5=(1+4)+0, 5=1+(4-0), (5-1)=(4+0), 5-1=4-0, 5=1+(4+0)");

	AddSubMulDivBracket.digit[22] = 9146;
	strcpy(AddSubMulDivBracket.equation[22], "(9+1)=(4+6), 9+(1-4)=6, (9+1)-4=6, (9+1)=4+6, 9+1=4+6, 9+1-4=6, 9+1=(4+6)");

	AddSubMulDivBracket.digit[23] = 5133;
	strcpy(AddSubMulDivBracket.equation[23], "5+(1-3)=3, 5+1=3+3, (5+1)-3=3, 5+1=(3+3), 5+1-3=3, (5+1)=3+3, (5+1)=(3+3)");

	AddSubMulDivBracket.digit[24] = 2825;
	strcpy(AddSubMulDivBracket.equation[24], "(2+8)/2=5, (2+8)=2*5, 2+8=(2*5), (2+8)=(2*5), 2+8=2*5, 2=(8+2)/5");

	AddSubMulDivBracket.digit[25] = 8162;
	strcpy(AddSubMulDivBracket.equation[25], "8=1*(6+2), 8*1-6=2, 8/1=(6+2), 8-1*6=2, 8-(1*6)=2, (8*1)=6+2, 8*1=6+2, 8/1=6+2, 8=(1*6)+2, (8/1)-6=2, (8*1)=(6+2), (8/1)=6+2, 8*1=(6+2), 8=1*6+2, (8/1)=(6+2), (8*1)-6=2, 8/1-6=2");

	AddSubMulDivBracket.digit[26] = 4440;
	strcpy(AddSubMulDivBracket.equation[26], "4=4-4*0, 4=4+(4*0), 4=4+4*0, 4=4-(4*0)");

	AddSubMulDivBracket.digit[27] = 3803;
	strcpy(AddSubMulDivBracket.equation[27], "3+8*0=3, 3=8*0+3, 3-8*0=3, 3=(8*0)+3, 3-(8*0)=3, 3+(8*0)=3");

	AddSubMulDivBracket.digit[28] = 6406;
	strcpy(AddSubMulDivBracket.equation[28], "6+(4*0)=6, 6=4*0+6, 6+4*0=6, 6=(4*0)+6, 6-4*0=6, 6-(4*0)=6");

	AddSubMulDivBracket.digit[29] = 6206;
	strcpy(AddSubMulDivBracket.equation[29], "6-2*0=6, 6=2*0+6, 6=(2*0)+6, 6-(2*0)=6, 6+(2*0)=6, 6+2*0=6");

	AddSubMulDivBracket.digit[30] = 1241;
	strcpy(AddSubMulDivBracket.equation[30], "(1+2)=4-1, 1+2=4-1, 1+2=(4-1), (1+2)=(4-1)");

	AddSubMulDivBracket.digit[31] = 4613;
	strcpy(AddSubMulDivBracket.equation[31], "4=6+(1-3), 4-6=1-3, 4-6=(1-3), 4=(6+1)-3, 4=6+1-3, (4-6)=1-3, (4-6)=(1-3)");

	AddSubMulDivBracket.digit[32] = 2064;
	strcpy(AddSubMulDivBracket.equation[32], "2+0=6-4, (2-0)=(6-4), 2=(0+6)-4, (2-0)=6-4, 2+0=(6-4), (2+0)=(6-4), 2=0+(6-4), 2-0=6-4, 2-0=(6-4), (2+0)=6-4, 2=0+6-4");

	AddSubMulDivBracket.digit[33] = 2144;
	strcpy(AddSubMulDivBracket.equation[33], "(2-1)=(4/4), 2=1+4/4, 2-1=(4/4), (2-1)=4/4, (2-1)*4=4, 2-1=4/4, 2=1+(4/4)");

	AddSubMulDivBracket.digit[34] = 4730;
	strcpy(AddSubMulDivBracket.equation[34], "4=7-(3-0), 4=7-3+0, 4=(7-3)-0, 4=7-(3+0), 4=7-3-0, 4=(7-3)+0");

	AddSubMulDivBracket.digit[35] = 3763;
	strcpy(AddSubMulDivBracket.equation[35], "3=(7-6)*3, 3*(7-6)=3, 3/(7-6)=3");

	AddSubMulDivBracket.digit[36] = 7268;
	strcpy(AddSubMulDivBracket.equation[36], "7*2=(6+8), 7*2=6+8, (7*2)-6=8, (7*2)=(6+8), 7*2-6=8, (7*2)=6+8");

	AddSubMulDivBracket.digit[37] = 1293;
	strcpy(AddSubMulDivBracket.equation[37], "(1+2)=(9/3), 1+2=(9/3), 1+2=9/3, (1+2)=9/3");

	AddSubMulDivBracket.digit[38] = 6327;
	strcpy(AddSubMulDivBracket.equation[38], "6+3=2+7, 6+(3-2)=7, (6+3)-2=7, (6+3)=2+7, (6+3)=(2+7), 6+3-2=7, 6+3=(2+7)");

	AddSubMulDivBracket.digit[39] = 3433;
	strcpy(AddSubMulDivBracket.equation[39], "3/(4-3)=3, 3=4-(3/3), 3*(4-3)=3, 3=(4-3)*3, 3=4-3/3");

	AddSubMulDivBracket.digit[40] = 4311;
	strcpy(AddSubMulDivBracket.equation[40], "4=3+1/1, (4-3)*1=1, 4-3/1=1, (4-3)=(1/1), 4=(3+1)/1, 4-3=1*1, (4-3)=1/1, 4=(3*1)+1, 4-3=(1*1), 4-(3*1)=1, 4=3+(1/1), 4-3=1/1, 4=3*1+1, (4-3)=(1*1), 4-3*1=1, 4=3/1+1, 4=3+1*1, 4=(3/1)+1, 4/(3+1)=1, (4-3)=1*1, 4=3+(1*1), 4=(3+1)*1, (4-3)/1=1, 4-3=(1/1), 4-(3/1)=1");

	AddSubMulDivBracket.digit[41] = 9117;
	strcpy(AddSubMulDivBracket.equation[41], "9-1=(1+7), 9=1+1+7, (9-1)=1+7, 9-(1+1)=7, 9=1+(1+7), (9-1)=(1+7), 9=(1+1)+7, 9-1=1+7, (9-1)-1=7, 9-1-1=7");

	AddSubMulDivBracket.digit[42] = 7017;
	strcpy(AddSubMulDivBracket.equation[42], "(7-0)/1=7, 7-(0/1)=7, 7-0=(1*7), 7-0/1=7, (7+0)=(1*7), 7+(0*1)=7, 7+0=(1*7), 7-0*1=7, 7=0+(1*7), (7+0)/1=7, (7+0)*1=7, 7+0*1=7, 7+(0/1)=7, (7-0)=(1*7), 7=(0+1)*7, (7+0)=1*7, 7+0/1=7, 7=(0*1)+7, 7-(0*1)=7, 7=0/1+7, 7=0+1*7, (7-0)*1=7, 7=0*1+7, 7+0=1*7, (7-0)=1*7, 7*(0+1)=7, 7/(0+1)=7, 7=(0/1)+7, 7-0=1*7");

	AddSubMulDivBracket.digit[43] = 1441;
	strcpy(AddSubMulDivBracket.equation[43], "(1*4)=4*1, (1+4)=(4+1), 1*4=(4*1), 1=4/4*1, (1*4)/4=1, 1+4-4=1, (1-4)+4=1, 1*4=4*1, 1-(4-4)=1, 1+4=(4+1), 1*4/4=1, 1=4/4/1, 1=4/(4/1), 1*4=(4/1), 1=(4/4)/1, 1*4=4/1, (1*4)=(4/1), (1*4)=(4*1), 1/4*4=1, (1*4)=4/1, 1+4=4+1, 1*(4/4)=1, 1/(4/4)=1, (1+4)=4+1, 1=(4-4)+1, 1-4+4=1, 1=4-4+1, 1=(4/4)*1, 1=4-(4-1), (1+4)-4=1, 1+(4-4)=1, 1=4/(4*1), (1/4)*4=1");

	AddSubMulDivBracket.digit[44] = 1322;
	strcpy(AddSubMulDivBracket.equation[44], "(1+3)/2=2, 1+3-2=2, 1+3=(2+2), 1+3=(2*2), 1+(3-2)=2, 1+3=2*2, 1+3=2+2, (1+3)=(2+2), (1+3)-2=2, (1+3)=2*2, (1+3)=2+2, (1+3)=(2*2)");

	AddSubMulDivBracket.digit[45] = 2902;
	strcpy(AddSubMulDivBracket.equation[45], "2+(9*0)=2, 2=(9*0)+2, 2-(9*0)=2, 2-9*0=2, 2=9*0+2, 2+9*0=2");

	AddSubMulDivBracket.digit[46] = 1168;
	strcpy(AddSubMulDivBracket.equation[46], "1+(1+6)=8, (1+1)+6=8, 1+1+6=8");

	AddSubMulDivBracket.digit[47] = 2174;
	strcpy(AddSubMulDivBracket.equation[47], "(2+1)=7-4, 2+1=(7-4), (2+1)=(7-4), 2+1=7-4, 2=(1+7)/4");

	AddSubMulDivBracket.digit[48] = 3653;
	strcpy(AddSubMulDivBracket.equation[48], "3=6/(5-3), 3=(6-5)*3, 3*(6-5)=3, 3/(6-5)=3");

	AddSubMulDivBracket.digit[49] = 8080;
	strcpy(AddSubMulDivBracket.equation[49], "8=0+8-0, 8+0=8-0, 8=(0+8)+0, (8+0)=(8+0), 8+0=(8+0), (8-0)=8+0, 8=0+(8-0), (8+0)=(8-0), 8=0+(8+0), 8-0=(8-0), 8+0=(8-0), 8-0=(8+0), 8-0=8+0, (8+0)=8+0, (8+0)=8-0, 8-0=8-0, (8-0)=(8-0), 8=(0+8)-0, (8-0)=8-0, 8=0+8+0, 8+0=8+0, (8-0)=(8+0)");

	AddSubMulDivBracket.digit[50] = 6445;
	strcpy(AddSubMulDivBracket.equation[50], "6=4/4+5, 6-(4/4)=5, 6=(4/4)+5, 6-4/4=5");

	AddSubMulDivBracket.digit[51] = 6506;
	strcpy(AddSubMulDivBracket.equation[51], "6=(5*0)+6, 6-(5*0)=6, 6+5*0=6, 6+(5*0)=6, 6=5*0+6, 6-5*0=6");

	AddSubMulDivBracket.digit[52] = 6993;
	strcpy(AddSubMulDivBracket.equation[52], "6=(9+9)/3, 6=9-9/3, 6=9-(9/3)");

	AddSubMulDivBracket.digit[53] = 2406;
	strcpy(AddSubMulDivBracket.equation[53], "2+(4-0)=6, 2+4-0=6, (2+4)=0+6, (2+4)-0=6, 2+4+0=6, (2+4)=(0+6), 2+4=(0+6), 2+4=0+6, 2+(4+0)=6, (2+4)+0=6");

	AddSubMulDivBracket.digit[54] = 8997;
	strcpy(AddSubMulDivBracket.equation[54], "8-(9/9)=7, 8=(9/9)+7, 8-9/9=7, 8=9/9+7");

	AddSubMulDivBracket.digit[55] = 7853;
	strcpy(AddSubMulDivBracket.equation[55], "7+8=(5*3), (7+8)=5*3, (7+8)=(5*3), 7+8=5*3, (7+8)/5=3");

	AddSubMulDivBracket.digit[56] = 6775;
	strcpy(AddSubMulDivBracket.equation[56], "6=(7/7)+5, 6=7/7+5, 6-(7/7)=5, 6-7/7=5");

	AddSubMulDivBracket.digit[57] = 5041;
	strcpy(AddSubMulDivBracket.equation[57], "5=0+(4+1), (5-0)-4=1, (5-0)=(4+1), 5=(0+4)+1, 5+0-4=1, 5-0-4=1, (5+0)=4+1, (5+0)=(4+1), 5-0=(4+1), 5-0=4+1, 5-(0+4)=1, 5+0=4+1, 5=0+4+1, 5+0=(4+1), 5+(0-4)=1, (5-0)=4+1, (5+0)-4=1");

	AddSubMulDivBracket.digit[58] = 5150;
	strcpy(AddSubMulDivBracket.equation[58], "5*1=5+0, (5*1)=5+0, (5/1)=5+0, 5=1*5-0, 5/1=5-0, 5=1*5+0, (5*1)=(5+0), 5*1=(5+0), (5*1)=5-0, (5*1)=(5-0), (5/1)=5-0, 5=1*(5+0), 5*1=(5-0), 5=(1*5)+0, 5/1=(5+0), 5/1=5+0, 5=1*(5-0), 5=(1*5)-0, (5/1)=(5+0), (5/1)=(5-0), 5/1=(5-0), 5*1=5-0");

	AddSubMulDivBracket.digit[59] = 3322;
	strcpy(AddSubMulDivBracket.equation[59], "3=3-2+2, 3=(3/2)*2, 3=(3-2)+2, 3-(3-2)=2, 3-3+2=2, 3=3*(2/2), 3/(3/2)=2, 3/3*2=2, 3/3=(2/2), 3=3/(2/2), 3=(3*2)/2, 3=3+(2-2), 3=3*2/2, (3/3)*2=2, 3=3-(2-2), 3=3+2-2, 3/3=2/2, 3=(3+2)-2, (3/3)=(2/2), (3-3)+2=2, (3/3)=2/2, 3=3/2*2");

	AddSubMulDivBracket.digit[60] = 2214;
	strcpy(AddSubMulDivBracket.equation[60], "(2+2)=(1*4), 2*2=(1*4), 2+2/1=4, (2*2)/1=4, 2*2=1*4, (2*2)=(1*4), 2*2*1=4, 2+2=(1*4), (2+2)=1*4, 2+2*1=4, (2+2)/1=4, 2*(2/1)=4, (2*2)*1=4, 2*2/1=4, (2+2)*1=4, 2+(2/1)=4, 2+2=1*4, 2+(2*1)=4, 2*(2*1)=4, (2*2)=1*4");

	AddSubMulDivBracket.digit[61] = 2240;
	strcpy(AddSubMulDivBracket.equation[61], "(2*2)=(4+0), 2*2=(4-0), (2+2)=(4-0), (2*2)=4-0, 2=2-(4*0), 2+2=(4+0), (2+2)=(4+0), 2=2+(4*0), 2*2=4-0, 2+2=4+0, (2+2)=4-0, 2*2=4+0, (2+2)=4+0, 2*2=(4+0), 2+2=(4-0), 2+2=4-0, 2=2+4*0, (2*2)=4+0, 2=2-4*0, (2*2)=(4-0)");

	AddSubMulDivBracket.digit[62] = 6026;
	strcpy(AddSubMulDivBracket.equation[62], "6+(0/2)=6, 6+0/2=6, 6=(0*2)+6, 6=0*2+6, 6+(0*2)=6, 6-0/2=6, 6-(0/2)=6, 6=0/2+6, 6-0*2=6, 6-(0*2)=6, 6+0*2=6, 6=(0/2)+6");

	AddSubMulDivBracket.digit[63] = 5577;
	strcpy(AddSubMulDivBracket.equation[63], "5-(5-7)=7, 5=5+7-7, 5=5-7+7, (5/5)=(7/7), 5=5+(7-7), 5-5+7=7, 5/5=7/7, 5/(5/7)=7, 5=5*7/7, 5/5*7=7, 5=5/7*7, 5=(5-7)+7, (5/5)=7/7, 5=5/(7/7), 5/5=(7/7), 5=(5*7)/7, 5=(5/7)*7, (5/5)*7=7, 5=5*(7/7), (5-5)+7=7, 5=5-(7-7), 5=(5+7)-7");

	AddSubMulDivBracket.digit[64] = 4916;
	strcpy(AddSubMulDivBracket.equation[64], "(4-9)=1-6, (4-9)=(1-6), 4=9+(1-6), 4=(9+1)-6, 4-9=1-6, 4-9=(1-6), 4=9+1-6");

	AddSubMulDivBracket.digit[65] = 2145;
	strcpy(AddSubMulDivBracket.equation[65], "2=1-4+5, 2=(1-4)+5, 2-(1-4)=5, (2-1)+4=5, 2-1+4=5, 2=1-(4-5)");

	AddSubMulDivBracket.digit[66] = 5554;
	strcpy(AddSubMulDivBracket.equation[66], "5/5=(5-4), (5/5)=5-4, 5=5/(5-4), 5=5*(5-4), 5-(5/5)=4, 5/5=5-4, (5/5)=(5-4), 5-5/5=4, 5=(5/5)+4, 5=5/5+4");

	AddSubMulDivBracket.digit[67] = 2243;
	strcpy(AddSubMulDivBracket.equation[67], "2/2=4-3, 2/2=(4-3), 2=(2+4)/3, 2=2*(4-3), 2=2/(4-3), (2/2)=(4-3), (2/2)=4-3");

