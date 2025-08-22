#include "levels.h"
#include <string.h>

struct EqAddSubBracket AddSubBracket;

void initAddSubBracket() {
	AddSubBracket.digit[0] = 5814;
	strcpy(AddSubBracket.equation[0], "5-8=(1-4), 5=(8+1)-4, 5=8+1-4, (5-8)=1-4, (5-8)=(1-4), 5-8=1-4, 5=8+(1-4)");

	AddSubBracket.digit[1] = 9878;
	strcpy(AddSubBracket.equation[1], "9-(8-7)=8, 9=8-(7-8), 9=8-7+8, 9-8+7=8, (9-8)+7=8, 9=(8-7)+8");

	AddSubBracket.digit[2] = 9584;
	strcpy(AddSubBracket.equation[2], "9=5+(8-4), (9-5)=8-4, 9=(5+8)-4, (9-5)=(8-4), 9-5=(8-4), 9-5=8-4, 9=5+8-4");

	AddSubBracket.digit[3] = 6291;
	strcpy(AddSubBracket.equation[3], "(6+2)=9-1, (6+2)=(9-1), 6+2=(9-1), 6+2=9-1");

	AddSubBracket.digit[4] = 8967;
	strcpy(AddSubBracket.equation[4], "8=9+6-7, (8-9)=(6-7), 8-9=(6-7), 8-9=6-7, 8=9+(6-7), 8=(9+6)-7, (8-9)=6-7");

	AddSubBracket.digit[5] = 3681;
	strcpy(AddSubBracket.equation[5], "3+6=8+1, 3+6=(8+1), (3+6)=(8+1), 3+(6-8)=1, 3+6-8=1, (3+6)-8=1, (3+6)=8+1");

	AddSubBracket.digit[6] = 3416;
	strcpy(AddSubBracket.equation[6], "(3+4)=(1+6), 3+4=(1+6), 3+(4-1)=6, 3+4-1=6, (3+4)-1=6, (3+4)=1+6, 3+4=1+6");

	AddSubBracket.digit[7] = 1528;
	strcpy(AddSubBracket.equation[7], "1+(5+2)=8, 1+5+2=8, (1+5)+2=8");

	AddSubBracket.digit[8] = 3137;
	strcpy(AddSubBracket.equation[8], "3+(1+3)=7, (3+1)+3=7, 3+1+3=7");

	AddSubBracket.digit[9] = 3823;
	strcpy(AddSubBracket.equation[9], "3=(8-2)-3, 3=8-2-3, 3=8-(2+3)");

	AddSubBracket.digit[10] = 9324;
	strcpy(AddSubBracket.equation[10], "9=3+2+4, 9=(3+2)+4, 9-(3+2)=4, 9-3=2+4, (9-3)-2=4, 9-3=(2+4), 9-3-2=4, (9-3)=(2+4), (9-3)=2+4, 9=3+(2+4)");

	AddSubBracket.digit[11] = 3829;
	strcpy(AddSubBracket.equation[11], "3+8=2+9, (3+8)-2=9, 3+8-2=9, 3+(8-2)=9, (3+8)=2+9, (3+8)=(2+9), 3+8=(2+9)");

	AddSubBracket.digit[12] = 8338;
	strcpy(AddSubBracket.equation[12], "8+(3-3)=8, (8-3)+3=8, 8=3-(3-8), 8-(3-3)=8, 8-3+3=8, (8+3)=3+8, 8+3=(3+8), 8=3-3+8, (8+3)=(3+8), 8=(3-3)+8, 8+3-3=8, 8+3=3+8, (8+3)-3=8");

	AddSubBracket.digit[13] = 8679;
	strcpy(AddSubBracket.equation[13], "8=(6-7)+9, 8-6+7=9, 8=6-(7-9), 8-(6-7)=9, 8=6-7+9, (8-6)+7=9");

	AddSubBracket.digit[14] = 3621;
	strcpy(AddSubBracket.equation[14], "3=6-(2+1), 3=6-2-1, 3=(6-2)-1");

	AddSubBracket.digit[15] = 2952;
	strcpy(AddSubBracket.equation[15], "2=(9-5)-2, 2=9-5-2, 2=9-(5+2)");

	AddSubBracket.digit[16] = 6208;
	strcpy(AddSubBracket.equation[16], "(6+2)=(0+8), 6+(2-0)=8, (6+2)-0=8, 6+(2+0)=8, 6+2+0=8, 6+2=(0+8), 6+2-0=8, (6+2)+0=8, 6+2=0+8, (6+2)=0+8");

	AddSubBracket.digit[17] = 6611;
	strcpy(AddSubBracket.equation[17], "(6-6)+1=1, 6=(6-1)+1, 6=6-1+1, 6=(6+1)-1, 6=6-(1-1), 6-6+1=1, 6-(6-1)=1, 6=6+1-1, 6=6+(1-1)");

	AddSubBracket.digit[18] = 7052;
	strcpy(AddSubBracket.equation[18], "7-0=(5+2), 7=0+5+2, (7-0)-5=2, 7-0-5=2, (7+0)-5=2, (7-0)=(5+2), (7-0)=5+2, 7-(0+5)=2, 7+0=(5+2), (7+0)=5+2, 7+0=5+2, 7=(0+5)+2, (7+0)=(5+2), 7=0+(5+2), 7+0-5=2, 7+(0-5)=2, 7-0=5+2");

	AddSubBracket.digit[19] = 7584;
	strcpy(AddSubBracket.equation[19], "7+(5-8)=4, (7+5)=8+4, (7+5)-8=4, (7+5)=(8+4), 7+5-8=4, 7+5=(8+4), 7+5=8+4");

	AddSubBracket.digit[20] = 2439;
	strcpy(AddSubBracket.equation[20], "2+(4+3)=9, (2+4)+3=9, 2+4+3=9");

	AddSubBracket.digit[21] = 7788;
	strcpy(AddSubBracket.equation[21], "7=7-8+8, 7=(7+8)-8, 7=7+8-8, 7=(7-8)+8, 7=7-(8-8), 7-(7-8)=8, 7-7+8=8, (7-7)+8=8, 7=7+(8-8)");

	AddSubBracket.digit[22] = 6846;
	strcpy(AddSubBracket.equation[22], "6=8+(4-6), 6-8=(4-6), 6-8=4-6, 6=8+4-6, 6=(8+4)-6, (6-8)=(4-6), (6-8)=4-6");

	AddSubBracket.digit[23] = 4239;
	strcpy(AddSubBracket.equation[23], "4+2+3=9, (4+2)+3=9, 4+(2+3)=9");

	AddSubBracket.digit[24] = 8154;
	strcpy(AddSubBracket.equation[24], "(8+1)=(5+4), (8+1)-5=4, (8+1)=5+4, 8+1-5=4, 8+1=(5+4), 8+(1-5)=4, 8+1=5+4");

	AddSubBracket.digit[25] = 4466;
	strcpy(AddSubBracket.equation[25], "4=4-6+6, 4=(4-6)+6, 4=(4+6)-6, 4=4-(6-6), 4=4+(6-6), (4-4)+6=6, 4-(4-6)=6, 4=4+6-6, 4-4+6=6");

	AddSubBracket.digit[26] = 6644;
	strcpy(AddSubBracket.equation[26], "6=6+(4-4), (6-6)+4=4, 6=6+4-4, 6=(6-4)+4, 6-6+4=4, 6=6-4+4, 6-(6-4)=4, 6=(6+4)-4, 6=6-(4-4)");

	AddSubBracket.digit[27] = 3737;
	strcpy(AddSubBracket.equation[27], "3=7+(3-7), (3+7)-3=7, 3+7-3=7, (3+7)=(3+7), 3+7=(3+7), 3-7=3-7, 3-7=(3-7), 3=7+3-7, 3+(7-3)=7, 3+7=3+7, 3=(7+3)-7, (3-7)=(3-7), (3-7)=3-7, (3+7)=3+7");

	AddSubBracket.digit[28] = 1791;
	strcpy(AddSubBracket.equation[28], "(1+7)=(9-1), (1+7)=9-1, 1+7=(9-1), 1+7=9-1");

	AddSubBracket.digit[29] = 8620;
	strcpy(AddSubBracket.equation[29], "8=6+2-0, 8=6+2+0, (8-6)=2+0, 8=6+(2+0), 8=(6+2)+0, 8-6=2+0, (8-6)=2-0, 8-6=2-0, (8-6)=(2+0), 8=6+(2-0), 8=(6+2)-0, 8-6=(2-0), (8-6)=(2-0), 8-6=(2+0)");

	AddSubBracket.digit[30] = 5656;
	strcpy(AddSubBracket.equation[30], "(5+6)=(5+6), 5-6=5-6, (5-6)=5-6, 5=6+(5-6), 5=6+5-6, 5+6=(5+6), (5+6)=5+6, 5+6=5+6, 5+(6-5)=6, 5+6-5=6, (5-6)=(5-6), 5-6=(5-6), 5=(6+5)-6, (5+6)-5=6");

	AddSubBracket.digit[31] = 2585;
	strcpy(AddSubBracket.equation[31], "(2-5)+8=5, 2=5-(8-5), 2=(5-8)+5, 2=5-8+5, 2-(5-8)=5, 2-5+8=5");

	AddSubBracket.digit[32] = 7313;
	strcpy(AddSubBracket.equation[32], "7-3=1+3, (7-3)=1+3, (7-3)-1=3, (7-3)=(1+3), 7-(3+1)=3, 7=3+1+3, 7=(3+1)+3, 7-3-1=3, 7-3=(1+3), 7=3+(1+3)");

	AddSubBracket.digit[33] = 5049;
	strcpy(AddSubBracket.equation[33], "(5-0)+4=9, (5+0)+4=9, 5-(0-4)=9, 5=0-(4-9), 5+(0+4)=9, 5=0-4+9, 5-0+4=9, 5+0+4=9, 5=(0-4)+9");

	AddSubBracket.digit[34] = 9746;
	strcpy(AddSubBracket.equation[34], "9=(7-4)+6, (9-7)+4=6, 9-(7-4)=6, 9=7-(4-6), 9-7+4=6, 9=7-4+6");

	AddSubBracket.digit[35] = 4312;
	strcpy(AddSubBracket.equation[35], "4=3-1+2, 4-3+1=2, 4=3-(1-2), 4-(3-1)=2, (4-3)+1=2, 4=(3-1)+2");

	AddSubBracket.digit[36] = 7359;
	strcpy(AddSubBracket.equation[36], "7=(3-5)+9, 7=3-5+9, (7-3)+5=9, 7-(3-5)=9, 7=3-(5-9), 7-3+5=9");

	AddSubBracket.digit[37] = 4796;
	strcpy(AddSubBracket.equation[37], "4=7-9+6, 4=7-(9-6), 4=(7-9)+6, 4-(7-9)=6, 4-7+9=6, (4-7)+9=6");

	AddSubBracket.digit[38] = 8932;
	strcpy(AddSubBracket.equation[38], "8-9+3=2, 8=(9-3)+2, 8=9-3+2, 8=9-(3-2), 8-(9-3)=2, (8-9)+3=2");

	AddSubBracket.digit[39] = 8965;
	strcpy(AddSubBracket.equation[39], "8-(9-6)=5, 8=9-6+5, 8-9+6=5, 8=(9-6)+5, 8=9-(6-5), (8-9)+6=5");

	AddSubBracket.digit[40] = 6129;
	strcpy(AddSubBracket.equation[40], "6+(1+2)=9, (6+1)+2=9, 6+1+2=9");

	AddSubBracket.digit[41] = 3492;
	strcpy(AddSubBracket.equation[41], "(3+4)=9-2, 3+4=9-2, (3+4)=(9-2), 3+4=(9-2)");

	AddSubBracket.digit[42] = 3401;
	strcpy(AddSubBracket.equation[42], "3=(4-0)-1, 3=4-(0+1), (3-4)=0-1, 3=4+(0-1), 3=4+0-1, (3-4)=(0-1), 3=4-0-1, 3-4=(0-1), 3-4=0-1, 3=(4+0)-1");

	AddSubBracket.digit[43] = 2839;
	strcpy(AddSubBracket.equation[43], "2=8+3-9, 2=(8+3)-9, (2-8)=3-9, 2=8+(3-9), 2-8=3-9, (2-8)=(3-9), 2-8=(3-9)");

	AddSubBracket.digit[44] = 9887;
	strcpy(AddSubBracket.equation[44], "9=8+(8-7), 9=(8+8)-7, (9-8)=(8-7), 9-8=(8-7), (9-8)=8-7, 9=8+8-7, 9-8=8-7");

	AddSubBracket.digit[45] = 9812;
	strcpy(AddSubBracket.equation[45], "9-8+1=2, 9-(8-1)=2, 9=8-1+2, 9=8-(1-2), 9=(8-1)+2, (9-8)+1=2");

	AddSubBracket.digit[46] = 6699;
	strcpy(AddSubBracket.equation[46], "6=(6+9)-9, 6=(6-9)+9, (6-6)+9=9, 6=6-(9-9), 6=6-9+9, 6=6+9-9, 6=6+(9-9), 6-(6-9)=9, 6-6+9=9");

	AddSubBracket.digit[47] = 2855;
	strcpy(AddSubBracket.equation[47], "2+(8-5)=5, (2+8)=5+5, (2+8)-5=5, 2+8=(5+5), 2+8-5=5, (2+8)=(5+5), 2+8=5+5");

	AddSubBracket.digit[48] = 9416;
	strcpy(AddSubBracket.equation[48], "9-(4-1)=6, 9=4-(1-6), 9=(4-1)+6, (9-4)+1=6, 9=4-1+6, 9-4+1=6");

	AddSubBracket.digit[49] = 3254;
	strcpy(AddSubBracket.equation[49], "3=2+(5-4), 3-2=5-4, (3-2)=(5-4), (3-2)=5-4, 3-2=(5-4), 3=(2+5)-4, 3=2+5-4");

	AddSubBracket.digit[50] = 2637;
	strcpy(AddSubBracket.equation[50], "2-6=3-7, (2-6)=(3-7), (2-6)=3-7, 2=6+(3-7), 2-6=(3-7), 2=(6+3)-7, 2=6+3-7");

	AddSubBracket.digit[51] = 8172;
	strcpy(AddSubBracket.equation[51], "(8+1)-7=2, 8+(1-7)=2, (8+1)=(7+2), 8+1-7=2, (8+1)=7+2, 8+1=7+2, 8+1=(7+2)");

	AddSubBracket.digit[52] = 5131;
	strcpy(AddSubBracket.equation[52], "5-1-3=1, 5=1+3+1, (5-1)=3+1, 5-1=3+1, 5=(1+3)+1, (5-1)=(3+1), 5=1+(3+1), (5-1)-3=1, 5-1=(3+1), 5-(1+3)=1");

	AddSubBracket.digit[53] = 9630;
	strcpy(AddSubBracket.equation[53], "(9-6)=3-0, 9=6+3-0, 9=(6+3)-0, 9=6+3+0, (9-6)=3+0, (9-6)=(3+0), 9-6=(3-0), 9-6=3+0, 9-6=3-0, 9=6+(3+0), (9-6)=(3-0), 9-6=(3+0), 9=(6+3)+0, 9=6+(3-0)");

	AddSubBracket.digit[54] = 3625;
	strcpy(AddSubBracket.equation[54], "3=6+2-5, 3-6=(2-5), 3=6+(2-5), (3-6)=2-5, 3=(6+2)-5, (3-6)=(2-5), 3-6=2-5");

	AddSubBracket.digit[55] = 5610;
	strcpy(AddSubBracket.equation[55], "5=(6-1)+0, 5=6-1-0, 5=6-1+0, 5=(6-1)-0, 5=6-(1+0), 5=6-(1-0)");

	AddSubBracket.digit[56] = 9900;
	strcpy(AddSubBracket.equation[56], "9=9+(0-0), 9=(9-0)+0, 9=9-(0+0), 9=9+(0+0), 9=(9+0)+0, 9=(9-0)-0, 9=9+0+0, 9=9-0-0, 9=9-0+0, 9=9+0-0, 9=9-(0-0), 9=(9+0)-0");

	AddSubBracket.digit[57] = 7108;
	strcpy(AddSubBracket.equation[57], "7+1=(0+8), 7+(1+0)=8, 7+(1-0)=8, (7+1)+0=8, (7+1)=(0+8), 7+1=0+8, (7+1)-0=8, 7+1+0=8, 7+1-0=8, (7+1)=0+8");

	AddSubBracket.digit[58] = 2262;
	strcpy(AddSubBracket.equation[58], "2+2=(6-2), (2+2)=6-2, 2+2=6-2, (2+2)=(6-2)");

	AddSubBracket.digit[59] = 9180;
	strcpy(AddSubBracket.equation[59], "9=(1+8)+0, (9-1)=8+0, 9=1+(8-0), (9-1)=8-0, (9-1)=(8-0), (9-1)=(8+0), 9-1=(8-0), 9-1=8+0, 9=(1+8)-0, 9=1+8-0, 9-1=(8+0), 9=1+8+0, 9=1+(8+0), 9-1=8-0");

	AddSubBracket.digit[60] = 2011;
	strcpy(AddSubBracket.equation[60], "2-0-1=1, 2+0=1+1, 2=0+(1+1), 2-0=(1+1), (2-0)=1+1, (2-0)-1=1, (2+0)=(1+1), 2+(0-1)=1, 2+0-1=1, 2-0=1+1, (2-0)=(1+1), 2-(0+1)=1, 2=(0+1)+1, (2+0)-1=1, 2+0=(1+1), 2=0+1+1, (2+0)=1+1");

	AddSubBracket.digit[61] = 4613;
	strcpy(AddSubBracket.equation[61], "4=6+(1-3), (4-6)=1-3, 4-6=1-3, 4-6=(1-3), 4=6+1-3, 4=(6+1)-3, (4-6)=(1-3)");

	AddSubBracket.digit[62] = 2684;
	strcpy(AddSubBracket.equation[62], "2-(6-8)=4, 2-6+8=4, 2=6-(8-4), 2=6-8+4, (2-6)+8=4, 2=(6-8)+4");

	AddSubBracket.digit[63] = 2497;
	strcpy(AddSubBracket.equation[63], "2-4+9=7, 2=4-9+7, 2=4-(9-7), 2=(4-9)+7, 2-(4-9)=7, (2-4)+9=7");

	AddSubBracket.digit[64] = 2273;
	strcpy(AddSubBracket.equation[64], "(2+2)=7-3, 2+2=(7-3), 2+2=7-3, (2+2)=(7-3)");

	AddSubBracket.digit[65] = 2828;
	strcpy(AddSubBracket.equation[65], "2=8+2-8, (2-8)=(2-8), 2+(8-2)=8, (2-8)=2-8, 2-8=(2-8), (2+8)=(2+8), 2+8=2+8, (2+8)-2=8, (2+8)=2+8, 2+8=(2+8), 2=8+(2-8), 2-8=2-8, 2+8-2=8, 2=(8+2)-8");

	AddSubBracket.digit[66] = 2552;
	strcpy(AddSubBracket.equation[66], "(2+5)=5+2, 2=5-5+2, (2+5)-5=2, 2+(5-5)=2, (2+5)=(5+2), 2-(5-5)=2, 2-5+5=2, 2+5=5+2, 2+5-5=2, (2-5)+5=2, 2+5=(5+2), 2=(5-5)+2, 2=5-(5-2)");

	AddSubBracket.digit[67] = 6583;
	strcpy(AddSubBracket.equation[67], "6+5=8+3, 6+(5-8)=3, 6+5-8=3, (6+5)=(8+3), 6+5=(8+3), (6+5)-8=3, (6+5)=8+3");

	AddSubBracket.digit[68] = 6114;
	strcpy(AddSubBracket.equation[68], "6-1=(1+4), (6-1)=(1+4), (6-1)=1+4, (6-1)-1=4, 6=(1+1)+4, 6=1+(1+4), 6=1+1+4, 6-1-1=4, 6-1=1+4, 6-(1+1)=4");

	AddSubBracket.digit[69] = 8945;
	strcpy(AddSubBracket.equation[69], "(8-9)=4-5, 8=9+4-5, 8-9=(4-5), 8-9=4-5, 8=(9+4)-5, 8=9+(4-5), (8-9)=(4-5)");

	AddSubBracket.digit[70] = 4105;
	strcpy(AddSubBracket.equation[70], "(4+1)+0=5, 4+1=(0+5), 4+(1+0)=5, (4+1)=(0+5), 4+1+0=5, (4+1)=0+5, 4+(1-0)=5, (4+1)-0=5, 4+1-0=5, 4+1=0+5");

	AddSubBracket.digit[71] = 6435;
	strcpy(AddSubBracket.equation[71], "6=(4-3)+5, 6=4-3+5, 6=4-(3-5), 6-(4-3)=5, 6-4+3=5, (6-4)+3=5");

	AddSubBracket.digit[72] = 3917;
	strcpy(AddSubBracket.equation[72], "(3-9)=(1-7), 3=9+1-7, 3=9+(1-7), (3-9)=1-7, 3-9=1-7, 3-9=(1-7), 3=(9+1)-7");

	AddSubBracket.digit[73] = 1155;
	strcpy(AddSubBracket.equation[73], "1=1-(5-5), 1=(1-5)+5, 1=(1+5)-5, 1=1-5+5, (1-1)+5=5, 1=1+(5-5), 1-1+5=5, 1=1+5-5, 1-(1-5)=5");

	AddSubBracket.digit[74] = 5522;
	strcpy(AddSubBracket.equation[74], "5=(5-2)+2, 5=(5+2)-2, 5-(5-2)=2, (5-5)+2=2, 5=5-2+2, 5-5+2=2, 5=5+(2-2), 5=5-(2-2), 5=5+2-2");

	AddSubBracket.digit[75] = 2169;
	strcpy(AddSubBracket.equation[75], "(2+1)+6=9, 2+(1+6)=9, 2+1+6=9");

	AddSubBracket.digit[76] = 7452;
	strcpy(AddSubBracket.equation[76], "(7-4)=(5-2), 7=4+(5-2), 7=4+5-2, 7=(4+5)-2, 7-4=5-2, (7-4)=5-2, 7-4=(5-2)");

	AddSubBracket.digit[77] = 5353;
	strcpy(AddSubBracket.equation[77], "5+3=(5+3), 5=3+(5-3), 5=(3+5)-3, 5=3+5-3, (5+3)-5=3, 5-3=5-3, (5-3)=(5-3), (5-3)=5-3, 5+3-5=3, 5-3=(5-3), 5+3=5+3, (5+3)=5+3, 5+(3-5)=3, (5+3)=(5+3)");

	AddSubBracket.digit[78] = 2002;
	strcpy(AddSubBracket.equation[78], "(2-0)=0+2, (2+0)=(0+2), 2=0-0+2, (2+0)-0=2, 2=0+(0+2), (2-0)+0=2, (2+0)=0+2, 2-0=(0+2), 2-(0+0)=2, 2=0+0+2, 2+(0-0)=2, 2-0-0=2, 2-0=0+2, 2=0-(0-2), 2+0+0=2, 2-0+0=2, 2-(0-0)=2, (2+0)+0=2, 2+(0+0)=2, (2-0)=(0+2), 2=(0+0)+2, 2+0=0+2, 2+0-0=2, (2-0)-0=2, 2=(0-0)+2, 2+0=(0+2)");

	AddSubBracket.digit[79] = 3524;
	strcpy(AddSubBracket.equation[79], "3=(5+2)-4, 3-5=(2-4), (3-5)=2-4, (3-5)=(2-4), 3=5+(2-4), 3=5+2-4, 3-5=2-4");

	AddSubBracket.digit[80] = 8877;
	strcpy(AddSubBracket.equation[80], "8=(8-7)+7, 8=8+(7-7), 8-8+7=7, 8-(8-7)=7, 8=8+7-7, 8=(8+7)-7, 8=8-7+7, (8-8)+7=7, 8=8-(7-7)");

	AddSubBracket.digit[81] = 4725;
	strcpy(AddSubBracket.equation[81], "4=(7+2)-5, (4-7)=2-5, 4-7=2-5, 4=7+2-5, 4-7=(2-5), (4-7)=(2-5), 4=7+(2-5)");

	AddSubBracket.digit[82] = 3432;
	strcpy(AddSubBracket.equation[82], "(3-4)+3=2, 3-4+3=2, 3=(4-3)+2, 3=4-3+2, 3-(4-3)=2, 3=4-(3-2)");

	AddSubBracket.digit[83] = 7294;
	strcpy(AddSubBracket.equation[83], "7-2=(9-4), 7=2+9-4, (7-2)=9-4, 7=2+(9-4), (7-2)=(9-4), 7=(2+9)-4, 7-2=9-4");

	AddSubBracket.digit[84] = 4356;
	strcpy(AddSubBracket.equation[84], "4=3-5+6, 4=3-(5-6), 4-3+5=6, (4-3)+5=6, 4=(3-5)+6, 4-(3-5)=6");

	AddSubBracket.digit[85] = 7034;
	strcpy(AddSubBracket.equation[85], "(7-0)=3+4, 7+(0-3)=4, 7=(0+3)+4, 7-(0+3)=4, 7-0-3=4, 7+0=(3+4), (7+0)-3=4, 7+0-3=4, 7=0+3+4, 7+0=3+4, 7=0+(3+4), (7-0)=(3+4), 7-0=(3+4), (7+0)=3+4, 7-0=3+4, (7+0)=(3+4), (7-0)-3=4");

	AddSubBracket.digit[86] = 5140;
	strcpy(AddSubBracket.equation[86], "5-1=(4-0), 5=1+4+0, (5-1)=4+0, (5-1)=4-0, 5-1=(4+0), 5=1+4-0, 5-1=4+0, (5-1)=(4-0), 5=(1+4)-0, 5=(1+4)+0, 5=1+(4-0), (5-1)=(4+0), 5-1=4-0, 5=1+(4+0)");

	AddSubBracket.digit[87] = 5643;
	strcpy(AddSubBracket.equation[87], "5-6+4=3, 5=6-(4-3), (5-6)+4=3, 5-(6-4)=3, 5=6-4+3, 5=(6-4)+3");

	AddSubBracket.digit[88] = 4152;
	strcpy(AddSubBracket.equation[88], "(4-1)=5-2, 4=1+(5-2), (4-1)=(5-2), 4-1=(5-2), 4=(1+5)-2, 4=1+5-2, 4-1=5-2");

	AddSubBracket.digit[89] = 8921;
	strcpy(AddSubBracket.equation[89], "8=(9-2)+1, 8=9-2+1, 8=9-(2-1), 8-9+2=1, (8-9)+2=1, 8-(9-2)=1");

	AddSubBracket.digit[90] = 1315;
	strcpy(AddSubBracket.equation[90], "(1+3)+1=5, 1+3+1=5, 1+(3+1)=5");

	AddSubBracket.digit[91] = 5142;
	strcpy(AddSubBracket.equation[91], "5+1=(4+2), 5+(1-4)=2, (5+1)=4+2, 5+1=4+2, 5+1-4=2, (5+1)-4=2, (5+1)=(4+2)");

	AddSubBracket.digit[92] = 5841;
	strcpy(AddSubBracket.equation[92], "5=(8-4)+1, 5=8-4+1, 5-8+4=1, 5-(8-4)=1, (5-8)+4=1, 5=8-(4-1)");

	AddSubBracket.digit[93] = 4103;
	strcpy(AddSubBracket.equation[93], "(4-1)=(0+3), 4=1+0+3, 4=1+(0+3), 4=1-0+3, (4-1)-0=3, 4=1-(0-3), 4-1=0+3, 4-1+0=3, (4-1)=0+3, 4-(1-0)=3, 4=(1-0)+3, 4-1-0=3, 4=(1+0)+3, 4-1=(0+3), (4-1)+0=3, 4-(1+0)=3");

	AddSubBracket.digit[94] = 7254;
	strcpy(AddSubBracket.equation[94], "(7+2)=(5+4), 7+(2-5)=4, 7+2=5+4, (7+2)-5=4, (7+2)=5+4, 7+2-5=4, 7+2=(5+4)");

	AddSubBracket.digit[95] = 4826;
	strcpy(AddSubBracket.equation[95], "4=8+2-6, (4-8)=2-6, 4-8=2-6, 4=8+(2-6), (4-8)=(2-6), 4=(8+2)-6, 4-8=(2-6)");

	AddSubBracket.digit[96] = 9382;
	strcpy(AddSubBracket.equation[96], "9=3+(8-2), (9-3)=(8-2), 9-3=8-2, 9=(3+8)-2, 9-3=(8-2), (9-3)=8-2, 9=3+8-2");

	AddSubBracket.digit[97] = 1964;
	strcpy(AddSubBracket.equation[97], "1+9=(6+4), 1+9=6+4, (1+9)=(6+4), 1+(9-6)=4, (1+9)-6=4, 1+9-6=4, (1+9)=6+4");

	AddSubBracket.digit[98] = 7362;
	strcpy(AddSubBracket.equation[98], "7=3+6-2, 7=(3+6)-2, 7=3+(6-2), (7-3)=(6-2), 7-3=(6-2), 7-3=6-2, (7-3)=6-2");

	AddSubBracket.digit[99] = 3557;
	strcpy(AddSubBracket.equation[99], "3-5=5-7, 3=(5+5)-7, 3=5+(5-7), (3-5)=5-7, 3-5=(5-7), (3-5)=(5-7), 3=5+5-7");
}