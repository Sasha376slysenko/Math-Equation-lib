#ifndef LEVELS_H
#define LEVELS_H

void initeq_4();
void initeq_5();
void initeq_6();
void initeq_7();
void initeq_8();

struct EQ_4 {
	unsigned int digit[10];
	char equation[10][286];
};
struct EQ_5 {
	unsigned int digit[10];
	char equation[10][2937];
};
struct EQ_6 {
	unsigned int digit[10];
	char equation[10][5088];
};
struct EQ_7 {
	unsigned int digit[10];
	char equation[10][12231];
};
struct EQ_8 {
	unsigned int digit[10];
	char equation[10][32898];
};

extern struct EQ_4 eq_4;
extern struct EQ_5 eq_5;
extern struct EQ_6 eq_6;
extern struct EQ_7 eq_7;
extern struct EQ_8 eq_8;
#endif