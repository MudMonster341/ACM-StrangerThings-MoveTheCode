#include <stdio.h>

int main() {
    int num = 12345;
    int count = 0;

    while (num != 0) {
        count++;
        num /= 10;
    }

    printf("Digits = %d\n", count);
    return 0;
}
