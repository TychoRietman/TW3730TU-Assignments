#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int numbers[10];
    int largest;

    srand(time(NULL));

    printf("Random numbers:\n");

    for (int i = 0; i < 10; i++) {
        numbers[i] = rand() % 100 + 1;
        printf("%d ", numbers[i]);
    }

    largest = numbers[0];

    for (int i = 1; i < 10; i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
    }

    printf("\n\nLargest number: %d\n", largest);

    return 0;
}