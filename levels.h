#pragma once

#ifndef LEVELS_H
#define LEVELS_H

void initAddSubBracket();
void initMulDivBracket();
void initAddSubMulDivBracket();

struct EqAddSubBracket {
	unsigned short digit[100];
	char equation[100][1000];
};

struct EqMulDivBracket {
	unsigned short digit[100];
	char equation[100][1000];
};

struct EqAddSubMulDivBracket {
	unsigned short digit[100];
	char equation[100][1000];
};

extern struct EqAddSubBracket AddSubBracket;
extern struct EqMulDivBracket MulDivBracket;
extern struct EqAddSubMulDivBracket AddSubMulDivBracket;

#endif