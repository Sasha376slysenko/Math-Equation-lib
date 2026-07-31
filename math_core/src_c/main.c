#include <stdio.h>
#include <string.h>
#include "levels_eq.h"

extern struct EQ_4 eq_4;
extern struct EQ_5 eq_5;
extern struct EQ_6 eq_6;
extern struct EQ_7 eq_7;
extern struct EQ_8 eq_8;

unsigned int maxLengthFour(struct EQ_4* obj, unsigned int numberItr);
unsigned int maxLengthFive(struct EQ_5* obj, unsigned int numberItr);
unsigned int maxLengthSix(struct EQ_6* obj, unsigned int numberItr);
unsigned int maxLengthSeven(struct EQ_7* obj, unsigned int numberItr);
unsigned int maxLengthEight(struct EQ_8* obj, unsigned int numberItr);

int main() {
		//Length Max

	initeq_4();
	initeq_5();
	initeq_6();
	initeq_7();
	initeq_8();

	unsigned int length_eq_4;
	unsigned int length_eq_5;
	unsigned int length_eq_6;
	unsigned int length_eq_7;
	unsigned int length_eq_8;

	length_eq_4 = maxLengthFour(&eq_4, 10);
	length_eq_5 = maxLengthFive(&eq_5, 10);
	length_eq_6 = maxLengthSix(&eq_6, 10);
	length_eq_7 = maxLengthSeven(&eq_7, 10);
	length_eq_8 = maxLengthEight(&eq_8, 10);

	float memory_eq_4 = (length_eq_4 * 10) / 1000.0f;
	float memory_eq_5 = (length_eq_5 * 10) / 1000.0f;
	float memory_eq_6 = (length_eq_6 * 10) / 1000.0f;
	float memory_eq_7 = (length_eq_7 * 10) / 1000.0f;
	float memory_eq_8 = (length_eq_8 * 10) / 1000.0f;
	float memoryTotal = memory_eq_4 + memory_eq_5 + memory_eq_6 + memory_eq_7 + memory_eq_8;

	printf("#==================Start===================================#\n");
	printf("Max length Eq_4: %d\n", length_eq_4);
	printf("Max length Eq_5: %d\n", length_eq_5);
	printf("Max length Eq_6: %d\n", length_eq_6);
	printf("Max length Eq_7: %d\n", length_eq_7);
	printf("Max length Eq_8: %d\n", length_eq_8);
	printf("#==================End=====================================#\n");

	FILE* file = fopen("result_length.txt", "w");

	if (file == NULL) {
		printf("File not opened!\n");
		return 1;
	}

	fprintf(file, "result length: \n");
	fprintf(file, "Max length Eq_4: %d\n", length_eq_4);
	fprintf(file, "Max length Eq_5: %d\n", length_eq_5);
	fprintf(file, "Max length Eq_6: %d\n", length_eq_6);
	fprintf(file, "Max length Eq_7: %d\n", length_eq_7);
	fprintf(file, "Max length Eq_8: %d\n", length_eq_8);
	fprintf(file, "\n");
	fprintf(file, "Memory Eq_4(kbite): %.1f\n", memory_eq_4);
	fprintf(file, "Memory Eq_5(kbite): %.1f\n", memory_eq_5);
	fprintf(file, "Memory Eq_6(kbite): %.1f\n", memory_eq_6);
	fprintf(file, "Memory Eq_7(kbite): %.1f\n", memory_eq_7);
	fprintf(file, "Memory Eq_8(kbite): %.1f\n", memory_eq_8);
	fprintf(file, "Memory total(kbite): %.1f\n", memoryTotal);
	fclose(file);

	return 0;
}

unsigned int maxLengthFour(struct EQ_4* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthFive(struct EQ_5* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthSix(struct EQ_6* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthSeven(struct EQ_7* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}

unsigned int maxLengthEight(struct EQ_8* obj, unsigned int numberItr) {
	int lengthEq = 0;
	for (int i = 0; i < numberItr; i++) {
		if (strlen(obj->equation[i]) > lengthEq)
			lengthEq = strlen(obj->equation[i]);
	}
	return lengthEq;
}