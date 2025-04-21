#include <stdio.h>

int main() {
    int num = 1234;
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    printf("Sum of digits: %d\n", sum);
    return 0;
}
