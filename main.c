#include <stdio.h>
#include <string.h>
#include "levels.h"

extern struct EqAddSubBracket AddSubBracket;
extern struct EqMulDivBracket MulDivBracket;
extern struct EqAddSubMulDivBracket AddSubMulDivBracket;

unsigned int maxLengthOne(struct EqAddSubBracket* obj, unsigned int numberItr);
unsigned int maxLengthTwo(struct EqMulDivBracket* obj, unsigned int numberItr);
unsigned int maxLengthThree(struct EqAddSubMulDivBracket* obj, unsigned int numberItr);

int main() {
		//Length Max

	initAddSubBracket();
	initMulDivBracket();
	initAddSubMulDivBracket();

	unsigned int lengthAddSubBracket;
	unsigned int lengthMulDivBracket;
	unsigned int lengthAddSubMulDivBracket;

	lengthAddSubBracket = maxLengthOne(&AddSubBracket, 100);
	lengthMulDivBracket = maxLengthTwo(&MulDivBracket, 100);
	lengthAddSubMulDivBracket = maxLengthThree(&AddSubMulDivBracket, 100);

	float memoryAddSubBrackets = (lengthAddSubBracket * 100) / 1000.0f;
	float memoryMulDivBrackets = (lengthMulDivBracket * 100) / 1000.0f;
	float memoryAddSubMulDivBracket = (lengthAddSubMulDivBracket * 100) / 1000.0f;
	float memoryTotal = memoryAddSubBrackets + memoryMulDivBrackets + memoryAddSubMulDivBracket;

	printf("#==================Start===================================#\n");
	printf("Max length EqAddSubBracket: %d\n", lengthAddSubBracket);
	printf("Max length EqMulDivBracket: %d\n", lengthMulDivBracket);
	printf("Max length EqAddSubMulDivBracket: %d\n", lengthAddSubMulDivBracket);
	printf("#==================End=====================================#\n");

	FILE* file = fopen("result_length.txt", "w");

	if (file == NULL) {
		printf("File not opened!\n");
		return 1;
	}

	fprintf(file, "result length: \n");
	fprintf(file, "Max length EqAddSubBracket: %d\n", lengthAddSubBracket);
	fprintf(file, "Max length EqMulDivBracket: %d\n", lengthMulDivBracket);
	fprintf(file, "Max length EqAddSubMulDivBracket: %d\n", lengthAddSubMulDivBracket);
	fprintf(file, "\n");
	fprintf(file, "Memory EqAddSubBracket(kbite): %.1f\n", memoryAddSubBrackets);
	fprintf(file, "Memory EqMulDivBracket(kbite): %.1f\n", memoryMulDivBrackets);
	fprintf(file, "Memory EqAddSubMulDivBracket(kbite): %.1f\n", memoryAddSubMulDivBracket);
	fprintf(file, "Memory total(kbite): %.1f\n", memoryTotal);
	fclose(file);

	return 0;
}

unsigned int maxLengthOne(struct EqAddSubBracket *obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthTwo(struct EqMulDivBracket* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthThree(struct EqAddSubMulDivBracket* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}